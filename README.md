# FastAPI Calculator

A simple calculator web application built with FastAPI. The app serves a static HTML/CSS/JavaScript frontend and evaluates arithmetic expressions on the backend using Python's `ast` module.

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, and division
- Parentheses support
- Simple web-based calculator UI
- FastAPI backend with JSON-based calculation endpoint
- Error handling for invalid expressions and division by zero

## Technologies Used

- Python
- FastAPI
- HTML/CSS/JavaScript
- Python `ast` evaluator

## Project Structure

```text
fastapi-calculator/
├── pyproject.toml
├── README.md
├── src/
│   └── fastapi_calculator/
│       ├── __init__.py
│       ├── main.py
│       ├── application.py
│       ├── Operation.py
│       └── static/
│           ├── index.html
│           ├── script.js
│           └── style.css
```

## Requirements

- Python 3.14+
- `uv` (recommended) or `pip`
- FastAPI


## Setup

### Using `uv` (recommended)

From the project root:

```bash
uv sync
```

Then start the app:

```bash
cd src/fastapi_calculator
uv run fastapi dev main.py
```

The app will run at:

```text
http://127.0.0.1:8000
```

### Using `pip`

If you prefer pip, install the dependencies first:

```bash
pip install "fastapi[standard]"
```

Then run:

```bash
cd src/fastapi_calculator
python -m fastapi dev main.py
```

## Usage

### Web UI

Open the browser at:

```text
http://127.0.0.1:8000/
```

Use the calculator buttons to enter an expression such as:

```text
(10 + 5) * 2
```

### API Endpoint

The app also exposes a REST API for calculating expressions.

#### Endpoint

```http
POST /calculate
```

#### Request Body

```json
{
  "expression": "10 + 5 * 2"
}
```

#### Example Response

```json
{
  "result": 20.0
}
```

#### Error Response

```json
{
  "detail": "Cannot Divide By Zero"
}
```

## Supported Operations

- `+` addition
- `-` subtraction
- `*` multiplication
- `/` division
- parentheses `(` and `)`

## Notes

The backend evaluates expressions by parsing them into an abstract syntax tree (`ast`) and then applying the relevant arithmetic rules. This keeps the implementation simple and safe for basic calculator use.

## License

This project is intended for learning and local development use.
