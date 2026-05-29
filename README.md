# Tester Project

## Overview
This repository serves as a centralized workspace for various software testing disciplines. It encompasses manual testing documentation, API testing automation, and User Interface (UI) test automation. The objective is to maintain a structured, comprehensive, and scalable testing environment.

## Repository Structure
The repository is segmented into three primary domains:

### 1. 01 Manual Testing
This directory is designated for manual testing artifacts. It includes test plans, test cases, test scenarios, and requirement traceability matrices (RTM).

### 2. 02 API Testing
This directory contains the API automation testing projects.
- **api-testing-postman/**: A Postman-based API testing framework. It utilizes Postman Collections and Environment variables to execute automated API assessments. Tests can be executed via the Postman application or the Newman command-line interface.

### 3. 03 UI Automation
This directory is dedicated to frontend test automation.
- **ui-automation-playwright/**: A Python-based UI automation framework built with Playwright and Pytest. It follows the Page Object Model (POM) architecture and includes comprehensive End-to-End (E2E) and smoke tests. GitHub Actions are integrated for continuous integration.

## Getting Started
To interact with specific projects within this repository, please navigate to the respective subdirectories and refer to their isolated `README.md` files for detailed installation and execution instructions.

- For UI Automation instructions, refer to: `03 UI Automation/ui-automation-playwright/README.md`
- For API Testing instructions, refer to: `02 API Testing/api-testing-postman/README.md`

## Version Control
This repository uses Git for version control. All changes to the automation frameworks and testing artifacts are tracked here to ensure transparent collaboration and historical integrity.