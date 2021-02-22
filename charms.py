class Eval:
    def __init__(self) -> None:
        print(" ")
        print("-----------------------------Exit Survey------------------------------")
        print("On a scale of one to ten, how satisfied are you with the game experience?")
        rating = input("> ")
        
        if rating == "1" or rating == "2":
             print("Why do you hate me...")
        
        elif rating == "9" or rating == "10":
            print("Awesome! Okay, bye")
        
        else:
            print("Hmm... not sure how to interpret. Ok, bye.")