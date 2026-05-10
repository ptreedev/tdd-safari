
class Duty:
    id_counter = 1
    def __init__(self, name, description=None):
        self.name = name
        self.description = description
        self.id = Duty.id_counter

        Duty.id_counter += 1