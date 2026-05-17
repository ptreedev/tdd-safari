import pytest

from duty_controller import DutyController
from duty import Duty

class FakeRepository:
            def __init__(self, duties):
                self._duties = duties

            def all(self):
                return self._duties
@pytest.fixture
def duties():
     return [Duty(name='D1', description='desc 1', id=1)]

@pytest.fixture
def controller(duties):
    return DutyController(FakeRepository(duties))

class TestDutyControllerList:

    def test_list_renders_template_with_duties_from_repository(self, duties, controller, mocker):

        mock_render = mocker.patch("duty_controller.render_template")
        mock_render.return_value = "<html>rendered</html>"

        result = controller.list()

        mock_render.assert_called_once_with("duties/list.html", duties=duties)
        assert result == "<html>rendered</html>"
    
    def test_new_form_renders_form_template(self, controller, mocker):

        mock_render = mocker.patch("duty_controller.render_template")
        mock_render.return_value = "<html>form</html>"

        result = controller.new_form()

        mock_render.assert_called_once_with("duties/new_form.html")
        assert result == "<html>form</html>"   

    