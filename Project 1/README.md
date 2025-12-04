# Retail Automation Framework (Playwright + Python)

# Project Overview

This repository hosts a **Unified UI Automation Framework** designed for high-traffic retail environments (e.g., Best Buy, Target,Amazon). It utilizes Playwright and Pytest to execute scalable, resilient end-to-end tests against the Swag Labs e-commerce platform.

The framework prioritizes speed, stability, and debugging capability, featuring Network Mocking to simulate backend failures and Auto-Trace Generation for rapid root-cause analysis.

# Architecture Design

The framework follows a modular Page Object Model (POM) structure to ensure maintainability and code reusability

# Project 1/

├── pages/                 # Page Objects (Locators & Business Logic)

│   ├── base_page.py       # Wrapper methods-safe actions (Waits, Safe Clicks)

│   ├── login_page.py      # Login functionality

│   ├── products_page.py   # Inventory management

 └── cart_page.py          # add to cart , remove item

│   └── checkout_page.py   # Cart & Checkout flows
│
├── tests/                 # Test Scripts

│   ├── test_e2e_flow.py   # Critical User Journeys (Happy Path)

│   ├── test_login.py      # Data-Driven Login Tests

│   └── test_network.py    # Chaos Engineering (Mocking 500 Errors)

 └── test_sorting.py   # sort prices from HiLo in products page

  └── test_cart_logic.py   # Dtaa Persistance- session and DOM Reactivity

   └── test_error_handling.py   # Negative Testing- going to inventory page without loggin in/clciking submit without entering shipping info

│
├── conftest.py            # The "Brain" (Fixtures, Hooks, Tracing)


└── requirements.txt       # Dependencies


 # Key Features
 
a) Hybrid Page Object Model: Separates locators (pages/) from test logic (tests/) using a strict inheritance model (BasePage parent class).

b) Self-Healing Reporting: A custom pytest hook in conftest.py automatically captures Trace Viewer (.zip) files and Screenshots immediately upon test failure.

c) Network Mocking (Chaos Testing): Uses page.route() to intercept network traffic, simulating CDN failures and API timeouts to verify UI resilience.

d) Data-Driven Testing: Utilizes @pytest.mark.parametrize to validate multiple user personas (Standard, Locked Out, Glitch) in a single execution.

e) Parallel Execution: Integrated with pytest-xdist to run tests concurrently across multiple worker nodes, reducing regression time by 60%.

# Setup & Installation

# 1. Clone the Repository

git clone https://github.com/Dimplegurajala/Playwright-Automation.git

cd "Project 1"

# 2. Create Virtual Environment

python -m venv venv
source venv/bin/activate  # Mac/Linux
.\venv\Scripts\activate   # Windows

# 3. Install Dependencies

pip install -r requirements.txt
playwright install

# 4. How to Run Tests

## a) Run All Tests (Headless if not explicity mentioned headed)

pytest


## b) Run with Visual Debugging (Headed + Slow Mo)

pytest --headed --slowmo 500


## c) Run in Parallel (Auto-Scaling)

pytest -n auto


## d) Generate HTML Report

pytest --html=reports/report.html

## e) Failure Analysis (Time Travel Debugging)

If a test fails, the framework automatically generates a Trace Zip in the reports/ folder with timestamps.

Walk through the timeline to see the exact state of the DOM and Network calls at the moment of failure.


# CI/CD Integration

This project is fully integrated with GitHub Actions.

## i) Trigger: Pushes to main branch.

## ii) Environment: Ubuntu Latest.

## iii) Artifacts: Automatically uploads HTML reports and Traces to GitHub artifacts upon pipeline failure.


# Dimple Gurajala SDET-QA Automation Tester | Python Automation Specialist
