[![Playwright Tests](https://github.com/royav84/playwright_saucedemo/actions/workflows/tests.yml/badge.svg)](https://github.com/royav84/playwright_saucedemo/actions/workflows/tests.yml)


# Playwright Saucedemo — QA Automation Portfolio

Senior QA Engineer with 13+ years of experience. This repo contains UI automation tests built with Playwright and pytest against saucedemo.com.

## What's covered

- Login flow — valid login, invalid credentials, locked out user
- Inventory page — title, product count, filter visibility, sorting (A-Z, Z-A)
- Cart — add single item, add all items, remove item, badge validation
- Checkout — form validation, missing fields, price calculation, order confirmation
- CI/CD — GitHub Actions pipeline runs all tests on every push

## Tech stack

- Python
- Playwright
- pytest
- Page Object Model (POM)

## How to run

Install dependencies:
```bash
pip install playwright pytest pytest-playwright
playwright install
```

Run all tests:
```bash
pytest
```

## Test structure

- `pages/` — Page Object Model classes
- `tests/` — test files
- `conftest.py` — shared fixtures
