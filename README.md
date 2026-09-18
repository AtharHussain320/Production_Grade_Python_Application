# Final Task 1 — Production-Grade Python Application

## Simple Sales Tracker

A lightweight command-line sales management application developed with Python.

The purpose of this project is to demonstrate how a small Python application can be organized with persistent storage, configuration, input validation, logging, exception handling, and automated testing.

---

## Project Overview

The Simple Sales Tracker allows a user to:

- Add new sales records
- View existing sales
- Calculate total sales
- Store information permanently
- Validate user input
- Handle missing or corrupted files
- Record important application events
- Run automated tests

The application is designed to remain simple and easy to maintain while following practical programming practices.

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| JSON | Data persistence |
| unittest | Automated testing |
| logging | Application logging |
| pathlib | File handling |

No external Python packages are required.

---

## Project Structure

```text
Production_App/
│
├── app.py
├── config.json
├── data.json
├── test_app.py
├── app.log
└── README.md
