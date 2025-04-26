[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18875142)
# CRUD App Project: Multi-Table Database Application

## Overview
In this project, you will design and implement a CRUD (Create, Read, Update,
Delete) application using SQLite and Python. Unlike the introductory example,
your application must manage a dataset with **multiple tables and complex
relationships**. You will also implement a simple command-line interface (CLI)
to interact with your database.

## Project Requirements

### 1. Choose a Dataset
Select a dataset that consists of at least **three related tables**. Feel free
to use datasets that you have used previously in this class.
Here are some ideas:

  - **Pokedex Dataset** (Pokemon, items, location, etc.): You can
  choose to focus on a subset of the dataset, and also add new simple feature such
  as a player owning a set of pokemons
  - **Library System** (Books, Authors, Borrowers)
  - **Student Management** (Students, Courses, Enrollments)
  - **E-commerce Store** (Customers, Orders, Products)
  - **Movie Database** (Movies, Actors, Directors)
  - **Event Registration** (Events, Participants, Venues)

Your database should model real-world relationships, including:

  - **One-to-Many Relationships** (e.g., one author writes many books)
  - **Many-to-Many Relationships** (e.g., students enroll in multiple courses,
  and courses have multiple students)

### 2. Database Design
Create an ER diagram or write a brief description of your tables and their
relationships. Your tables should include:

  - **Primary keys** to uniquely identify records
  - **Foreign keys** to establish relationships between tables
  - **Constraints** to maintain data integrity (e.g., `NOT NULL`, `UNIQUE`)

### 3. Implement CRUD Operations
Implement basic CRUD operations:

  - **Create**: Insert new records
  - **Read**: Retrieve records with filtering options
  - **Update**: Modify existing records
  - **Delete**: Remove records while maintaining data integrity

### 4. Command-Line Interface (CLI)
Your application should include a simple CLI for users to:

  1. Add new records
  2. View records
  3. Update existing records
  4. Delete records
  5. Exit the application

### 5. Implement a Search Feature

  - Allow users to search for records using at least **one meaningful filter**
  (e.g., find all books by a certain author, all courses a student is enrolled in, etc.).

### 6. Data Validation

  - Ensure user input is valid (e.g., prevent negative ages, enforce required fields).

### 7. Extra Challenge

  - If you want additional experience or challenge, feel free to implement your
  CRUD app on the web via fastapi and uvicorn as per
  https://github.com/env3d-lessons/sql-crud/blob/main/README2.md

## Example Database Schema (Student Management System)

```sql
CREATE TABLE Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);

CREATE TABLE Courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    instructor TEXT NOT NULL
);

CREATE TABLE Enrollments (
    student_id INTEGER,
    course_id INTEGER,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES Students(id),
    FOREIGN KEY (course_id) REFERENCES Courses(id)
);
```

## Submission Instructions

  1. Implement your project and thoroughly test CRUD operations.

  2. Write a short PROJECT.md file explaining:

    - Your chosen dataset
    - The relationships between your tables
    - How to run your application

  3. Submit your project via github with the following command:

    ```
    git add -A
    git commit -m 'submit'
    git push
    ```
    
  4. Present and demo your project at the last day of class.


## Grading Criteria

| Criteria               | Points |
|------------------------|--------|
| Database Design and Diagram (tables & relationships) | 20 |
| CRUD Operations        | 20 |
| Command-Line Interface (CLI) | 10 |
| Search Feature        | 10 |
| Data Validation & Error Handling | 10 |
| PROJECT.md Documentation  | 10 |
| Presentataion | 20 |
| **Total**             | **100** |


