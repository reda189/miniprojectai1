import random
from environment import Room


class Agent:
    def __init__(self, env, location, energy, n_rooms):
        self.env = env
        self.location = location
        self.energy = int(2.5*n_rooms)
        self.path = [] #path of cleaned  rooms

    def perceive(self, environment):
        room = environment.get_room(self.location)
        if room.dirtiness == 'Dirty':
            return self.suck_dirt(room)
        elif room.dirtiness == 'Clean':
            return self.move_right()
        else:
            return self.move_left()

    def move_right(self):
        if self.location < len(self.env.rooms) - 1 and self.energy > 2:
            self.location += 1 
            self.energy -= 2
            return self.location

    def move_left(self):
        if self.location > 0 and self.energy > 2:
            self.location -= 1 
            self.energy -= 2
            return self.location

    def suck_dirt(self, room):
        if self.energy >= room.dirtiness_level:
            room.dirtiness = 'Clean'
            self.energy -= room.dirtiness_level
            self.path.append(room) 
            return f"The room number {self.location} is clean"
