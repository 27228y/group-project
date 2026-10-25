# Python Calculator - Project Documentation & Report

## 1. Executive Summary & Objectives
This document outlines the design, development, and project management lifecycle of the **Python Calculator** project. Built by a collaborative team of 6 students, this project demonstrates real-world software engineering practices using **GitHub**, including Kanban board tracking, branch-based development, and peer code reviews.

## 2. Team Structure & Role Distribution
To meet individual contribution criteria, responsibilities were strictly divided among 6 team members:
- **Project Manager (PM):** Coordinated team workflow, managed the GitHub Kanban board, and tracked milestones.
- **Analyst (BA):** Formulated core system requirements and user stories.
- **Documentation Specialist:** Managed project markdown files, README, and structured documentation (`documentation.md`).
- **Backend Developer 1:** Implemented core arithmetic logic and mathematical operations (`add`, `subtract`, `multiply`, `divide`).
- **Backend Developer 2 / Integrator:** Implemented error handling, input validation, and bug fixes (NameError and logic fixes).
- **QA (Quality Assurance) & DevOps:** Designed the test plan, managed GitHub issues, performed bug tracking, and handled repository security and merge rules.

## 3. System Architecture & Features
### Core Features
- Basic arithmetic operations: Addition, Subtraction, Multiplication, Division.
- Robust input validation to catch non-numeric entries.
- Zero-division error handling to prevent application crashes.

### Code Structure (`calculator.py`)
```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y
```

## 4. Software Development Lifecycle & GitHub Workflow
The team followed a professional Git workflow to ensure transparency and version control:
1. **Issue Tracking:** Issues and bugs (such as name errors and logic issues) were logged via GitHub Issues with detailed steps to reproduce.
2. **Kanban Management:** Tasks were organized across GitHub Projects columns (`To Do`, `In Progress`, `Done`).
3. **Branching & Pull Requests:** Developers wrote code in isolated feature branches (`fix/calculator-bugs`), submitted Pull Requests, and required peer code reviews and approvals (`Approve`) before merging into `main`.

## 5. Testing & Quality Assurance
- **Bug 1 (Critical):** Application crashed with a `NameError` due to a variable typo (`nums1` instead of `num1`) during subtraction. Resolved via Pull Request `#9`.
- **Bug 2 (Logic):** Subtraction function returned addition (`x + y` instead of `x - y`). Fixed and verified through team code review.

## 6. Conclusion
The Python Calculator project successfully delivers a functional, tested, and well-managed software product, showcasing effective teamwork, clear individual contributions, and professional version control practices.