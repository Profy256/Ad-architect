#!/usr/bin/env python3
"""Deterministic regression check: does the skill's text contain the guidance
each eval prompt needs? It cannot judge model output; it catches missing guidance.
Run:  python evals/check_coverage.py   (from the skill root)"""
import os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def load(*names):
    out = ""
    for n in names:
        with open(os.path.join(ROOT, n), encoding="utf-8") as f:
            out += f.read() + "\n"
    return out.lower()

CORE = ["SKILL.md", "references/ad-posture.md", "references/audit-templates.md",
        "references/policy-and-trust.md", "references/ad-format-taxonomy.md"]
CHECKS = {
 1: (CORE + ["references/vertical-playbooks.md", "references/product-playbooks.md",
             "references/market-context.md", "references/platform-playbooks.md"], {
   "default non-interruptive": r"non-interruptive ads have the highest priority",
   "readiness / low traffic": r"monetization readiness check",
   "featured/sponsored listings first": r"featured/promoted/boosted listings",
   "payment/deposit protected": r"deposit|payment confirmation",
   "contact form protected": r"contact forms?|contact/call/pay",
   "app-open guidance": r"app-open",
   "challenge owner's assumption": r"challenge the project owner",
   "mobile money advertiser payments": r"mobile-money payment",
   "worked example report": r"example-report\.md",
 }),
 2: (CORE + ["references/product-playbooks.md", "references/platform-playbooks.md"], {
   "mid-roll only at breaks": r"mid-roll only at|chapter",
   "timer mid-roll rejected": r"timer firing mid-sentence|timer.*rejection|arbitrary time",
   "no ads in quizzes": r"quiz",
   "rewarded unlock": r"rewarded unlock",
   "tradeoff block": r"option a",
   "quick decision mode": r"quick decision mode|question-sized",
 }),
 3: (CORE + ["references/implementation-standards.md"], {
   "adsense is web, apps use admob": r"adsense is a website product|adsense.*not.*apps|apps use admob",
   "network capability matrix": r"network capability",
   "badge alone not enough": r"badge is all that",
   "no bare modulo": r"index % 5",
   "reserve slot size": r"reserve the slot",
   "register native asset views": r"register the asset views",
   "verify live policy": r"check the network's current native ad policy|verify",
 }),
 4: (CORE + ["references/vertical-playbooks.md", "references/platform-playbooks.md"], {
   "gambling restricted by google": r"online gambling",
   "responsible gambling messages": r"responsible-gambling|responsible gaming",
   "self-exclusion": r"self-exclu",
   "loss chasing": r"loss-chasing",
   "bet slip protected": r"bet slip",
   "quiet hours": r"quiet hours",
   "play gambling requirements": r"valid licen[cs]e",
   "regulator directives text": r"directive",
 }),
 5: (CORE + ["references/vertical-playbooks.md", "references/market-context.md"], {
   "child-directed treatment": r"child-directed",
   "coppa": r"coppa",
   "families self-certified sdk": r"families self-certified",
   "teen category restrictions": r"teen",
   "no ads in lessons/quizzes": r"never during lessons|ads never during lessons",
   "age split rule for 10-17": r"under 13.*(whole|entire)|mixed-age.*under-13|treat the under-13",
   "non-ad revenue for minors": r"school.*licen[cs]|institution|parent-paid|subscription",
 }),
 6: (CORE + ["references/platform-playbooks.md", "references/product-playbooks.md"], {
   "tauri first-party sponsor cards": r"first-party sponsor cards",
   "editor/settings protected": r"editors?, file operations|never inside editors",
   "license/update flows protected": r"license and update|update dialogs|license/update",
   "invoicing/billing protected": r"invoice|billing",
   "offline degrade": r"degrade to nothing",
   "inventory script": r"inventory\.py",
 }),
 7: (CORE + ["references/product-playbooks.md"], {
   "assumed posture stated": r"state that it is an assumption|assumed default",
   "reserve list": r"held in reserve",
   "ask posture question": r"how much interruption",
   "recipe / cook mode protected": r"cook mode|cooking mode|step-by-step mode",
 }),
 8: (CORE + ["references/implementation-standards.md"], {
   "explicit opt-in honored": r"explicit opt-in",
   "rewarded prompt before ad": r"reward stated before",
   "natural break interstitial": r"natural break",
   "frequency cap overrides 'after every'": r"unbounded|every single|after each|cap by default",
   "grace period for new users": r"grace period",
 }),
}
fails = 0
for eid, (files, checks) in CHECKS.items():
    text = load(*files)
    for name, rx in checks.items():
        ok = re.search(rx, text) is not None
        if not ok:
            fails += 1
        print(f"eval {eid} | {'PASS' if ok else 'FAIL'} | {name}")
print(f"\n{fails} gap(s)")
sys.exit(1 if fails else 0)
