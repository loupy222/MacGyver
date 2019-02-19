from labyrinth import my_lab
import pprint

class Items:

    def __init__ (self, name, position):
        self.name = name
        self.position = position
        self.structure = my_lab.structure
        self.structure[position[0]] [position[1]] = name[0]

tube = Items("Tube", my_lab.rand_free_tile())
syringe = Items("Syringe", my_lab.rand_free_tile())
poison = Items("Poison", my_lab.rand_free_tile())
#pprint.pprint(my_lab.structure)