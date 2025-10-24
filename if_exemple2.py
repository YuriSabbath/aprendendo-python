name = input("Enter your name: ")

if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name}")

online = True

if online:
    print("The user is online")
else:
    print("The user is offline")