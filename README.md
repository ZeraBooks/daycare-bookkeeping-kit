# Daycare bookkeeping kit

Bookkeeping for a daycare records parent tuition, state subsidy payments and
CACFP food reimbursements as separate income, matches each subsidy deposit to
the children and weeks it covers, books payroll from the payroll report, and
keeps what each family paid so year-end statements are right. This kit has the
accounts, a checklist and two small scripts.

## Files

| File | What it is |
|---|---|
| `chart-of-accounts.csv` | A starting chart of accounts for a licensed center: tuition, subsidy, food program and fees as separate income, prepaid tuition as a liability. Columns: Number, Name, Type, Detail, Notes. |
| `month-end-checklist.md` | Eight monthly steps plus the January job of parent year-end statements. |
| `subsidy-remittance.csv` | A fictional subsidy remittance: 14 children, four weeks each, weekly rate and amount per child. |
| `september-2026-month.csv` | A fictional center's September 2026 on cash basis: every line, its account, and whether it counts in profit. |
| `check_subsidy_month.py` | Checks each child's line on the remittance, ties the remittance to the subsidy deposit, and prints revenue by source and profit. |
| `family-payments.csv` | A fictional year of payments for three families, one row per payment. |
| `family_year_end.py` | Totals each family's payments for the year, by type, for parent year-end statements. |

Both scripts are Python 3, standard library only.

## How to use it

1. Import `chart-of-accounts.csv` into your accounting software, or compare it
   with the accounts you have. Home daycares use the same income lines and add
   home expense accounts.
2. Each month, fill in a copy of `subsidy-remittance.csv` from the remittance
   notice and run:

   ```
   python3 check_subsidy_month.py subsidy-remittance.csv september-2026-month.csv
   ```

3. Keep every parent payment in a file shaped like `family-payments.csv`, or
   export one from your child care software. In January run:

   ```
   python3 family_year_end.py family-payments.csv 2026
   ```

   Fill in your center's name, address and taxpayer ID at the top of the
   script first.
4. Work through `month-end-checklist.md` before you lock each month.

## The worked month

Little Acorn Learning Center is a fictional licensed center with 48 children
enrolled. September 2026, cash basis:

| | Amount |
|---|---|
| Parent tuition, card and ACH | 38,700.00 |
| State subsidy deposit, 14 children | 11,240.00 |
| CACFP reimbursement for August meals | 2,165.00 |
| Registration fees, 3 new families | 450.00 |
| **Revenue** | **52,555.00** |
| Payroll, gross wages | 29,800.00 |
| Employer payroll taxes | 2,279.70 |
| Groceries | 3,980.00 |
| Classroom supplies | 1,120.00 |
| Rent | 7,500.00 |
| Liability insurance | 890.00 |
| Card and ACH fees | 420.00 |
| **Expenses** | **45,989.70** |
| **Profit** | **6,565.30** |

The 2,165.00 food deposit pays for August's meals, while September's 3,980.00
of groceries will be reimbursed in October. That is why one month's food line
never looks right on its own. Compare food cost with food income over a
quarter instead.

The three families in `family-payments.csv` are a separate small sample, not
Little Acorn's 48 children.

All figures are fictional.

## Home daycares

A home daycare uses part of the house for the business. The IRS lets daycare
providers work out a time-space percentage: the share of the home used for
child care times the share of hours it is used. Rent or mortgage interest,
utilities and insurance are then deducted at that percentage (IRS Publication
587). The books keep the household bills and a log of hours; your accountant
does the calculation.

## FAQ

### Why does the subsidy deposit need to be matched to children?

It arrives as one deposit for many children, usually after attendance is
submitted. Without the split by child and week, you can't tell which families
still owe their copay and which weeks are still unpaid.

### What do parents need at year end?

Families claiming a dependent care FSA or the child care credit (Form 2441)
need what they paid and the provider's name, address and taxpayer ID. That
only works if tuition was recorded by family all year.

### Is a nonprofit child care center different?

Yes. A nonprofit center also tracks grants and restricted funds and files a
Form 990.

## Learn more

Full guide: [Bookkeeping for daycares](https://www.zerabooks.com/bookkeeping-for-daycares). Related: [ZeraBooks](https://www.zerabooks.com/), accounting software that does your books for you, with free setup and a free catch-up of your past months.

## License

The content and data in this repository are licensed under
[CC BY 4.0](LICENSE). Free to use and adapt with credit to ZeraBooks.
The code (`*.py`) is licensed under [MIT](LICENSE-CODE).

Maintained by [ZeraBooks](https://www.zerabooks.com).
