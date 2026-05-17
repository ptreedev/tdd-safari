from dataclasses import asdict, dataclass
import json
from pathlib import Path
@dataclass
class Duty:
    name: str
    description: str
    id: int

class DutyFactory:
    def __init__(self, start_id=1):
        self.id_counter = start_id
    
    def create_duty(self, name, description):

        new_duty = Duty(name, description, self.id_counter)

        self.id_counter += 1   
        
        return new_duty

#This will handle the state of the duties rather than Factory    
class DutyRepository:
    def __init__(self, filepath):
        self.filepath = Path(filepath)
        self._duties = self._load()
        next_id = max((d.id for d in self._duties), default=0) + 1
        self.factory = DutyFactory(start_id=next_id)

    def _load(self):
        if not self.filepath.exists():
            return []
        with open(self.filepath, "r") as dutyfile:
            return [Duty(**duty) for duty in json.load(dutyfile)]
        
    def _save(self):
        with open(self.filepath, "w") as f:
            json.dump([asdict(duty) for duty in self._duties], f)
       
    def _check_unique(self, name, description):

        if any(duty.name == name for duty in self._duties):
            raise DuplicateNameError("A duty with this name already exists")
        if any(duty.description == description for duty in self._duties):
            raise DuplicateDescriptionError("A duty with this description already exists")

    def add(self, name, description):
        self._check_unique(name, description)
        
        duty = self.factory.create_duty(name, description)

        self._duties.append(duty)
        self._save()

        return duty
    
    def all(self):
        return self._duties
    
class DuplicateNameError(Exception):
    pass

class DuplicateDescriptionError(Exception):
    pass