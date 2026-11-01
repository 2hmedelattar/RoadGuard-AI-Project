# Project Structure and Imports

## 1. What We Learned

- `main.py` is the application's entry point.
- The main guard prevents application code from executing automatically during imports.
- Absolute Imports use the full package path.
- Relative Imports use dots to reference modules within the current package.
- Running a Python file directly does not provide package context for relative imports.
- The `-m` flag runs a module with its package context.
- `sys.path` contains directories where Python searches for modules and packages.
- `__file__` identifies the location of a Python module file.

## 2. Project Structure

The project separates application entry points, reusable modules, tests, and documentation.

Example:

```text
RoadGuard-AI-Project/
├── vehicle/
│   ├── __init__.py
│   ├── processor.py
│   └── validator.py
├── tests/
├── docs/
├── main.py
├── requirements.txt
└── README.md
