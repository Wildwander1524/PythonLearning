# Day 1 Homework — BankAccount

Week 1, Day 1 of the 3-month AI study plan.

## What this covers
Python OOP: classes, `__init__`, instance vs class attributes, encapsulation, properties, and transaction history.

## How to run

```bash
# Manual smoke-test
python bank_account.py

# Run all tests
python test_bank_account.py
```

## Skills demonstrated
- Class definition, `__init__`, `self`
- Private attributes (`_balance`) + read-only `@property`
- Input validation with `ValueError`
- Class attributes shared across instances (`account_count`)
- List-based history with copy-on-read
