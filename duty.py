class Duty:
    def __init__(self, name, description, duty_id):
        self.name = name
        self.description = description
        self.id = duty_id

class DutyFactory:
    def __init__(self):
        self.id_counter = 1
        self.duty_names = set()
    
    def create_duty(self, name, description):
        if name in self.duty_names:
            raise ValueError("A duty with this name already exists")
        new_duty = Duty(name, description, self.id_counter)

        self.id_counter += 1
        self.duty_names.add(name)
        return new_duty