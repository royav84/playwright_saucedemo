# Playwright Saucedemo — QA Automation Portfolio

Senior QA Engineer with 13+ years of experience. This repo contains UI automation tests built with Playwright and pytest against saucedemo.com.

## What's covered

- Login flow — valid login, invalid credentials, locked out user
- Inventory page — title, product count, filter visibility
- Add to cart — cart badge validation
- Product sorting — A to Z, Z to A filter validation

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
