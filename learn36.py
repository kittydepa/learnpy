from sys import exit

def second_try():
    print("You can spend in whatever you'd like. Woo! Lucky you!")
    exit(0)

def spend():
    print("Ha! You can only spend the money on one of two things:")
    print(" food, or healthcare.")
    print("What do you choose?")

    choice = input("> ")
    if "food" in choice:
        dead("I hope you are hungry!")
    elif "healthcare" in choice:
        print("Okay. You much be American. I'm sorry.")
        dead("Take care buddy.")
    else:
        print("I'm sorry, I don't understand. Try again.")

def donate():
    print("Wow! That is generous of you.")
    print("You now only have two options")
    print("You can either donate to a cause for sick kids, or a celebrity of your choice.")
    print("What do you choose?")

    choice = input("> ")

    if "celebrity" in choice:
        dead("Well, that was a waste.")
    elif "kids" in choice:
        print("Wow! You are really kind.")
        print("As a reward, you get another 1 million dollars!")
        second_try()
    else:
        print("I'm sorry. What do you mean? Try again.")


def dead(why):
    print(why, "Game over. Goodbye!")
    exit(0)

def start():
    print("You enter a room and are suddently given 1 million dollars.")
    print("You can either donate or spend it.")
    print("What do you do?")

    choice = input("> ")
    if "donate" in choice:
        donate()
    elif "spend" in choice:
        spend()
    else:
        print("I'm sorry, I don't know what you mean. Try again.")


start()
