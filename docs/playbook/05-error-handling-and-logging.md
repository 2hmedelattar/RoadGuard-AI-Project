# Error Handling and Logging

## 1. What We Did

- Introduced error handling for invalid operations.
- Used exceptions to communicate failures.
- Added centralized logging configuration.
- Configured separate log files for general system events and errors.
- Used a named logger for the RoadGuard application.

## 2. Error Handling

Error handling allows an application to respond to unexpected situations without failing unpredictably.

Python provides several mechanisms:

- `try`
- `except`
- `else`
- `finally`
- `raise`

## 3. Exceptions

An exception represents an error or unexpected condition during program execution.

Examples include:

| Exception | Meaning |
|---|---|
| `ValueError` | A value has the correct general type but is invalid |
| `TypeError` | An operation receives an inappropriate type |
| `FileNotFoundError` | A requested file does not exist |
| `PermissionError` | The process does not have the required permission |
| `IsADirectoryError` | A file operation was attempted on a directory |
| `OSError` | An operating-system-related error |

## 4. Raising Exceptions

The `raise` statement explicitly raises an exception.

Example:

```python
raise ValueError("Invalid vehicle speed.")
