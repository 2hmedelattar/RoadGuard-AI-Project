## What we did 
- Created a Git repository and verified its configuration.
- Added a `.gitignore` file to exclude unnecessary files.
- Installed standalone Python 3.12.10.
- Created and activated a project-specific virtual environment.
- Created an empty `requirements.txt` file.
- Added the initial `README.md`.
- Created the documentation structure.

## Key Concepts
| Concept | Description | Why it matters |
|---|---|---|
| Git | A version control system | Tracks project changes |
| Python Interpreter | Executes Python code | Runs the application |
| Virtual Environment | An isolated Python environment | Prevents dependency conflicts |
| Dependency | An external package required by the project | Provides additional functionality |
| `requirements.txt` | A file listing project dependencies | Helps reproduce the environment |
| `.gitignore` | Defines files Git should ignore | Keeps unnecessary files out of the repository |
| `README.md` | The project's introduction and documentation | Helps developers understand the project |

## Decision Log
| Decision | Reason | Trade-off |
|---|---|---|
| Use `pip` + `venv` instead of `Conda` | Lightweight, standard Python tooling and project isolation | Python versions must be installed separately |
| Use Python 3.12.10 | Selected as the project's Python interpreter | Requires checking package compatibility |

## Mistakes and Fixes
| Mistake | Cause | Fix |
|---|---|---|
| Created `.gitigonre` instead of `.gitignore` | Filename typo | Renamed the file using `mv` |

## Interview Questions
1. What is the difference between a Python interpreter and a virtual environment?
2. Why should each Python project have its own virtual environment?
3. What is the purpose of `requirements.txt`, and how does it differ from `.venv`?
