# Clean Code and Professional Tooling

## 1. What We Did

- Introduced Ruff as the project's code quality tool.
- Configured Ruff through `pyproject.toml`.
- Enabled selected linting rules.
- Configured code formatting.
- Fixed linting issues.
- Verified formatting, tests, and static type checking.
- Added Ruff to development dependencies.

## 2. Why Code Quality Tools Matter

Professional software development requires more than code that runs successfully.

Code should also be:

- Readable.
- Consistent.
- Maintainable.
- Easy to review.
- Easier to test.
- Less likely to contain common mistakes.

Automated tools help enforce consistent standards.

## 3. Ruff

Ruff is a Python linter and formatter.

It helps identify code quality issues and automatically format Python files.

The project uses Ruff for:

- Linting.
- Import sorting.
- Code formatting.
- Detecting common code issues.

## 4. Ruff Configuration

The project configuration is stored in:

```text
pyproject.toml
