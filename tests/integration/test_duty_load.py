import json

from duty import Duty, DutyRepository


class TestLoad:
    def test_empty_state_when_file_missing(self, mocker):
        mocker.patch("duty.Path.exists", return_value=False)
 
        repo = DutyRepository(filepath="anything.json")
 
        assert repo.all() == []

    def test_populated_state_when_file_exists(self, mocker):
        mocker.patch("duty.Path.exists", return_value=True)
        json_content = json.dumps([
            {"id": 1, "name": "Cleaning", "description": "Sweep floors"},
            {"id": 2, "name": "Cooking", "description": "Make food"},
        ])
        mocker.patch("builtins.open", mocker.mock_open(read_data=json_content))

        repo = DutyRepository(filepath="anything.json")

        assert repo.all() == [
            Duty(name="Cleaning", description="Sweep floors", id=1),
            Duty(name="Cooking", description="Make food", id=2),
        ]


