import random 


# Room class with dirtiness level and methods to clean and get dirtiness
class Room:
    def __init__(self, index:int, dirtiness:int=0):
        self.index = index
        self.dirtiness = dirtiness # 0=> clean, 1-5=> dirtiness level

    def is_dirty(self)->bool:
        return self.dirtiness > 0
    
    def get_dirtiness(self)->int:
        return self.dirtiness
    
    def clean(self):
        self.dirtiness = 0

    def maybe_get_dirty(self, probability:float=0.1):
        if self.dirtiness == 0 and random.random() < probability:
            self.dirtiness = random.randint(1, 5)

class Environment:
    def __init__(self, n_rooms:int, dirtiness_probability:float=0.5):
        self.rooms = []
        for i in range(n_rooms):
            if random.random() < dirtiness_probability:
                dirtiness = random.randint(1, 5)
            else:
                dirtiness = 0
            self.rooms.append(Room(i, dirtiness))
    
    def all_rooms_clean(self)->bool:
        return all(not r.is_dirty() for r in self.rooms)
    
    def step_dirt_reappearance(self):
        for r in self.rooms:
            r.maybe_get_dirty(probability=0.1)