from duty import DuplicateDescriptionError, DuplicateNameError
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

    def test_create_duty_calls_add_method_with_name_and_desc(self, mocker):
        repo = mocker.Mock()
        controller = DutyController(repo)

        mocker.patch("duty_controller.redirect")
        mocker.patch("duty_controller.url_for")

        controller.create_duty(name="D1", description="desc 1")

        repo.add.assert_called_once_with("D1", "desc 1")

    def test_create_duty_redirects_to_list_view(self, mocker):
        repo = mocker.Mock()
        controller = DutyController(repo)

        mock_redirect = mocker.patch("duty_controller.redirect")
        mock_url_for = mocker.patch("duty_controller.url_for")
        mock_url_for.return_value = "/duties"
        mock_redirect.return_value = "<redirect>"

        result = controller.create_duty(name="D1", description="desc 1")
        mock_url_for.assert_called_once_with("duties_list")                                    
        mock_redirect.assert_called_once_with("/duties")                                
        assert result == "<redirect>" 

    def test_create_duty_flashes_and_redirects_to_list_on_duplicate_name(self, mocker):
        repo = mocker.Mock()
        repo.add.side_effect = DuplicateNameError("A duty with this name already exists")
        controller = DutyController(repo)

        mock_flash = mocker.patch("duty_controller.flash")
        mock_redirect = mocker.patch("duty_controller.redirect")
        mock_url_for = mocker.patch("duty_controller.url_for")
        mock_url_for.return_value = "/duties/new_form"
        mock_redirect.return_value = "<redirect-new-form>"

        result = controller.create_duty(name="D1", description="desc 1")

        mock_flash.assert_called_once_with("A duty with this name already exists", "error")
        mock_url_for.assert_called_once_with("duties_list")
        mock_redirect.assert_called_once_with("/duties/new_form")
        assert result == "<redirect-new-form>"

    def test_create_duty_flashes_and_redirects_to_list_on_duplicate_description(self, mocker):
        repo = mocker.Mock()
        repo.add.side_effect = DuplicateDescriptionError("A duty with this description already exists")
        controller = DutyController(repo)

        mock_flash = mocker.patch("duty_controller.flash")
        mock_redirect = mocker.patch("duty_controller.redirect")
        mock_url_for = mocker.patch("duty_controller.url_for")
        mock_url_for.return_value = "/duties/new_form"
        mock_redirect.return_value = "<redirect-new-form>"

        result = controller.create_duty(name="D1", description="desc 1")

        mock_flash.assert_called_once_with("A duty with this description already exists", "error")
        mock_url_for.assert_called_once_with("duties_list")
        mock_redirect.assert_called_once_with("/duties/new_form")
        assert result == "<redirect-new-form>"