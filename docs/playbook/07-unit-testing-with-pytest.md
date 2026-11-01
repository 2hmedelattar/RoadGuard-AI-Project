# Unit Testing with Pytest

## 1. What We Did

- Installed Pytest as a development dependency.
- Created automated tests for vehicle validation.
- Created automated tests for the Vehicle class.
- Used fixtures to provide reusable test objects.
- Used parametrization to test multiple input cases.
- Used `pytest.raises()` to verify expected exceptions.

## 2. What Is Unit Testing?

Unit Testing verifies that individual units of code behave as expected.

A unit can be:

- A function.
- A method.
- A class behavior.

In RoadGuard, tests help verify that vehicle data validation and object state management work correctly.

## 3. Why Automated Testing Matters

Automated tests help:

- Detect bugs early.
- Prevent regressions.
- Verify expected behavior.
- Support safe refactoring.
- Increase confidence in code changes.

## 4. Pytest Discovery

Pytest discovers test files using naming conventions.

Common patterns:

- `test_*.py`
- `*_test.py`

Test functions commonly start with:

```python
def test_...():
    pass
