#!/usr/bin/env python3
"""Heuristic project inventory for ad-placement audits.

Usage:
    python scripts/inventory.py <project-root> [--json]

Finds candidate screens/routes, flags screens that should stay ad-free
(auth, payment, KYC, forms, settings, editors), and detects existing ad SDKs.
Results are HEURISTIC: always open the important files and confirm.
Standard library only.
"""
import json
import os
import re
import signal
import sys
from collections import defaultdict

SKIP_DIRS = {
    "node_modules", ".git", "dist", "build", ".next", ".nuxt", "out", "target",
    "vendor", "__pycache__", ".dart_tool", ".gradle", "Pods", ".venv", "venv",
    "coverage", ".turbo", ".cache", ".idea", ".vscode", "bin", "obj",
}
CODE_EXT = {".tsx", ".jsx", ".ts", ".js", ".vue", ".svelte", ".dart", ".kt",
            ".swift", ".java", ".html", ".tmpl", ".gohtml", ".py", ".go", ".rs"}
MAX_BYTES = 400_000

# Directories whose files are usually screens/pages.
SCREEN_DIRS = {"pages", "screens", "views", "routes", "app", "scenes", "templates",
               "features", "activities", "fragments"}
SCREEN_NAME_HINT = re.compile(
    r"(screen|page|view|activity|fragment|scene)\b|(Screen|Page|View|Activity|Fragment)\.",
)

PROTECTED = {
    "auth": r"login|log-in|signin|sign-in|signup|sign-up|register|registration|"
            r"password|forgot|reset|otp|2fa|mfa|verify|verification",
    "payment/checkout": r"checkout|payment|pay\b|billing|invoice|cart|order-confirm|"
                        r"momo|mobile-?money|wallet|transfer|withdraw|deposit|subscribe|subscription",
    "kyc/identity": r"kyc|identity|id-?upload|document-?upload|passport|licen[cs]e",
    "forms/creation": r"editor|compose|create|new-|upload|submit|form|wizard|onboarding-form",
    "settings/security": r"settings|security|privacy|account|profile-edit",
    "errors/system": r"error|404|500|offline|maintenance|unauthorized|forbidden",
    "safety/emergency": r"emergency|sos|safety|report-abuse|help-?center",
}
PROTECTED_RE = {k: re.compile(v, re.I) for k, v in PROTECTED.items()}

AD_SDKS = {
    "Google AdSense": r"adsbygoogle|pagead2\.googlesyndication|ca-pub-\d+",
    "Google Ad Manager / GPT": r"googletag|securepubads\.g\.doubleclick|gpt\.js",
    "Google AdMob (web/native)": r"ca-app-pub-\d+|google_mobile_ads|react-native-google-mobile-ads|"
                                 r"com\.google\.android\.gms\.ads|GoogleMobileAds|MobileAds\.initialize",
    "AppLovin / MAX": r"applovin|AppLovinSdk",
    "Unity Ads": r"UnityAds|unity3d\.ads|com\.unity3d\.ads",
    "ironSource / LevelPlay": r"ironsource|levelplay",
    "Meta Audience Network": r"audience[-_ ]?network|com\.facebook\.ads",
    "AdColony / Digital Turbine": r"adcolony|digitalturbine",
    "Taboola / Outbrain": r"taboola|outbrain",
    "Amazon Publisher Services": r"amazon-adsystem|apstag",
    "Carbon / EthicalAds / BuySellAds": r"carbonads|ethicalads|buysellads",
    "Generic ad terms": r"\b(interstitial|rewarded|banner[-_ ]?ad|native[-_ ]?ad|ad[-_ ]?slot|"
                        r"AdBanner|AdSlot|SponsoredCard|sponsored)\b",
}
AD_RE = {k: re.compile(v, re.I) for k, v in AD_SDKS.items()}


VERTICAL_HINTS = {
    "betting/gambling": r"\b(bet|bets|betting|sportsbook|odds|casino|jackpot|slots?|lottery|wager|bookmaker|stake)\b",
    "adult": r"\b(adult|nsfw|xxx|18\+|erotic)\b",
    "crypto/trading/forex": r"\b(crypto|bitcoin|token|forex|trading|exchange|wallet-connect|defi|nft)\b",
    "lending/fintech/payments": r"\b(loan|credit|lending|mobile-?money|momo|kyc|remittance|savings|insurance|bank)\b",
    "health/pharma": r"\b(health|clinic|patient|pharmacy|symptom|medical|therapy|prescription|telehealth)\b",
    "kids/education": r"\b(kids?|children|student|school|course|lesson|quiz|classroom|learn(ing)?)\b",
    "marketplace/classifieds": r"\b(listing|listings|marketplace|property|rent|landlord|seller|buyer|classified|vehicle)\b",
    "jobs/career": r"\b(jobs?|vacancy|vacancies|resume|cv|recruit|employer|candidate)\b",
    "e-commerce": r"\b(cart|checkout|product|catalog|sku|shop|store|order)\b",
    "video/audio/streaming": r"\b(video|stream(ing)?|podcast|episode|playlist|player|livestream)\b",
    "social/community": r"\b(feed|follow(ers)?|post|comment|community|chat|message)\b",
    "news/content": r"\b(article|news|blog|editorial|headline)\b",
    "dating": r"\b(dating|match(es)?|swipe|partner-?search)\b",
    "games": r"\b(game|level|score|leaderboard|player-?stats|unity)\b",
    "AI assistant/tools": r"\b(chatbot|llm|prompt|assistant|completion|embedding)\b",
}
VERTICAL_RE = {k: re.compile(v, re.I) for k, v in VERTICAL_HINTS.items()}

