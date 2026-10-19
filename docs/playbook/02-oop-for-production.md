# Object-Oriented Programming for Production

## 1. Project Goal

The goal of this learning project is to build a Vehicle Data Processing System that simulates how vehicle information is managed in a Computer Vision application.

The system represents detected vehicles as Python objects and manages their attributes, including vehicle ID, vehicle type, bounding box, speed, and movement status.

This project focuses on applying Object-Oriented Programming principles to build modular, maintainable, and reliable Python code that can later be integrated into the RoadGuard AI pipeline.

## 2. Class and Object

A **Class** is a blueprint that defines the attributes and behaviors of an object.

In this project, the `Vehicle` class defines the structure and behavior of a vehicle in the system.

An **Object** is an instance of a class with its own data.

For example, two Vehicle objects can share the same class while having different vehicle IDs, types, bounding boxes, speeds, and movement statuses.

The `Vehicle` class encapsulates both vehicle data and the methods used to manage that data.

## 3. Encapsulation

Encapsulation is the practice of controlling access to an object's internal data.

In the `Vehicle` class, internal attributes use a leading underscore (`_`) to indicate that they are intended for internal use.

Public `@property` methods provide read-only access to these attributes.

This design prevents direct modification through the public interface and ensures that state changes happen through controlled update methods.

For example:
- `vehicle.vehicle_id` allows reading the vehicle ID but not modifying it directly.
- `update_speed()` validates a new speed before updating the internal state.
- `update_bounding_box()` ensures that new coordinates satisfy the geometric validation rules.

## 4. Data Validation

Data validation ensures that the system only accepts values that follow the expected rules.

Validation logic is separated into `validator.py` to keep the `Vehicle` class focused on managing vehicle data and behavior.

The validator module provides functions to validate:

- Vehicle IDs: must be non-negative integers.
- Vehicle types: must belong to the supported vehicle categories.
- Bounding boxes: must contain four finite numeric coordinates and satisfy geometric constraints.
- Speeds: must be finite, non-negative numeric values.
- Movement statuses: must be one of the supported states.

The `Vehicle` constructor validates initial data before assigning it to the object.

Update methods also validate new values before modifying internal attributes. If validation fails, a `ValueError` is raised and the previous valid state is preserved.

## 5. State Lifecycle

The `Vehicle` class distinguishes between an uninitialized state and a measured or analyzed state.

The initial values of `current_speed` and `status` are set to `None`.

This represents the fact that no speed measurement or movement analysis has been performed yet.

The following values have different meanings:

- `None`: No measurement or analysis is available yet.
- `0.0`: A valid speed measurement indicates zero measured speed at that moment. Movement status may require additional temporal analysis.
- `"unknown"`: Analysis has been performed, but the movement status cannot be determined.
- `"moving"`: The vehicle is classified as moving.
- `"stationary"`: The vehicle is classified as stationary.

The system treats movement status separately from accident status. A stationary vehicle does not necessarily indicate an accident.

## 6. Design Decisions

### Immutable Vehicle Identity

The `vehicle_id` is exposed through a read-only property and has no update method.

This decision preserves vehicle identity across consecutive video frames and helps maintain tracking consistency.

### Mutable Vehicle Attributes

The `vehicle_type`, `bounding_box`, `current_speed`, and `status` can change over time.

- Vehicle type may be refined by subsequent classification results.
- Bounding box changes as the vehicle moves between frames.
- Speed is updated as new measurements become available.
- Movement status changes according to the latest analysis.

### Tuple for Bounding Boxes

Bounding boxes are represented as tuples containing four coordinates: `(x1, y1, x2, y2)`.

Using a tuple prevents individual coordinate values from being modified directly and encourages updating the bounding box as a complete unit.

### Separation of Validation and Contextual Checks

Geometric validation checks the internal structure and coordinate relationships of a bounding box.

Checking whether coordinates fall within a specific frame's boundaries requires additional frame dimensions and will be handled separately in the video processing pipeline.

## 7. Testing Results

The `Vehicle` class was manually tested through `main.py`.

The following scenarios were verified:

| Test Scenario | Expected Behavior | Result |
|---|---|---|
| Create a vehicle with valid data | Object is created successfully | Passed |
| Create a vehicle with an invalid ID | Raise `ValueError` | Passed |
| Modify the vehicle ID directly | Raise `AttributeError` | Passed |
| Update speed with valid data | Update the speed | Passed |
| Update speed with invalid data | Preserve the previous valid speed | Passed |
| Update bounding box with valid data | Update the bounding box | Passed |
| Update bounding box with invalid data | Preserve the previous valid bounding box | Passed |
| Update vehicle type with valid data | Update the vehicle type | Passed |
| Update vehicle type with invalid data | Preserve the previous valid type | Passed |
| Initialize speed and status | Both start as `None` | Passed |

These tests confirm the expected behavior of the constructor, encapsulation, validation, and state management.

**Note:** These are manual tests, not automated unit tests. Automated testing with `pytest` will be introduced in a later development step.
