import labyrinth
import pprint

class Items:

    def __init__ (self, name, position):
        self.name = name
        self.position = position
        self.structure = labyrinth.my_lab.structure
        self.structure[position[0]] [position[1]] = name[0]

tube = Items("Tube", labyrinth.my_lab.rand_free_tile())
syringe = Items("Syringe", labyrinth.my_lab.rand_free_tile())
poison = Items("Poison", labyrinth.my_lab.rand_free_tile())