ROUTE_PATTERNS = [
    re.compile(r"<Route[^>]*\bpath=[\"']([^\"']+)[\"']"),               # react-router
    re.compile(r"\bpath:\s*[\"']([^\"']+)[\"']"),                       # route objects / vue-router
    re.compile(r"\b(?:GET|POST|HandleFunc|Handle)\(\s*[\"'](/[^\"']*)[\"']"),   # go/gin/echo/chi-ish
    re.compile(r"\b(?:router|app)\.(?:get|post|use)\(\s*[\"'](/[^\"']*)[\"']"),  # express
    re.compile(r"\bGoRoute\([^)]*path:\s*[\"']([^\"']+)[\"']", re.S),    # flutter go_router
    re.compile(r"\bnavigation\.navigate\(\s*[\"']([^\"']+)[\"']"),        # react-native
    re.compile(r"<Stack\.Screen[^>]*\bname=[\"']([^\"']+)[\"']"),         # react-native/expo
]


def walk(root):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".")]
        for f in filenames:
            ext = os.path.splitext(f)[1].lower()
            if ext in CODE_EXT or f in ("package.json", "pubspec.yaml", "go.mod",
                                        "Cargo.toml", "tauri.conf.json", "AndroidManifest.xml",
                                        "Info.plist", "requirements.txt", "build.gradle",
                                        "manifest.json", "manifest.webmanifest") \
                    or f.lower().startswith("readme"):
                yield os.path.join(dirpath, f), dirpath, f, ext


def read(path):
    try:
        if os.path.getsize(path) > MAX_BYTES:
            return ""
        with open(path, "r", encoding="utf-8", errors="ignore") as fh:
            return fh.read()
    except OSError:
        return ""


def classify(rel, text_sample=""):
    hits = []
    low = rel.lower()
    for label, rx in PROTECTED_RE.items():
        if rx.search(low):
            hits.append(label)
    return hits


def is_screen_file(rel, name, ext):
    parts = {p.lower() for p in rel.replace("\\", "/").split("/")[:-1]}
    if ext not in {".tsx", ".jsx", ".vue", ".svelte", ".dart", ".kt", ".swift", ".java",
                   ".html", ".tmpl", ".gohtml"}:
        return False
    if SCREEN_NAME_HINT.search(name) or parts & SCREEN_DIRS:
        return True
    return False


