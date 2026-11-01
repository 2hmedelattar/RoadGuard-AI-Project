# File I/O and Data Processing

## 1. What We Did

- Implemented file reading and writing.
- Used context managers to manage file resources.
- Added error handling for common file operations.
- Introduced JSON serialization and deserialization.
- Added validation for loaded vehicle data.

## 2. File I/O

File I/O means reading data from files and writing data to files.

Python provides the built-in `open()` function.

Example:

```python
with open("vehicles.txt", "r", encoding="utf-8") as file:
    content = file.read()
