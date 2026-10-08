#!/usr/bin/env python3
"""Back-of-envelope ad revenue estimator for the monetization readiness check.

It NEVER supplies eCPMs or prices: you must pass them, so every number in the
output is traceable to a stated assumption. Replace assumptions with real
network/advertiser data as soon as you have it.

Usage examples
--------------
Programmatic units (impressions-based):
  python scripts/revenue_estimator.py --mau 3000 --sessions 10 \
    --unit "native feed:3:0.6:2.0:0.8" --unit "banner:2:0.2:0.8:0.7"
    # name : impressions per session : eCPM low : eCPM high : fill rate (0-1)

Direct-sold slots (flat price):
  python scripts/revenue_estimator.py --mau 3000 --sessions 10 \
    --direct "featured listing:6:20:0.3:0.7"
    # name : slots available : price per slot per month : sell-through low : sell-through high

Both can be combined. Currency is whatever you use consistently.
"""
import argparse
import sys


def parse_unit(s):
    p = [x.strip() for x in s.split(":")]
    if len(p) != 5:
        raise ValueError(f"--unit needs name:imps_per_session:ecpm_low:ecpm_high:fill, got {s!r}")
    name, imps, lo, hi, fill = p
    imps, lo, hi, fill = float(imps), float(lo), float(hi), float(fill)
    if not 0 <= fill <= 1:
        raise ValueError("fill must be between 0 and 1")
    if lo > hi:
        lo, hi = hi, lo
    return name, imps, lo, hi, fill


def parse_direct(s):
    p = [x.strip() for x in s.split(":")]
    if len(p) != 5:
        raise ValueError(f"--direct needs name:slots:price_per_slot_per_month:sell_low:sell_high, got {s!r}")
    name, slots, price, lo, hi = p
    slots, price, lo, hi = float(slots), float(price), float(lo), float(hi)
    if not (0 <= lo <= 1 and 0 <= hi <= 1):
        raise ValueError("sell-through must be between 0 and 1")
    if lo > hi:
        lo, hi = hi, lo
    return name, slots, price, lo, hi


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--mau", type=float, required=True, help="monthly active users")
    ap.add_argument("--sessions", type=float, required=True, help="sessions per active user per month")
    ap.add_argument("--unit", action="append", default=[], help="programmatic unit (see usage)")
    ap.add_argument("--direct", action="append", default=[], help="direct-sold slot (see usage)")
    ap.add_argument("--viewable", type=float, default=1.0,
                    help="share of impressions that are billable/viewable (default 1.0; lower it if you know better)")
    a = ap.parse_args()

    if not a.unit and not a.direct:
        print("Provide at least one --unit or --direct. No default prices are assumed on purpose.")
        sys.exit(2)

    rows = []
    total_lo = total_hi = 0.0
    for u in a.unit:
        name, imps, lo, hi, fill = parse_unit(u)
        monthly_imps = a.mau * a.sessions * imps * fill * a.viewable
        r_lo, r_hi = monthly_imps * lo / 1000, monthly_imps * hi / 1000
        rows.append((f"programmatic: {name}", f"{monthly_imps:,.0f} billable imps", r_lo, r_hi))
        total_lo += r_lo
        total_hi += r_hi
    for d in a.direct:
        name, slots, price, lo, hi = parse_direct(d)
        r_lo, r_hi = slots * price * lo, slots * price * hi
        rows.append((f"direct: {name}", f"{slots:g} slots x {price:g}", r_lo, r_hi))
        total_lo += r_lo
        total_hi += r_hi

    print(f"Assumptions: MAU={a.mau:,.0f}, sessions/user/month={a.sessions:g}, viewable={a.viewable:g}")
    print("All prices, eCPMs, fill and sell-through are YOUR assumptions; none are defaults.\n")
    print(f"{'Source':38} {'Volume':28} {'Low/mo':>10} {'High/mo':>10}")
    for n, v, lo, hi in rows:
        print(f"{n:38} {v:28} {lo:>10,.2f} {hi:>10,.2f}")
    print("-" * 90)
    print(f"{'TOTAL per month':38} {'':28} {total_lo:>10,.2f} {total_hi:>10,.2f}")
    print(f"{'Per active user per month':38} {'':28} {total_lo / a.mau:>10,.4f} {total_hi / a.mau:>10,.4f}")
    print(f"{'Per year':38} {'':28} {total_lo * 12:>10,.2f} {total_hi * 12:>10,.2f}")
    print("\nReading guide: compare the TOTAL with the cost of the UX risk (retention loss, development time,"
          " SDK weight, support). If programmatic totals are tiny relative to direct-sold totals, lead with"
          " sponsorships and featured listings. Validate every input with real data before presenting revenue as fact.")


if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(f"Input error: {e}")
        sys.exit(2)
