class Item(object):
    #name{str} - The name of the item
    #rooms{dict[int,int]} - A dictionary of events mapped to rooms
    #des{str} - The description given upon inspection
    #obtainText{str} - The description given upon getting the item
    def __init__(self, name: str, rooms: dict, des: str, obtainText: str):
        self.name = name
        self.rooms = rooms
        self.des = des
        self.oT = obtainText
        self.equipable = 0

class Weapon(Item):
    def __init__(self, name: str, rooms: dict, des: str, obtainText: str, damage: int):
        super().__init__(name, rooms, des, obtainText)
        self.equipable = 1
        self.damage = damage


class Armor(Item):
    def __init__(self, name: str, rooms: dict, des: str, obtainText: str, defense: int):
        super().__init__(name, rooms, des, obtainText)
        self.equipable = 2
        self.defense = defense

class Room(object):
    #number{int} - The room's id number
    #name{str} - The room's displayed name
    #objects{Item[]} - The list of items in the room
    #des{str} - The description given upon entering the room
    #adjRooms{int[]} - List of room id numbers that are adjacent to this room
    def __init__(self, number: int, name: str, objects: list, des: str, adjRooms: list):
        self.number = number
        self.name = name
        self.objects = objects
        self.des = des
        self.adjRooms = adjRooms

    #item{str} - The item the pc is searching/searching for
    #inventory{Item[]} - The player's current inventory
    def search(self, item: str, inventory: list):
        for obj in self.objects:
            if item == obj.name:
                inventory.append(obj)
                print(obj.oT)
                return True
        print("You can't search that")
        return False

    def enter(self, pcMap: list):
        print(self.des)
        for r in self.adjRooms:
            pcMap.append(r)

class Event(object):
    #room{Room} - The room in which the event occurs
    #des{str} - The description of what happens when the event is triggered
    #destAdd{int[]} - A list of new locations to add to the room
    #newDes{str} - The appended description to the room
    #items{Item[]} - A list of items obtained in the event
    #subEvents{Event[]} - A list of events triggered by this event. Used to affect other rooms
    def __init__(self,room: Room,des: str,destAdd: list,newDes: str,items: list,subEvents: list =[]):
        self.room = room
        self.des = des
        self.destAdd = destAdd
        self.newDes = newDes
        self.items = items
        self.subE = subEvents
        self.activated = False

    #inventory{Item[]} - The player's current inventory
    def activate(self, inventory: list):
        if not self.activated:
            self.room.des+=self.newDes
            for r in self.destAdd:
                if r > 0:
                    self.room.adjRooms.append(r)
                else:
                    try:
                        self.room.adjRooms.remove(r)
                    except:
                        pass
            for i in self.items:
                inventory.append(i)
            print(self.des)
            for e in self.subE:
                e.activate()
            self.activate = True
        