# Project 7 Report: Automated Testing with Pytest

> [!IMPORTANT]
> **AUTOGRADER COMPLIANCE INSTRUCTIONS:**
> This report is parsed automatically by the autograder. To ensure you receive full credit for your work:
> 1. **Do not modify** the section headers (`## ...`) or bold field keys (e.g., `**Name:**`, `**Pytest Version & Framework:**`, `**GitHub Repository URL:**`, etc.).
> 2. **Write your answers directly after** the colon `:` of each field, replacing the placeholder text completely (including the outer brackets `[` and `]`).
> 3. **Maintain the file structure**. Changing headers, bold titles, or deleting lines can cause the autograder to miss your responses and award 0 marks.

---

## Student Information
- **Name:** WUT YEE PHYO
- **MMDT ID:** MMDT004

---

## Section 1: Test Suite Configuration
- **Pytest Version & Framework:** Pytest 9.1.1 with pytest-cov, running on Python 3.10.2.
- **Total Test Cases Written:** 187 test cases across the three test modules.
- **Measured Code Coverage (%):** 100% statement coverage across `src/` (213 statements).
- **Key Fixtures Implemented:** `empty_manager` provides a fresh manager, `sample_student` provides a valid student, `populated_manager` provides students with grades, and `valid_registration_data` provides a valid registration payload.

---

## Section 2: Test Case Design & Boundary Analysis
- **Calculator Boundary & Edge Cases:** Tests cover valid and invalid inputs, empty and single-item sequences, score limits of 0 and 100, and just-out-of-range scores. Prime tests include negative values, 0, 1, small primes, and composites. Factorial and power tests check zero, negative, and invalid-type cases.
- **Validator Exception Scenarios:** Tests check valid email and username formats, malformed email addresses, and password length and complexity requirements. They assert the specific exception type and message for invalid data, including weak passwords, invalid ages, wrong input types, and missing registration fields. Registration tests also verify that validation errors from individual fields propagate.
- **Student Manager State Transitions:** Tests verify creating and adding students, rejecting duplicate IDs without overwriting records, retrieving students, and errors for unknown IDs. They check grade updates, GPA recalculation, removal and updated counts, plus ranking and GPA filtering. Grade and GPA tests exercise score bounds and every GPA conversion bracket.

---

## Section 3: Local Verification & Feature Checklist
*Check the test modules and features you successfully implemented and verified locally by placing an `x` in the brackets (e.g., `[x]`):*
- [x] Module 1: Calculator Unit Tests with Boundary & Type Assertions (`test_calculator.py`)
- [x] Parameterized Testing with `@pytest.mark.parametrize` for Multiple Input Scenarios
- [x] Module 2: Data Validator Tests with Custom Exception Assertions (`pytest.raises`)
- [x] Module 3: Student Management System Tests with State Mutation & CRUD Verification
- [x] Reusable Pytest Fixtures in `conftest.py` for Modular Test Setup
- [x] Mutation Testing & Bug Detection Verification (Catching Hidden Mutants)
- [x] Code Coverage Analysis with `pytest-cov` (>= 85% Coverage)

---

## Section 4: Deployed and Presentation Information
- **GitHub Repository URL:** https://github.com/ariesphyo/Automated-Testing-with-Pytest
- **Video Presentation Link:** Pending: record and upload the required 5–7 minute presentation.

---

## Section 5: Discussion
*Provide your written analysis for each point by replacing the bracket placeholders below:*
- **Explain why a test suite that passes 100% does not guarantee code correctness, and how mutation testing or evaluating tests against buggy code verifies test suite effectiveness.**
    Passing all tests only shows that the current implementation satisfies the scenarios those tests cover; untested behavior or weak assertions can still hide defects. Mutation testing introduces small, deliberate code changes, and a test suite demonstrates bug-detection strength when its tests fail on those mutants. Mutants that survive can reveal missing test cases or assertions, although equivalent mutants may not represent a real behavior change.
- **Compare classical unit and integration testing in software engineering with modern AI engineering evaluation (e.g., LLM benchmarks, unit testing AI agents/tool calls, and Process Reward Models / LLM-as-a-judge).**
    Classical unit and integration tests typically check defined behavior with repeatable inputs and expected outputs, including interactions between components. AI evaluation also uses benchmarks and task-specific tests, but must account for probabilistic outputs by assessing quality across representative examples rather than relying only on exact matches. Agent tool-call tests can verify schemas and actions, while Process Reward Models and LLM-as-a-judge assess intermediate reasoning or response quality and should be calibrated against human judgments because they can be inconsistent or biased.
