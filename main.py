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

class Event(object):
    #room{int} - The room in which the event occurs
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

    def activate(self):
        if not self.activated:
            global inventory
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
    def search(self, item):
        global inventory
        for obj in self.objects:
            if item == obj.name:
                inventory.append(obj)
                print(obj.oT)
                return True
        print("You can't search that")
        return False


if __name__ == "__main__":
    pcMap = [0]
    fullMap = []
    eventList = []
    hp = 10
    weapon = Item("Pickaxe",[],"An iron pick. Chips and rust mark it well aged. Equipable as a weapon.","")
    armor = Item("Miner Outfit",[],"A ragged, stained shirt, tucked into thick, yet torn, trousers. Comes with a helmet. Equipable as armor.","")
    inventory = [weapon,armor]
    game = True
    running = True
    crntRoom = fullMap[0]

    while game is running:
        decision = input("What will you do?   ")
    
        if decision == "h" or decision == "help":
            print("Command List:\nhelp (h): prints command list\nmap (mp): prints list of discovered locations\nmove <#> (mv): move to numbered location\nattack (a): initiates combat with known entities in the room\nsearch (s): Search a location and take loose items.\ninventory (i): Lists items\nuse (u): Use item from inventory")
    
        elif decision == "mp" or decision == "map":
            print("Current Room: "+str(crntRoom.number)+" - "+crntRoom.name)
            print("Other Explored Rooms:")
            for i in pcMap:
                print(str(crntRoom.number)+" - "+crntRoom.name)

        elif decision == "mv" or decision == "move":
            dest = int(input("What room will you move to?"))
            if dest in pcMap and dest != crntRoom.number:
                crntRoom = fullMap[dest]
                print(crntRoom.des)
            else:
                print("That isn't on your map")

        elif decision == "a" or decision == "attack":
            pass

        elif decision == "s" or decision == "search":
            crntRoom.search(input("What do you search?"))

        elif decision == "i" or decision == "inventory":
            print("Current Weapon: "+weapon.name+" - "+weapon.des)
            print("Current Armor: "+armor.name+" - "+armor.des)
            print("Backpack: ")
            if len(inventory) > 2:
                for item in inventory:
                    if item != weapon and item != armor:
                        print(item.name+" - "+item.des)
            else:
                print("Empty")

        elif decision == "u" or decision == "use":
            item = input("What item would you like to use?")
            pItem = None
            for i in inventory:
                if i.name == item:
                    pItem = i
            if pItem == None:
                print("Couldn't find that item")
            elif not(crntRoom.number in pItem.rooms):
                print("Can't use that here")
            else:
                pass


