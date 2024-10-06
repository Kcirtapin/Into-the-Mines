import components
if __name__ == "__main__":
    pcMap = [0]
    fullMap = []
    eventList = []
    hp = 10
    weapon = components.Item("Pickaxe",[],"An iron pick. Chips and rust mark it well aged. Equipable as a weapon.","")
    armor = components.Item("Miner Outfit",[],"A ragged, stained shirt, tucked into thick, yet torn, trousers. Comes with a helmet. Equipable as armor.","")
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
        
        elif decision == "e" or decision == "equip":
            item = input("What item would you like to use?")
            pItem = None
            for i in inventory:
                if i.name == item:
                    pItem = i
            if pItem == None:
                print("Couldn't find that item")
            elif pItem.equipable == 0:
                print("You can't equip this item")
            else:
                if pItem.equipable == 1:
                    weapon = pItem
                    print("Your weapon is now a "+pItem.name)
                else:
                    armor = pItem
                    print("You are now wearing the "+pItem.name+" as armor")

        else:
            print("Didn't recognize that command. Please try again")


