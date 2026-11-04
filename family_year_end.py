"""Total each family's payments for the year, for parent year-end statements.

Reads a payments file (Date, Family, Child, Method, Type, Amount) and prints,
for each family, the payments by type and the total paid in the year. Parents
claiming a dependent care FSA or the child care credit need what they paid
plus your name, address and taxpayer ID, so fill those in below before you
send anything. Which amounts count for the credit is for the parent and
their tax preparer to decide.

Usage: python3 family_year_end.py family-payments.csv 2026
Python 3, standard library only.
"""
import csv
import sys
from collections import defaultdict
from decimal import Decimal

PROVIDER = "Your center name, street address, city, state, ZIP. Taxpayer ID: __________"


def main(path, year):
    totals = defaultdict(lambda: defaultdict(Decimal))
    children = defaultdict(set)
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if not r["Date"].startswith(year):
                continue
            totals[r["Family"]][r["Type"]] += Decimal(r["Amount"])
            children[r["Family"]].add(r["Child"])
    print(f"Payments received in {year}")
    print(f"Provider: {PROVIDER}\n")
    grand = Decimal("0")
    for fam in sorted(totals):
        fam_total = sum(totals[fam].values())
        grand += fam_total
        print(f"{fam} family ({', '.join(sorted(children[fam]))})")
        for typ, amt in sorted(totals[fam].items()):
            print(f"  {typ}: {amt:,.2f}")
        print(f"  Total paid: {fam_total:,.2f}\n")
    print(f"All families: {grand:,.2f}. With every family in the file, this should agree with tuition and fee income in the books for the year.")


if __name__ == "__main__":
    a = sys.argv[1:] + [None] * 2
    main(a[0] or "family-payments.csv", a[1] or "2026")
