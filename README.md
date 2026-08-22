# FastAPI Calculator

A small calculator application built with FastAPI. It serves a browser-based calculator UI and evaluates expressions through a backend API using Python's `ast` module.

## Features

- Arithmetic support for `+`, `-`, `*`, and `/`
- Parentheses support
- Frontend calculator UI with buttons and display
- REST API endpoint for expression evaluation
- Division-by-zero handling
- Basic validation for invalid expressions

## Project Structure

```text
Fastapi_calculator/
├── .gitignore
├── .python-version
├── pyproject.toml
├── README.md
├── src/
│   └── fastapi_calculator/
│       ├── __init__.py
│       ├── main.py
│       ├── service.py
│       └── static/
│           ├── index.html
│           ├── script.js
│           └── style.css
```

## Application Behavior

- The root route serves the calculator frontend from `static/index.html`.
- The frontend sends POST requests to `/calculate` with a JSON body.
- The backend evaluates the expression and returns the result.
- A `ZeroDivisionError` is converted into an HTTP 400 error response.

## Requirements

- Python 3.14+
- FastAPI
- `uv` (recommended) or `pip`

## Setup

### Using `uv`

From the project root:

```bash
uv sync
```

Then start the app:

```bash
cd src/fastapi_calculator
uv run fastapi dev main.py
```

Open the app in the browser:

```text
http://127.0.0.1:8000/
```

### Using `pip`

Install dependencies:

```bash
pip install "fastapi[standard]"
```

Then run:

```bash
cd src/fastapi_calculator
python -m fastapi dev main.py
```

## API Usage

### Endpoint

```http
POST /calculate
```

### Request Body

```json
{
  "expression": "(10 + 5) * 2"
}
```

### Example Response

```json
{
  "result": 30.0
}
```

### Error Example

```json
{
  "detail": "Cannot Divide By Zero"
}
```

## Example Expressions

```text
10 + 5
(20 - 8) / 2
3 * (4 + 2)
```

## Notes

The calculator uses Python's `ast` module to parse and evaluate expressions safely for basic arithmetic operations. This makes it a lightweight backend evaluator without needing a full expression engine.

## License

This project is intended for learning and local development.
