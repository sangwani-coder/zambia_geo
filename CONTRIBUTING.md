# Contributing to Zambia Geo

We welcome contributions from everyone! This guide will help you get started with contributing to our Zambia geographical data package.

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Environment](#development-environment)
- [Making Changes](#making-changes)
- [Adding New Data](#adding-new-data)
- [Testing](#testing)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Reporting Issues](#reporting-issues)
- [Requesting Features](#requesting-features)
- [Code Review](#code-review)
- [License](#license)

## Code of Conduct

All contributors must adhere to our [Code of Conduct](CODE_OF_CONDUCT.md). Please read it before participating.

## Getting Started

1. **Fork** the repository on GitHub
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/zambia_geo.git
   cd zambia_geo
   
3. **Set up the upstream remote:**
   ```bash
      git remote add upstream https://github.com/sangwani-coder/zambia_geo.git

## Development Environment

**Prerequisites:***
- Python 3.6+
- pip
- virtualenv (recommended)

### Setup
1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate    # Windows
2. Install dependencies:
   ```bash
   pip install -e .[dev]

## Making Changes
1. Create a new branch
   ```bash
   git checkout -b type/description

### Branch naming conventions:
   - feature/add-new-province
   - fix/city-data-error
   - docs/update-contributing

2. Make your changes following the code style:
   - Use 4 spaces for indentation
   - Follow PEP 8 guidelines
   - Include type hints
   - Add docstrings for public functions
  
3. Format your code before committing:
   ```bash
      black zambia_geo tests
      isort zambia_geo tests

## Adding New Data
**To add new provinces or cities**:
*Edit:* zambia_geo/data.py
   #### Follow this structure:
   ```bash
   "New Province": {
    "capital": "Capital City",
    "area_km2": 00000,
    "population": 000000,
    "cities": [
        {
            "name": "City Name",
            "is_capital": False,
            "population": 00000,
            "coordinates": {"lat": 0.0, "lng": 0.0}  # Optional
        }
    ]
}
```
### Add tests for new data in tests/test_data.py
Run the test suite with:
```bash
   pytest
```

We aim for 100% test coverage. Check coverage with:
```bash
   pytest --cov=zambia_geo --cov-report=term-missing
```

## Commit Guidelines
Use Conventional Commits style:
      
      type(scope): description
      
**Examples**:

      feat(data): add new cities for Copperbelt province
      fix(utils): correct population formatting
      docs(readme): update installation instructions

## Pull Request Process
**Ensure your branch is up-to-date**:
```bash
   git fetch upstream
   git rebase upstream/main
```
* Push your changes:
```
git push origin your-branch-name
```
**Create a Pull Request on GitHub with**:
- Clear title and description
- Reference related issues
- Screenshots if applicable
- Respond to review feedback

## Reporting Issues
**When creating an issue**:
- Use the issue template
- Include steps to reproduce
- Add expected vs actual behavior
### Provide environment details:
```
Zambia Geo version: X.Y.Z
Python version: 3.X
OS: Windows/Linux/Mac
```
### Requesting Features
**For feature requests**:
- Check if a similar request exists
- Describe the feature and its benefits
- Provide use cases
- Suggest implementation ideas if possible

### Code Review
**All PRs require**:
- Two approving reviews
- Passing CI checks
- Updated documentation
- Proper test coverage

**Reviewers will**:
- Verify code quality
- Check for consistency
- Ensure proper test coverage
- Validate data accuracy

### License
By contributing, you agree to license your work under the project's MIT License.
