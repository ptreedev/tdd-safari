import pytest
from app import create_app
from duty import DutyRepository


@pytest.fixture(scope="session")
def duties_file(tmp_path_factory):
    return tmp_path_factory.mktemp("data") / "duties.json"


@pytest.fixture(scope="session")
def app(duties_file):
    return create_app(repo=DutyRepository(filepath=duties_file))


@pytest.fixture(autouse=True)
def _reset_duties(duties_file):
    duties_file.write_text("[]")
    yield


@pytest.fixture
def browser_context_args(browser_context_args, live_server):
    return {**browser_context_args, "base_url": live_server.url()}