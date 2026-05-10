class Duty:
    id_counter = 1
    def __init__(self, name, description=None):
        self.name = name
        self.description = description
        self.id = Duty.id_counter

        Duty.id_counter += 1
    
    # def is_unique(self, duty):
    #     return True

class DutyFactory:
    def __init__(self):
        pass
    
    def create_duty(self, name, description):
        new_duty = Duty(name, description)
        return new_duty