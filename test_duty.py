# what does duty have? Data and behaviour
# a new duty will have a description, Id and unique name
# it will be able to be associated with the automate coin 
# should it have any behaviour? A check for uniqueness?
# 

from duty import Duty, DutyFactory
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

# def test_duty_is_unique():
#     d1 = Duty(name="d1", description="description 1")
#     d2 = Duty(name="d2", description="description 2")
#     assert d1.is_unique(d2) is True

# def test_is_unique_returns_false_if_duties_not_unique():
#     d1 = Duty(name="d1", description="description 1")
#     duplicate_duty = Duty(name="d1", description="description 1")
#     assert d1.is_unique(duplicate_duty) is False

# Rather than have the duty test for uniqueness this could be done by a duty factory class instead, which only creates a class if it is unique and otherwise returns an error

def test_factory_creates_a_an_instance_of_a_duty():
    name = "d1"
    description = "description 1"
    new_duty_factory = DutyFactory()
    d1 = new_duty_factory.create_duty(name, description)

    assert name, description in d1

# def test_factory_ensures_no_duplicate_ids():
#     factory = DutyFactory()
#     d1 = factory.create_duty("d1", "description 1")
#     d2 = factory.create_duty("d2", "description 2")

#     assert d1.id != d2.id
#     assert d1.id == 1
#     assert d2.id == 2

    
