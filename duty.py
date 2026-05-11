class Duty:
    def __init__(self, name, description, duty_id):
        self.name = name
        self.description = description
        self.id = duty_id

class DutyFactory:
    def __init__(self):
        self.id_counter = 1
        self.duty_names = set()
        self.description = set()
    
    def create_duty(self, name, description):
        if name in self.duty_names:
            raise DuplicateNameError("A duty with this name already exists")
        if description in self.description:
            raise DuplicateDescriptionError("A duty with this description already exists")
        new_duty = Duty(name, description, self.id_counter)

        self.id_counter += 1
        self.duty_names.add(name)
        self.description.add(description)
        
        return new_duty
    
class DuplicateNameError(Exception):
    pass

class DuplicateDescriptionError(Exception):
    pass