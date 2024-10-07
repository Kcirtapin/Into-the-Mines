import components, story
if __name__ == "__main__":
    pcMap = []
    fullMap = story.createRoomList()
    eventList = story.createEventList(fullMap)
    hp = 10
    weapon = story.startingWeapon()
    armor = story.startingArmor()
    inventory = [weapon,armor]
    game = True
    running = True
    crntRoom = fullMap[1]
    crntRoom.enter(pcMap)

    while game is running:
        print("\n")
        decision = input("What will you do?   ")
        print()
        if decision == "h" or decision == "help":
            print("Command List:\nhelp (h): prints command list\nmap (mp): prints list of discovered locations\nmove <#> (mv): move to numbered location\nattack (a): initiates combat with known entities in the room\nsearch (s): Search a location and take loose items.\ninventory (i): Lists items\nuse (u): Use item from inventory")
    
        elif decision == "mp" or decision == "map":
            print("Current Room: "+str(crntRoom.number)+" - "+crntRoom.name)
            print("Other Accessible Rooms:")
            for i in pcMap:
                if i != crntRoom.number:
                    print(str(fullMap[i].number)+" - "+fullMap[i].name)

        elif decision == "mv" or decision == "move":
            dest = int(input("What room will you move to?"))
            if dest in pcMap and dest != crntRoom.number:
                crntRoom = fullMap[dest]
                crntRoom.enter(pcMap)
            elif dest == crntRoom.number:
                print("You're already there")
            else:
                print("That isn't on your map")

        elif decision == "a" or decision == "attack":
            pass

        elif decision == "s" or decision == "search":
            crntRoom.search(input("What do you search?"),inventory)

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

        elif decision == "q" or decision == "quit":
            running = False
            print("Goodbye")
        
        else:
            print("Didn't recognize that command. Please try again")


