Practicing TDD skills using python, flask, pytest and playwright.

Covers unit, integration and e2e tests.

To run this locally follow these cli commands:

1. `python -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `python -m playwright install chromium --with-deps`

You will also need a .env file with:
`DUTIES_FILE = <your-file-path-here-to-mount-duties.json>`


To run the tests you can use coverage:

1. `coverage run -m pytest`
and then report test coverage with:
2. `coverage report -m`

To run the app:
1. `flask run`

