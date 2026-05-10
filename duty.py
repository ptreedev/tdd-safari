class Duty:
    def __init__(self, name, description, duty_id):
        self.name = name
        self.description = description
        self.id = duty_id

class DutyFactory:
    def __init__(self):
        self.id_counter = 1
    
    def create_duty(self, name, description):
        new_duty = Duty(name, description, self.id_counter)
        return new_duty