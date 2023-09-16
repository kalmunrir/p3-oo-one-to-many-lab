class Pet:
    
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner = None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def pet_type(self):
        return self._pet_type
    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type in self.PET_TYPES:
            self._pet_type = pet_type
        else:
            raise Exception("The pet must be of a recognized type")
        
    @property
    def owner(self):
        return self._owner
    @owner.setter
    def owner(self, owner):
        if isinstance(owner, Owner) and owner:
            self._owner = owner

class Owner:
    
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    def pets(self):
        return ([pet for pet in Pet.all if pet.owner == self])
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception("Pet must be of type Pet")
    def get_sorted_pets(self):
        return sorted(self.pets(), key = lambda pet: pet.name.lower())