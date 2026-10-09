# Math App

Math App is a desktop application developed in Python using Tkinter. It provides a collection of mathematical tools through a graphical user interface.

## Features

- **Multiplication Table** – displays a multiplication table and allows filtering products by divisor, including all, even, and odd products.
- **Prime Numbers** – displays prime numbers up to a specified limit.
- **GCD and LCM** – calculates the greatest common divisor (GCD) and least common multiple (LCM) of numbers.
- **Geometric Shapes** – draws geometric shapes on a canvas based on user-defined dimensions.
- **User Authentication** – supports user registration, login, and logout using a local SQLite database.

## Technologies

- Python
- Tkinter
- SQLite
- CSV
- Git and GitHub

## Project Structure

```text
math-app-python/
├── data/
│   └── multiplication_table.csv
├── src/
│   ├── app_state.py
│   ├── auth.py
│   ├── auth_ui.py
│   ├── gcd_lcm.py
│   ├── main.py
│   ├── multiplication_table.py
│   ├── prime.py
│   ├── primes_gcd_lcm_functionality.py
│   ├── select_1.py
│   ├── shapes_functionality.py
│   ├── test_functionality.py
│   └── utils.py
└── .gitignore
```

## Running the Application

Make sure Python 3 is installed on your computer.

From the project root directory, run:

```bash
python src/main.py
```

The application uses a local SQLite database for user authentication. The database file is created when the application connects to it, provided the configured database path is correct.

## Notes

This project was developed as an individual programming project to practise Python programming, GUI development, mathematical functionality, and local data storage.