def next_route(rel):
    """Derive a route from Next.js / Expo / SvelteKit file-based routing."""
    r = rel.replace("\\", "/")
    m = re.search(r"(?:^|/)(?:src/)?(app|pages)/(.*)$", r)
    if not m:
        return None
    tail = m.group(2)
    base = os.path.basename(tail)
    stem = os.path.splitext(base)[0]
    if m.group(1) == "app" and stem not in ("page", "index", "+page", "layout") :
        return None
    if stem in ("_app", "_document", "layout") or tail.startswith("api/"):
        return None
    route = "/" + os.path.dirname(tail).strip("/")
    if m.group(1) == "pages" and stem not in ("index",):
        route = route.rstrip("/") + "/" + stem
    return re.sub(r"/+", "/", route) or "/"


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    as_json = "--json" in sys.argv
    if not args or not os.path.isdir(args[0]):
        print(__doc__)
        sys.exit(1)
    root = os.path.abspath(args[0])

    stack = set()
    screens, routes = [], defaultdict(set)
    ads = defaultdict(list)
    protected_files = defaultdict(list)
    surfaces = set()
    corpus = []   # lightweight text used only for vertical hints

    for path, dirpath, name, ext in walk(root):
        rel = os.path.relpath(path, root)
        low_rel = rel.lower()
        if name == "AndroidManifest.xml" or low_rel.endswith("build.gradle"):
            surfaces.add("Android app")
        if name == "Info.plist" or "/ios/" in "/" + low_rel.replace("\\", "/"):
            surfaces.add("iOS app")
        if name in ("manifest.webmanifest", "manifest.json") and ext == ".json":
            if "manifest" in name and "start_url" in read(path):
                surfaces.add("PWA (web manifest)")
        if name in ("service-worker.js", "sw.js", "serviceworker.js"):
            surfaces.add("PWA (service worker)")
        corpus.append(low_rel.replace("\\", " ").replace("/", " ").replace("-", " ").replace("_", " "))
        # stack detection
        if name == "package.json":
            t = read(path)
            for key, label in (("\"next\"", "Next.js"), ("\"react-native\"", "React Native"),
                               ("\"expo\"", "Expo"), ("\"react\"", "React"), ("\"vue\"", "Vue"),
                               ("\"svelte\"", "Svelte"), ("@tauri-apps", "Tauri"),
                               ("\"electron\"", "Electron")):
                if key in t:
                    stack.add(label)
        elif name == "pubspec.yaml":
            stack.add("Flutter")
        elif name == "go.mod":
            stack.add("Go")
        elif name == "tauri.conf.json" or name == "Cargo.toml":
            if name == "tauri.conf.json":
                stack.add("Tauri")
        elif name == "requirements.txt":
            stack.add("Python")

        if name.lower().startswith("readme") or name == "package.json":
            corpus.append(read(path)[:4000])
        text = read(path) if ext in CODE_EXT or name in (
            "package.json", "pubspec.yaml", "requirements.txt", "build.gradle",
            "AndroidManifest.xml", "Info.plist", "Cargo.toml") else ""

        # ad SDK detection
        if text:
            for label, rx in AD_RE.items():
                m = rx.search(text)
                if m:
                    ads[label].append(f"{rel} ({m.group(0)[:40]})")

        # routes
        if text and ext in CODE_EXT:
            for rx in ROUTE_PATTERNS:
                for m in rx.finditer(text):
                    routes[m.group(1)].add(rel)

        fr = next_route(rel) if ext in {".tsx", ".jsx", ".ts", ".js", ".svelte", ".vue"} else None
        if fr:
            routes[fr].add(rel)

        if is_screen_file(rel, name, ext):
            flags = classify(rel)
            screens.append({"file": rel, "flags": flags})
            for fl in flags:
                protected_files[fl].append(rel)

    # classify routes too
    route_rows = []
    for r, files in sorted(routes.items()):
        flags = classify(r)
        route_rows.append({"route": r, "files": sorted(files)[:3], "flags": flags})

    blob = " ".join(corpus)
    vertical_scores = {}
    for label, rx in VERTICAL_RE.items():
        n = len(rx.findall(blob))
        if n:
            vertical_scores[label] = n
    top_verticals = sorted(vertical_scores.items(), key=lambda kv: -kv[1])[:5]
    if "Flutter" in stack or "React Native" in stack or "Expo" in stack:
        surfaces.add("Cross-platform mobile app")
    if "Tauri" in stack or "Electron" in stack:
        surfaces.add("Desktop app")
    if any(x in stack for x in ("Next.js", "React", "Vue", "Svelte")) and not surfaces:
        surfaces.add("Web (confirm mobile vs desktop usage)")

    data = {
        "root": root,
        "surface_hints": sorted(surfaces),
        "vertical_hints": [{"vertical": k, "keyword_hits": v} for k, v in top_verticals],
        "stack_hints": sorted(stack),
        "screens_found": len(screens),
        "routes_found": len(route_rows),
        "existing_ad_signals": {k: v[:8] for k, v in ads.items()},
        "protected_candidates": {k: v[:15] for k, v in protected_files.items()},
        "routes": route_rows[:200],
        "screens": screens[:300],
        "note": "Heuristic output. Confirm by reading the files; dynamic routes and "
                "server-rendered templates may be missed.",
    }

    if as_json:
        print(json.dumps(data, indent=2))
        return

    print(f"# Project inventory: {root}")
    print(f"Stack hints: {', '.join(data['stack_hints']) or 'none detected'}")
    print(f"Surface hints: {', '.join(data['surface_hints']) or 'none detected'}")
    if top_verticals:
        print("Vertical hints (keyword counts, CONFIRM with the owner): " +
              ", ".join(f"{k} ({v})" for k, v in top_verticals))
        if any(k.startswith("betting") for k, _ in top_verticals):
            print("  -> Gambling signals found: read references/vertical-playbooks.md section 2 and run the eligibility gate.")
    print(f"Screen-like files: {len(screens)}   Routes: {len(route_rows)}\n")

    print("## Existing ad signals")
    if ads:
        for k, v in ads.items():
            print(f"- {k}: {len(v)} hit(s), e.g. {v[0]}")
    else:
        print("- none detected")

    print("\n## Routes")
    for row in route_rows[:120]:
        tag = f"  [PROTECTED: {', '.join(row['flags'])}]" if row["flags"] else ""
        print(f"- {row['route']}  ({row['files'][0] if row['files'] else ''}){tag}")
    if not route_rows:
        print("- none detected (check navigation setup manually)")

    print("\n## Screen-like files")
    for s in screens[:150]:
        tag = f"  [PROTECTED: {', '.join(s['flags'])}]" if s["flags"] else ""
        print(f"- {s['file']}{tag}")

    print("\n## Protected-flow candidates (default NO AD, confirm)")
    if protected_files:
        for k, v in protected_files.items():
            print(f"- {k}: {len(v)} file(s)")
    else:
        print("- none flagged by name; still check auth, payment and forms manually")

    print("\nNOTE: heuristic only. Open the key files and confirm before relying on this.")


if __name__ == "__main__":
    if hasattr(signal, "SIGPIPE"):
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)  # quiet when piped to head
    main()
