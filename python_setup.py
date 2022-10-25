

def hello():
    print("Hello User")

def pack(item_1, item_2, item_3):
    return [item_1, item_2, item_3]

def eat_lunch(Lunch_items):
    if len(Lunch_items) == 0:
        print("Ain't got no lunch!")
    else:
        for i in range(len(Lunch_items)):
            if i == 0:
                print(f"First I eat {Lunch_items[i]}")
            else:
                print(f"Next I eat {Lunch_items[i]}")


hello()
print(pack("a", "b", "c"))
eat_lunch([])
eat_lunch(["pork chop"])
eat_lunch(["pork chop", "chicken", "beef surprise", "sprite"])

