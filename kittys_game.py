print("""You are in a cave, and enter a room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a really cute group of K-pop stars standing around.")
    print("What do you do?")
    print("1. Run in and start dancing.")
    print("2. Scream at them.")

    kpop = input("> ")

    if kpop == "1":
        print("They all stare at you, thinking you are a weirdo. Good job!")
    elif kpop == "2":
        print("They all scream with you. Good job!")
    else:
        print("They were not found of that, so they close the door. Good job!")

elif door == "2":
    print("Your great, great, great grandparents are there.")
    print("What do you do?")
    print("1. Tell them who you are and about modern society.")
    print("2. Try to get to know them, how life is for them.")

    grand = input("> ")

    if grand == "1":
        print("They claim you are a witch and burn you alive. Good job!")
    else:
        print("They are very suspicious of who you are, and stab you with a pitchfork. Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")
