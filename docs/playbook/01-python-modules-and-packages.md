## Python Modules and Packages

- A Module is a Python file containing reusable code.
- A Package organizes related Python modules.
- `__init__.py` initializes a regular Python package.
- import allows modules to reuse code from other modules.
- `main.py` is the application's entry point.
- The main guard prevents automatic execution during imports.
- Separation of Concerns improves maintainability and testability.

## Python Import System

- Absolute Imports use the full package path to locate a module.
- Relative Imports use dots (`.`) to reference modules within the current package.
- Running a Python file directly does not provide package context for relative imports.
- The `-m` flag runs a module with its package context.
- `sys.path` contains directories where Python searches for modules and packages.
- The current working directory is included in the search path when using `python -c`.
- `__file__` identifies the location of an imported module or package file.
- Running Python from the correct project context helps maintain reliable imports.

### Key Concepts
- Absolute Import
- Relative Import
- Module Search Path
- Current Working Directory
- Package Context
- `python -m`
- `sys.path`
- `__file__`

## Type Hints and Runtime Validation

- Type Hints describe the expected types of variables, parameters, and return values.
- Python does not enforce Type Hints at runtime.
- Static Type Checkers detect potential type errors before execution.
- Runtime Validation checks actual input values during execution.
- `float | None` represents a value that can be either a float or None.
- `None` means no measurement is currently available, while `0.0` is a valid measurement.
- `-> None` indicates that a function does not return a meaningful value.
- Validators use `object` when they need to inspect inputs of unknown types.
- `isinstance()` helps verify runtime types and supports type narrowing.

### Key Concepts
- Type Hints
- Union Types
- Static Type Checking
- Runtime Validation
- Type Narrowing
- Return Type
- Optional Values

### Static Type Checking with mypy

- mypy is a static type checker for Python.
- Static Type Checking detects potential type errors without executing the application.
- Type Inference allows tools to infer variable types from assigned values.
- Variable Annotations explicitly declare expected variable types.
- Union Types allow variables to hold multiple possible types.
- Initializing a variable with `None` may require an explicit Union Type.
- `python -m mypy vehicle` checks the vehicle package.
- A successful mypy check does not guarantee runtime correctness.

### Development Dependencies

- mypy is a development dependency because it supports code quality checks rather than application runtime functionality.
