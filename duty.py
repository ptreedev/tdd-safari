from dataclasses import asdict, dataclass
import json
from pathlib import Path
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
    def __init__(self, filepath):
        self.factory = DutyFactory()
        self.filepath = Path(filepath)
        self._duties = self._load()
        self.description = set()
        self.duty_names = set()

    def _load(self):
        if not self.filepath.exists():
            return []
        with open(self.filepath, "r") as dutyfile:
            return [Duty(**duty) for duty in json.load(dutyfile)]
        
    def _save(self):
        with open(self.filepath, "w") as f:
            json.dump([asdict(duty) for duty in self._duties], f)
       

    def add(self, name, description):
        if name in self.duty_names:
            raise DuplicateNameError("A duty with this name already exists")
        if description in self.description:
            raise DuplicateDescriptionError("A duty with this description already exists")
        
        duty = self.factory.create_duty(name, description)
        # currently state is stored in memory, need a refactor for peristence.
        self.duty_names.add(name)
        self.description.add(description)
        self._duties.append(duty)
        self._save()

        return duty
    
    def all(self):
        return self._duties
    
class DuplicateNameError(Exception):
    pass

class DuplicateDescriptionError(Exception):
    pass