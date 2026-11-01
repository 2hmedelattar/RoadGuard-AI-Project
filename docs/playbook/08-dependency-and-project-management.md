# Dependency and Project Management

## 1. What We Did

- Organized project dependencies into separate files.
- Separated runtime dependencies from development dependencies.
- Added version pins for development tools.
- Installed dependencies using pip.
- Verified dependency consistency.

## 2. What Is a Dependency?

A dependency is an external package or library required by a project.

Dependencies provide functionality without requiring the project to implement everything from scratch.

For example, RoadGuard may use external packages for Computer Vision, Deep Learning, API development, and testing.

## 3. Runtime vs. Development Dependencies

### Runtime Dependencies

Packages required for the application to run.

Examples planned for future RoadGuard development include:

- OpenCV.
- PyTorch.
- Other Computer Vision libraries.

### Development Dependencies

Packages used during development, testing, and code quality checks.

The project currently uses:

- `pytest`
- `mypy`
- `ruff`

These tools support development rather than the application's runtime functionality.

## 4. Dependency Files

### requirements.txt

Contains runtime dependencies.

Current content:

```text
# Runtime dependencies
