# QA Home Assignment
## Description
Simple test framework created for a home assignment.
It uses pytest as the base of the framework and pytest-html for creating reports.


## How to configure
Go to the root of the project.

1. Create venv:
```bash
python -m venv .venv
```
2. Activate virtual environment

On windows
```bash
.venv\Scripts\activate.bat
```
On linux
```bash
source .venv/bin/activate
```
3. Install all required libraries.
```bash
pip install -r requirements.txt
```
4. Create .env file and fill it with your user id and app address.
You can copy and rename .env_example file.
```
USER_ID=<provide-user-id>
APP_ADDRESS=https://<qa-app-address>
```
## How to run
You can run the tests in pycharm or with the command:
```bash
pytest
```

To run UI tests use this command:
```bash
pytest -k e2e
```

To run API tests use this command:
```bash
pytest -k api
```

## Additional information
Test reports, logs and screenshots are saved in the reports directory.
Each run creates a separate directory where all relevant artifacts are stored.
