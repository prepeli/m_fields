# m_fields Readme file
This project is a basic test automation scenario for digital m_fields form.

## Technologies

We're using Playwright, a cross-browser end-to-end testing library, with pytest, a framework for writing and running Python tests.

## Setup

To set up the project, you need to have Python and pytest installed on your system.

To install Playwright within your project:

```bash
pip install pytest-playwright
```

Install the required browsers:
```bash
python -m playwright install
```

Next, you need to rename `secrets_example.py` to `secrets.py` and insert your credentials for logging into m_fields.

## Running the test
To run the test file, you can use the following command:

`pytest test_all.py`

This will launch a browser instance and execute the test cases defined in `test_all.py`.

### Running the test in debug mode
To run your playwright python pytest file in debug mode, you need to set the PWDEBUG environment variable to 1 and use the -s option for pytest. For example, you can run the following command in your terminal:

`PWDEBUG=1 pytest -s test_all.py`