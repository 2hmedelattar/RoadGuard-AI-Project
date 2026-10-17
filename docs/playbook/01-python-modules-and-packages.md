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
