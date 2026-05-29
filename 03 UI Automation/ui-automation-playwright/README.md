# UI Automation with Playwright and Pytest

## Overview
This repository contains the UI Automation testing framework developed using Python, Playwright, and Pytest. It is designed to perform End-to-End (E2E) and Regression testing on web applications. The framework strictly adheres to the Page Object Model (POM) design pattern to ensure maintainability, readability, and scalability of the test scripts.

## Project Structure
The project is organized into the following directory structure:

- **.github/workflows/**: Contains the continuous integration (CI) configuration for GitHub Actions.
- **fixtures/**: Houses test configurations and test data (e.g., test-data.json).
- **pages/**: Contains Page Object classes representing different pages of the web application.
- **reports/**: The output directory for generated HTML test reports.
- **tests/**: Contains the actual test scripts.
  - **e2e/**: End-to-End test scenarios.
  - **regression/**: Regression and smoke test scenarios.
- **conftest.py**: Pytest configuration file for defining globally accessible fixtures.
- **playwright_config.py**: Core configuration parameters such as environment variables and base URLs.
- **pytest.ini**: Default runtime arguments and configurations for Pytest.
- **requirements.txt**: List of Python dependencies required to run the project.

## Prerequisites
Before setting up the project, ensure that the following software is installed on your system:
- Python 3.11 or higher
- pip (Python package installer)
- Git

## Installation Guide
1. Navigate to the project directory:
   ```bash
   cd "03 UI Automation/ui-automation-playwright"
   ```

2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install Playwright browsers and dependencies:
   ```bash
   playwright install
   ```

## Test Execution
The framework uses Pytest as the test runner. Default configurations are already specified in the `pytest.ini` file.

- **Run all tests**:
  ```bash
  pytest
  ```

- **Run tests in headed mode (visible browser window)**:
  ```bash
  pytest --headed
  ```

- **Run a specific test file**:
  ```bash
  pytest tests/e2e/test_login.py
  ```

- **Run tests concurrently (requires pytest-xdist)**:
  ```bash
  pytest -n auto
  ```

## Reporting
The framework is configured to generate a self-contained HTML report automatically after every test execution. 
- The report is saved to `reports/report.html`.
- In the event of a test failure, screenshots, videos, and trace files are automatically captured and attached to the report for debugging purposes.

## Continuous Integration
This project integrates with GitHub Actions. The workflow is located at `.github/workflows/playwright.yml`. It is triggered automatically upon push or pull request events to the main branch. The CI pipeline executes the complete test suite and uploads the HTML report as an artifact accessible directly from the GitHub interface.