# Student Enrolment System

## Scenario Description

The university has a student enrolment system for different subjects.

## Additional Attributes

The following attributes can be added to the respective entities:

- **Student:** Email, Contact_no
- **Subject:** Credits

## Relationships Between Entities

| Entities | Relationship | Description |
|---|---|---|
| **Student – Enrolment** | One-to-Many | One student can have many enrolments, but each enrolment belongs to one student. |
| **Enrolment – Lecture** | Many-to-One | One enrolment can have one lecture, while one lecture can have many enrolments. |
| **Lecturer – Lecture** | One-to-Many | One lecturer can teach multiple lectures, while each lecture is taught by one lecturer. |
| **Subject – Lecture** | One-to-Many | One subject can have multiple lectures, and each lecture belongs to one subject. |