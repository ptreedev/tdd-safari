
# this has been moved as it's actually an integration test
import pytest

from duty import Duty, DutyRepository

@pytest.fixture
def repo(tmp_path):
    return DutyRepository(filepath=tmp_path / "duties.json")

class TestAllDutyRepository:
    def test_ALL_empty_repo_returns_emptylist(self, repo):
        assert repo.all() == []
    
    def test_ALL_returns_added_duties(self, repo):
        repo.add('D1', "desc1")

        assert repo.all() == [
            Duty(name='D1', description="desc1", id=1)
        ]
    