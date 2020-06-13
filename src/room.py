# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def __str__(self):
        output =  f'\nYou are in the {self.name}.\n\n{self.description}\nAvailable Items:'
        i = 1
        for item in self.items:
            output += f'\n {i}. {item.name}'
            i += 1
        return output + f'\n'
