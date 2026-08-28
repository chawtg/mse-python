# College Management System – Activity Diagrams

## Overview

Based on the defined scope, **two activity diagrams** are created:

1. **Student Activity Diagram**
2. **Lecturer Activity Diagram**


---

# 1. Student Activity Diagram

The Student Activity Diagram represents the main workflow of a student using the College Management System. It covers finding available courses, viewing course details, enrolling in a course, and viewing enrolled courses.

```mermaid
flowchart TD
    A([Start]) --> B[Find Available Courses]
    B --> C[Select a Course]
    C --> D[View Course Details]
    D --> E{Enrol in Course?}

    E -- Yes --> F{Already Enrolled?}
    F -- No --> G[Enrol in Course]
    G --> H[Enrollment Successful]
    H --> I[View Enrolled Courses]

    F -- Yes --> J[Display Already Enrolled Message]
    J --> I

    E -- No --> I
    I --> K([End])
```


---

# 2. Lecturer Activity Diagram

The Lecturer Activity Diagram represents the main workflow of a lecturer using the College Management System. It covers viewing assigned courses, viewing enrolled students, and managing basic course information.

```mermaid
flowchart TD
    A([Start]) --> B[View Assigned Courses]
    B --> C[Select a Course]
    C --> D{Which action to choose?}

    D -- View Students --> E[View Enrolled Students]
    E --> F{Continue?}

    D -- Manage Course --> G[View Course Information]
    G --> H[Update Basic Course Information]
    H --> I[Save Course Information]
    I --> F

    F -- Yes --> C
    F -- No --> J([End])
```


