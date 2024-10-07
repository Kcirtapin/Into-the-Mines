import components

def createRoomList():
    outList = [None]

    itemList = [components.Item("Key",{2:1},"A rusty bronze key for the mine.", "You pick up the bronze key on the table and put it in your pocket")]
    description = "An abandoned barracks in front of a mine. Inside are a row of bunk beds, with a table in the corner. The table is littered with cards and such, as well as a key for the mine."
    crntRoom = components.Room(1,"Barracks",itemList,description, [2])
    outList.append(crntRoom)
    
    itemList = []
    description = "The entryway to the mine. It's only jagged hole carved into the rock, a stark contrast to the solid iron door blocking your path. The door has a lock across it"
    crntRoom = components.Room(2,"Entrance",itemList,description,[1])
    outList.append(crntRoom)

    return outList

def createEventList(mapList: list):
    outList = [None]

    description = "The key grinds against the inside of the lock, but both hold up and the lock opens. The door swings open, admitting you into the mine"
    roomDesChange = ", but you have since disengaged the lock"
    crntEvent = components.Event(mapList[2],description,[3], roomDesChange,[])
    outList.append(crntEvent)

    return outList

def startingWeapon():
    return components.Weapon("Pickaxe",[],"An iron pick. Chips and rust mark it well aged. Equipable as a weapon.","",1)

def startingArmor():
    return components.Armor("Miner Outfit",[],"A ragged, stained shirt, tucked into thick, yet torn, trousers. Comes with a helmet. Equipable as armor.","",1)