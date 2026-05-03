# what does duty have? Data and behaviour
# a new duty will have a description, Id and unique name
# it will be able to be associated with the automate coin 
# should it have any behaviour? A check for uniqueness?
# 

from duty import Duty

def test_duty_has_a_name_when_initiaslised_with_a_name():
    d1 = Duty(name="d1")
    assert d1.name == "d1"
    
