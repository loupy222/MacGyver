import labyrinth

class Items:

    def __init__ (self, name, position):
        self.name = name
        self.position = position

tube = Items("Tube", labyrinth.my_lab.rand_free_tile())
print(tube.position)
syringe = Items("Syringe", labyrinth.my_lab.rand_free_tile())
print(syringe.position)
poison = Items("Poison", labyrinth.my_lab.rand_free_tile())
print(poison.position)