# what does duty have? Data and behaviour
# a new duty will have a description, Id and unique name
# it will be able to be associated with the automate coin 
# should it have any behaviour? A check for uniqueness?
# 

from duty import Duty, DutyFactory
import pytest

def test_duty_has_name_description_and_id_when_initialised():
    name = "d1"
    description = "description 1"
    duty_id = 1
    d1 = Duty(name=name, description=description, duty_id=duty_id)
    assert d1.name == name
    assert d1.description == description
    assert d1.id == duty_id

def test_factory_creates_a_an_instance_of_a_duty():
    name = "d1"
    description = "description 1"
    new_duty_factory = DutyFactory()
    d1 = new_duty_factory.create_duty(name, description)

    assert name, description in d1
    assert d1.id == 1

def test_factory_ensures_no_duplicate_ids():
    factory = DutyFactory()
    d1 = factory.create_duty("d1", "description 1")
    d2 = factory.create_duty("d2", "description 2")

    assert d1.id != d2.id
    assert d1.id == 1
    assert d2.id == 2

    
