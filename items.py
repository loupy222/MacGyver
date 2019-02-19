from labyrinth import my_lab
import pprint

class Items:

    def __init__ (self, name, position):
        self.name = name
        self.position = position

tube = Items("Tube", my_lab.rand_free_tile())
print(tube.position)
"""pprint.pprint(my_lab.structure)"""
syringe = Items("Syringe", my_lab.rand_free_tile())
print(syringe.position)
poison = Items("Poison", my_lab.rand_free_tile())
print(poison.position)