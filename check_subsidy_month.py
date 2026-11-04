"""Check a daycare's subsidy remittance and month in this repo's layout.

1. Every child on the subsidy remittance reads across: weeks x weekly rate =
   amount, and the remittance total agrees with the subsidy deposit in the
   month file.
2. Profit is every "In profit" line in the month file added up, with revenue
   shown by source (tuition, subsidy, food program, fees).

Usage: python3 check_subsidy_month.py subsidy-remittance.csv september-2026-month.csv
Python 3, standard library only.
"""
import csv
import sys
from decimal import Decimal


def d(cell):
    return Decimal(cell.strip()) if cell and cell.strip() else Decimal("0")


def main(remit_path, month_path):
    ok = True
    total = Decimal("0")
    children = 0
    with open(remit_path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            expected = d(r["Weeks"]) * d(r["Weekly rate"])
            if expected != d(r["Amount"]):
                ok = False
                print(f"{r['Child']}: {r['Weeks']} weeks x {r['Weekly rate']} is {expected:,.2f}, remittance says {r['Amount']}")
            total += d(r["Amount"])
            children += 1
    print(f"Subsidy remittance: {children} children, {total:,.2f}")

    income = expenses = Decimal("0")
    by_account = {}
    with open(month_path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            amt = d(r["Amount"])
            if r["In profit"].strip().lower() != "yes":
                continue
            if amt >= 0:
                income += amt
                by_account[r["Account"]] = by_account.get(r["Account"], Decimal("0")) + amt
            else:
                expenses -= amt
    for acct, amt in by_account.items():
        print(f"  {acct}: {amt:,.2f} ({amt / income * 100:.1f}% of revenue)")
    if by_account.get("Subsidy income", Decimal("0")) != total:
        ok = False
        print(f"Subsidy income in the month is {by_account.get('Subsidy income', Decimal('0')):,.2f}, remittance is {total:,.2f}")
    print(f"Revenue {income:,.2f}, expenses {expenses:,.2f}, profit {income - expenses:,.2f}")
    print("All checks pass." if ok else "Some checks failed; see above.")
    return ok


if __name__ == "__main__":
    a = sys.argv[1:] + [None] * 2
    sys.exit(0 if main(a[0] or "subsidy-remittance.csv", a[1] or "september-2026-month.csv") else 1)
