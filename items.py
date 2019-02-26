from labyrinth import Labyrinth
import pprint

lab = Labyrinth()

class Items:

    def __init__ (self, name, position):
        self.name = name
        self.position = position
        self.structure = lab.structure
        self.structure[position[0]] [position[1]] = name[0]

