class Item(object):
    #name{str} - The name of the item
    #rooms{dict[int,int]} - A dictionary of events mapped to rooms
    #des{str} - The description given upon inspection
    #obtainText{str} - The description given upon getting the item
    def __init__(self, name, rooms, des, obtainText):
        self.name = name
        self.rooms = rooms
        self.des = des
        self.oT = obtainText
        self.equipable = 0

class Weapon(Item):
    def __init__(self, name, rooms, des, obtainText, equipable, damage):
        super(self, name, rooms, des, obtainText)
        self.equipable = 1
        self.damage = damage


class Armor(Item):
    def __init__(self, name, rooms, des, obtainText, defense):
        super(self, name, rooms, des, obtainText)
        self.equipable = 2
        self.defense = defense

class Event(object):
    #room{Room} - The room in which the event occurs
    #des{str} - The description of what happens when the event is triggered
    #destAdd{int[]} - A list of new locations to add to the room
    #newDes{str} - The appended description to the room
    #items{Item[]} - A list of items obtained in the event
    def __init__(self,room,des,destAdd,newDes,items,subEvents):
        self.room = room
        self.des = des
        self.destAdd = destAdd
        self.newDes = newDes
        self.items = items
        self.subE = subEvents
        self.activated = False

    def activate(self, inventory):
        if not self.activated:
            self.room.des+=self.newDes
            for r in self.destAdd:
                self.room.adjRooms.append(r)
            for i in self.items:
                inventory.append(i)
            print(self.des)
            for e in self.subE:
                e.activate()
            self.activate = True
        


class Room(object):
    #number{int} - The room's id number
    #objects{Item[]} - The list of items in the room
    #des{str} - The description given upon entering the room
    #adjRooms{int[]} - List of room id numbers that are adjacent to this room
    def __init__(self, number, objects, des, adjRooms):
        self.number = number
        self.objects = objects
        self.des = des

    #item{str} - The item the pc is searching/searching for
    def search(self, item, inventory):
        for obj in self.objects:
            if item == obj.name:
                inventory.append(obj)
                print(obj.oT)
                return True
        print("You can't search that")
        return False