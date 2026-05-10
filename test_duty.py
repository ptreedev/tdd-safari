# what does duty have? Data and behaviour
# a new duty will have a description, Id and unique name
# it will be able to be associated with the automate coin 
# should it have any behaviour? A check for uniqueness?
# 

from duty import Duty
import pytest

@pytest.fixture(autouse=True)
def reset_id_counter(mocker):
    mocker.patch.object(Duty, 'id_counter', 1)

def test_duty_has_a_name_when_initiaslised_with_a_name():
    d1 = Duty(name="d1")
    assert d1.name == "d1"

def test_duty_has_a_description_when_initialised_with_a_description_and_a_name():
    d1 = Duty(name="d1", description="description 1")
    assert d1.description == "description 1"

def test_duty_has_an_id():
    d1 = Duty(name="d1", description="description 1")
    assert d1.id == 1

def test_duty_has_no_duplicate_id():
    d1 = Duty(name="d1", description = "description 1")
    d2 = Duty(name="d2", description="description 2")
    assert d1.id != d2.id

    
