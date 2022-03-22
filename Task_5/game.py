"""Task 5"""
class Room:
    """The main class that describe rooms
    >>> kitchen = Room("Kitchen")
    >>> kitchen.set_description("A dank and dirty room buzzing with flies.")
    >>> kitchen.description
    'A dank and dirty room buzzing with flies.'
    """    
    def __init__(self, name, link_rooms = [], characters = [], items = []):
        self.name = name
        self.link_rooms = []
        self.characters = []
        self.items = []

    def set_description(self, description):
        self.description = description

    def link_room(self, other, direction):
        self.link_rooms.append((other, direction))

    def set_character(self, character):
        self.characters.append(character)

    def set_item(self, item):
        if item != None:
            self.items.append(item)
        else:
            del self.items[0]
        
    def get_details(self):
        print(self.name)
        print(self.description)
        for i in self.link_rooms:
            print(i[0].name, "is", i[1])
        for i in self.characters:
            print(i.name, "is here")
            print(i.description)
        for i in self.items:
            print(i.name, "is here -- ", i.description)            
        return f"link rooms - {self.link_rooms}, items - {self.items}, characters - {self.characters}"

    def get_character(self):
        if len(self.characters) > 0:
            return self.characters[0]
        return None

    def get_item(self):
        if len(self.items) > 0:
            return self.items
        return None
    
    def move(self, direction):
        for i in self.link_rooms:
            if i[1] == direction:
                res = i[0]
                break
        return res


class Character:
    """
    Mother class that describe main character, enemies and allies
    Consists with common functions for enemies and allies
    """    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.message = ""
        self.defeat = 0

    def describe(self):
        return print(self.description)
    
    def talk(self):
        print(self.message)


class Enemy(Character):
    """
    Class-heir of Character
    >>> dave = Enemy("Dave", "A smelly zombie")
    >>> dave.set_weakness("cheese")
    >>> dave.weak
    'cheese'
    """
    
    def set_conversation(self, message):
        self.message = message
    
    def set_weakness(self, weak):
        self.weak = weak

    def fight(self, item):        
        return True if item == self.weak else False

    def get_defeated(self):
        self.defeat += 1
        return self.defeat

class Ally(Character):
    """
    Class-heir of Character
    useless class in game
    >>> ch1 = Ally("Devid", "Friend with cheese")
    >>> ch1.name
    'Devid'
    """    
    restore_health = 1
    def help(self):
        print("You get 1 point of health from ally")        
        self.restore_health = 0
    
    def give_item(self, name):
        for i in self.items:
            if i.name == name:
                print("Okay, I will give it for you")
                return i
        print("I don't have this, sorry")

class Item:
    """
    Class for things in game
    >>> book = Item("book")
    >>> book.name
    'book'
    """
    def __init__(self, name):
        self.name = name

    def set_description(self, description):
        self.description = description
        
    def get_name(self):
        return self.name
    
    def describe(self):
        return print(self.description)

# import doctest
# doctest.testmod()