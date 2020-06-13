class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}: {self.description}'

    def on_take(self, player, room):
        if room.items.count(self) > 0:
            room.items.remove(self)
            player.items.append(self)
            output = f'\nPlayer Inventory: \n'
            i = 1
            for item in player.items:
                output += f' {i}. {item.name}: {item.description}\n'
                i += 1
            print(output)
            print(f'{player.current_room}')
        else:
            if self.name[-1] == 's':
                print(f'\n{self.name} are not in this room')
            else:
                print(f'\n{self.name} is not in this room')
            output = f'\nAvailable Items: \n'
            i = 1
            for item in room.items:
                output += f' {i}. {item.name}\n'
                i += 1
            print(output)

    def on_drop(self, player, room):
        if player.items.count(self) > 0:
            player.items.remove(self)
            room.items.append(self)
            output = f'\nPlayer Inventory: \n'
            i = 1
            for item in player.items:
                output += f' {i}. {item.name}: {item.description}\n'
                i += 1
            print(output)
            print(f'{player.current_room}')
        else:
            if self.name[-1] == 's':
                print(f'\nPlayer does not have {self.name}')
            else:
                print(f'\nPlayer does not have a {self.name}')
            output = f'\nPlayer Inventory: \n'
            i = 1
            for item in player.items:
                output += f' {i}. {item.name}: {item.description}\n'
                i += 1
            print(output)
        
        