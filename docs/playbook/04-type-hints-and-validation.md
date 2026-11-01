# Type Hints and Data Validation

## 1. What We Learned

- Type Hints describe the expected types of variables, parameters, and return values.
- Python does not enforce Type Hints at runtime.
- Static Type Checkers detect potential type errors before execution.
- Runtime Validation checks actual input values during execution.
- `float | None` represents a value that can be either a float or `None`.
- `None` means no measurement is currently available, while `0.0` is a valid measurement.
- `-> None` indicates that a function does not return a meaningful value.
- Validators use `object` when they need to inspect inputs of unknown types.
- `isinstance()` helps verify runtime types and supports type narrowing.

## 2. Type Hints

Type Hints communicate the expected types of values.

Example:

```python
def calculate_speed(distance: float, time: float) -> float:
    return distance / time
