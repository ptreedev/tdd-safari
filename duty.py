from dataclasses import dataclass
@dataclass
class Duty:
    name: str
    description: str
    id: int

class DutyFactory:
    def __init__(self):
        self.id_counter = 1
    
    def create_duty(self, name, description):

        new_duty = Duty(name, description, self.id_counter)

        self.id_counter += 1   
        
        return new_duty

#This will handle the state of the duties rather than Factory    
class DutyRepository:
    def __init__(self):
        self.factory = DutyFactory()
        self.description = set()
        self.duty_names = set()

    def add(self, name, description):
        if name in self.duty_names:
            raise DuplicateNameError("A duty with this name already exists")
        if description in self.description:
            raise DuplicateDescriptionError("A duty with this description already exists")
        
        duty = self.factory.create_duty(name, description)
        self.duty_names.add(name)
        self.description.add(description)

        return duty
    
class DuplicateNameError(Exception):
    pass

class DuplicateDescriptionError(Exception):
    pass