"""Plan toner reorders from level and daily page use.

Usage: python3 main.py printers.csv [--pages-per-cartridge 2000]
CSV columns: printer,toner_percent,pages_per_day.
Days until empty = remaining pages / pages per day, using the
cartridge page yield. REORDER when under 14 days left, OK otherwise,
UNKNOWN when the printer reports no daily usage.
"""
import argparse, csv, sys

REORDER_DAYS = 14

def plan(rows, pages_per_cartridge=2000):
    out = []
    for row in rows:
        toner = float(row["toner_percent"])
        per_day = int(row["pages_per_day"])
        if per_day <= 0:
            days = None
        else:
            days = (toner / 100.0 * pages_per_cartridge) / per_day
        if days is None:
            verdict = "UNKNOWN"
        elif days < REORDER_DAYS:
            verdict = "REORDER"
        else:
            verdict = "OK"
        out.append((row["printer"].strip(), toner, per_day, days, verdict))
    return sorted(out, key=lambda r: (r[3] is None, r[3] if r[3] is not None else 0))

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    parser.add_argument("--pages-per-cartridge", type=int, default=2000)
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        for printer, toner, per_day, days, verdict in plan(list(csv.DictReader(f)), args.pages_per_cartridge):
            days_text = f"{days:.1f} days left" if days is not None else "no usage data"
            print(f"{printer}: {verdict} ({toner:g}% toner, {per_day} pages/day, {days_text})")
    return 0

if __name__ == "__main__":
    sys.exit(main())
