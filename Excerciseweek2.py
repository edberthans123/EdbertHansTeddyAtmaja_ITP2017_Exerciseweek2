def check_inventory1():
    return len(fruits)
def check_inventory2():
    return len(frozen)
def check_inventory3():
    return len(misc)
def add_item():
    stuff=str(input("stuff"))
    place=str(input("place"))
    if place == "fruits":
        check_inventory1()
        if check_inventory1()>=5:
            print("not enough space")
            print("items in fruits:", fruits)
        else:
            fruits.append(str(stuff))
            print("item", stuff, "has been added")
    elif place == "frozen":
        check_inventory2()
        if check_inventory2()>=5:
            print("not enough space")
            print("items in frozen:", frozen)
        else:
            frozen.append(str(stuff))
            print("item", stuff, "has been added")
    elif place =="misc":
        check_inventory3()
        if check_inventory3()>=5:
            print("not enough space")
            print("items in misc:", misc)
        else:
            misc.append(str(stuff))
            print("item", stuff, "has been added")

fruits=[]
frozen=[]
misc=[]
while True:
    command=input()
    if command=="add":
        add_item()
    elif command=="display":
        print(fruits)
        print(frozen)
        print(misc)
    elif command=="end":
        print("we done boiz")
        break
