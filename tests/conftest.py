import os
from datetime import datetime
from pathlib import Path

import pytest
from dotenv import load_dotenv

from communication.rest.api_client import ApiClient
from consts import ROOT, REPORTS_DIR, TIMESTAMP_FORMAT
from utils.logger import configure_logger

load_dotenv(ROOT / ".env")


def pytest_configure(config):
    timestamp = datetime.now().strftime(TIMESTAMP_FORMAT)
    report_dir = REPORTS_DIR / str(timestamp)
    report_dir.mkdir(exist_ok=True)

    config.option.htmlpath = str(
        report_dir / f"{timestamp}.html"
    )
    configure_logger(report_dir)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    if report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            report_file = Path(item.config.option.htmlpath)
            screenshots_dir = report_file.parent / "screenshots"
            screenshots_dir.mkdir(exist_ok=True)

            screenshot_path = (
                screenshots_dir / f"{item.name}.png"
            )

            driver.save_screenshot(str(screenshot_path))


@pytest.fixture(scope="session")
def user_id() -> str:
    return os.getenv("USER_ID")


@pytest.fixture(scope="session")
def app_address() -> str:
    address = os.getenv("APP_ADDRESS")
    if address.endswith("/"):
        address = address[:-1]

    return address


@pytest.fixture(scope="session")
def authorized_app_address(app_address, user_id) -> str:
    return f"{app_address}/?user-id={user_id}"


@pytest.fixture
def api_client(app_address, user_id) -> ApiClient:
    client = ApiClient(app_address, user_id)
    return client


@pytest.fixture(autouse=True)
def reset_balance_to_default(api_client: ApiClient):
    api_client.reset_balance()
