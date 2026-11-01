# Object-Oriented Programming for Production

## 1. Project Goal

The goal of this learning project is to build a Vehicle Data Processing System that simulates how vehicle information is managed in a Computer Vision application.

The system represents detected vehicles as Python objects and manages their attributes, including vehicle ID, vehicle type, bounding box, speed, and movement status.

This project focuses on applying Object-Oriented Programming principles to build modular, maintainable, and reliable Python code that can later be integrated into the RoadGuard AI pipeline.

## 2. Class and Object

A Class is a blueprint that defines the attributes and behaviors of an object.

In this project, the `Vehicle` class defines the structure and behavior of a vehicle in the system.

An Object is an instance of a class with its own data.

Two Vehicle objects can share the same class while having different IDs, types, bounding boxes, speeds, and movement statuses.

The `Vehicle` class encapsulates both vehicle data and the methods used to manage that data.

## 3. Encapsulation

Encapsulation is the practice of controlling access to an object's internal data.

In the `Vehicle` class, internal attributes use a leading underscore (`_`) to indicate that they are intended for internal use.

Public `@property` methods provide read-only access to selected attributes.

This design encourages state changes to happen through controlled update methods.

For example:

- `vehicle.vehicle_id` allows reading the vehicle ID but not modifying it directly.
- `update_speed()` validates a new speed before updating the internal state.
- `update_bounding_box()` ensures that new coordinates satisfy geometric validation rules.

## 4. Data Validation

The `Vehicle` constructor validates initial data before assigning it to the object.

Update methods also validate new values before modifying internal attributes.

If validation fails, a `ValueError` is raised and the previous valid state is preserved.

The validation logic is separated into `validator.py` to keep the `Vehicle` class focused on managing vehicle data and behavior.

## 5. State Lifecycle

The `Vehicle` class distinguishes between an uninitialized state and a measured or analyzed state.

The initial values of `current_speed` and `status` are set to `None`.

The following values have different meanings:

- `None`: No measurement or analysis is available yet.
- `0.0`: A valid speed measurement indicates zero measured speed at that moment.
- `"unknown"`: Analysis has been performed, but the movement status cannot be determined.
- `"moving"`: The vehicle is classified as moving.
- `"stationary"`: The vehicle is classified as stationary.

The system treats movement status separately from accident status. A stationary vehicle does not necessarily indicate an accident.

## 6. Design Decisions

### Immutable Vehicle Identity

The `vehicle_id` is exposed through a read-only property and has no update method.

This decision preserves vehicle identity across consecutive video frames and helps maintain tracking consistency.

### Mutable Vehicle Attributes

The following attributes can change over time:

- `vehicle_type`
- `bounding_box`
- `current_speed`
- `status`

### Tuple for Bounding Boxes

Bounding boxes are represented as tuples containing four coordinates:

```python
(x1, y1, x2, y2)
