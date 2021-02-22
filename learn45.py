from sys import exit
#from random import randint
from textwrap import dedent
import typing
from charms import Eval  # Importing a function from another file
import time

class Room:

    def enter(self):
        print("---NA---")
        exit(1)

# Setting up the games mechanisms, e.g. go to next room, start with Characters, etc.
class Game:

    def __init__(self, quest):
        self.quest = quest

    def play(self):
        current_event = self.quest.character_selection()
        #print(f"DEBUG Current Event: {current_event}")
        last_event = self.quest.next_event('finished')

        while current_event != last_event:
            #print(f"DEBUG Current Event: {current_event}")
            next_event_name = current_event.enter()
            current_event = self.quest.next_event(next_event_name)

        current_event.enter()

# The mini-game. ALl characters will end up here regardless.
class MiniGame:

    def enter(self) -> str:
        print(" ")
        print("--------------------------------Game of the Gods--------------------------------")
        time.sleep(2)
        print(dedent("""
              You enter a special room where three tiles lay before you.
              Stepping on one of the tiles will reward you with a powerup.
              However, stepping on the other two will have its consequences.
              Which tile do you choose to step on, tile 1, 2 or 3?"""))

        tile_choice = input("> ")

        if tile_choice == "1":
            time.sleep(1)
            print("That was not the correct tile. You lose half of your health.")
            time.sleep(1)
            return 'death'

        elif tile_choice == "2":
            time.sleep(1)
            print("That was not the correct tile. A giant Oger appears and kills you with a single blow.")
            time.sleep(1)
            return 'death'

        elif tile_choice == "3":
            time.sleep(1)
            print("You got the powerup! You are rewarded with... nothing!")
            time.sleep(1)
            return 'cave'
        
        else:
            raise Exception("You done wrong.")

# First Room - Intro + Pick a character
class Characters(Room):

    def enter(self) -> str:
            print("                                 ")
            print("Welcome to Kitty's Version of Children of Morta, and adventure RPG.")
            print(dedent("""
                  ----------------------------------------------------------------
                  Now it's time to choose a character.

                  Who you choose will determine which quest you will complete,
                  and all characters must make it to the Caves and defeat the Spider King at the end.

                  You can choose one of the following characters:
                  John - the Warrior
                  Linda - the Archer
                  Kevin - the Assassin
                  Mark - the Monk
                  Lucy - the Pyromancer
                  Joey - the Brawler

                  Choose wisely.
                  ----------------------------------------------------------------
                  """))

            selection = input(">The name of the character you choose is: ")

            if selection.lower() == "john" or selection.lower() == "linda":
                print("Good choice. This character is a mighty fighter.")
                time.sleep(1)
                print("You must find and rescue Mary before proceeding to the Caves.")
                return 'mary'

            elif selection.lower() == "mark" or selection.lower() == "lucy":
                print("Good choice. This character dabbles a bit in magic and is very swift.")
                time.sleep(1)
                print("You must help Grandma Margaret find some special herbs before proceeding to the Caves.")
                return 'grandma'

            elif selection.lower() == "kevin" or selection.lower() == "joey":
                print("Good choice. This character is quite skillfull and strong.")
                time.sleep(1)
                print("You must fight through monsters in the cave.")
                return 'fight'

            else:
                print("Sorry, what was that? Try again.")
                return 'character'

# When you die - boo
class Death(Room):

    def enter(self):
        print("Game over.")
        exit(1)

# When you win!
class Finished(Room):

    def enter(self):
        print(" ")
        time.sleep(1)
        print("------------------------------Victory!--------------------------------")
        print("You made it out in one piece!!! Good job.")
        time.sleep(1)
        x = Eval()
        return x

# Everyone needs to go here. Last stop before 'winning; the game'
class Cave(Room):

    def enter(self)  -> str:
            print(" ")
            print("---------------------------Cave of the Spider King---------------------------")
            print(dedent("""
                  You made it to the final level! The Cave. Time to defeat the
                  Spider King. You have two options: either *1* or *2*
                  """))
            
            choice = input("> ")

            if choice == "1":
                time.sleep(1)
                print("Damn, you made it so far but did not make it in the end.")
                print("You died.")
                return 'death'

            elif choice == "2": # something:
                time.sleep(1)
                print("Spider King = defeated!")
                return 'finished'

            else:
                time.sleep(1)
                print("Huh? What's that mean? Try again.")
                return 'cave'


class RescueMary(MiniGame):

    def enter(self) -> str:
        print(" ")
        print("--------------------------------Rescue Mary--------------------------------")
        time.sleep(1)
        print(dedent("""
              You enter a room and see Mary being held down by a mob of ghouls,
              with a little bit of her life draining each minute. You can either
              attack the ghouls *one-by-one*, or attempt to *charge* at them
              to kill them all at once. What do you do?"""))
        action = input("> ")

        if "one" in action.lower().strip() or "attack" in action.lower().strip():
            time.sleep(1)
            print("You fight them, and win. Woohooo!")
            minigame = super(RescueMary, self)
            x = minigame.enter()
            return x

        elif "charge" in action.lower().strip():
            time.sleep(1)
            print("Damn, well that did not go as expected. They clobbered you.")
            return 'death'

        else:
            print("I'm sorry, I don't understand. Try again.")
            time.sleep(1)
            return 'mary'


class HelpGrandma(MiniGame):

    def enter(self) -> str:  # 1. Apply to all other enter functions. 
        print(" ")
        print("--------------------------------Help Grandma--------------------------------")
        time.sleep(1)
        print(dedent("""
              You see the special herb that Grandma Margaret needs for
              healing potions. However, the herb is surronded by hundreds
              of tiny spiders. You have two choices. You can try to use your
              magic to *freeze* the spiders for a split second, or you can try
              to become *invisible* and invulnerable for a few moments to try to
              retreive the herb. Which one do you choose?
              """))

        action = input("> ")

        if "freeze" == action.lower().strip(): # Calling .strip on the result of the lower function  # Chained function call
            time.sleep(1)
            print(dedent("""
                  Well... that didn't go as expected. The spiders did freeze, but
                  not for long enough. You made your way to the herb but just as you
                  were about to turn back, your magic wore off and caught you off guard.
                  The spiders devoured you.
                  """))
            return 'death'

        elif "invisible" in action.lower().strip():
            time.sleep(1)
            print(dedent("""
                  You conjure up enough mana to be able to make yourself invisible.
                  You treaded cautiously as you were not sure how long you could stay
                  in this state. Luckily, you were able to grab the herb and make it
                  back to safety just before you became visible again.
                  You leave without a scratch. Nice work.
                  """))
            minigame = super(HelpGrandma, self)
            x = minigame.enter() # AN UNNAMED VARiABLE WITHOUT THE X or RETURN!
            return x # or return minigame.enter()   it's the same
            # A recursive function.

        else:
            print("What? ... Try again.")
            time.sleep(1)
            return "grandma"
        
       # raise Exception("Function must return as the string.") # 


class PreCave(MiniGame):

    def enter(self) -> str:
        print(" ")
        print("--------------------------------Cave 1--------------------------------")
        time.sleep(1)
        print(dedent("""
              You are in a cave and need to battle your way out. Inside
              the cave where are dozens of demonic archers, all pointing
              arrows at you! You have one of two options. You can either
              use your *heavenly strike* to try to kill them all with a 
              single blow, or you can attempt to *throw a fan of knives*
              at them. Both of these attacks have a chance of killing them
              all in one go, and of course, failing as well. You only get
              one chance. What do you choose?
              """))
        
        choice = input("> ")

        if "knives" == choice.lower().strip():
            time.sleep(1)
            print(dedent("""
                  You rush towards the epicenter of all of the chaos. You
                  jump in the air, surrounded by enemies, and attempt to 
                  throw a fan of knives and... You succeede!
                  """))
            minigame = super(PreCave, self)
            x = minigame.enter()
            return x

        elif "strike" == choice.lower().strip():
            time.sleep(1) 
            print("Omg that was the wrong choice. Very bad. You died.")
            return 'death'

        else:
            print("... the fuck does that mean? Try again")
            time.sleep(1)
            return 'fight'

# Dict with all events, and the code for how to go from 1 room to the next
class Events:

    events = {
        'character': Characters(),
        'mini_game': MiniGame(),
        'mary': RescueMary(),
        'grandma': HelpGrandma(),
        'death': Death(),
        'finished': Finished(),
        'cave': Cave(),
        'fight': PreCave(),
    }

    def __init__(self, start_event):
        self.start_event = start_event

    def next_event(self, event_name):
        val = Events.events.get(event_name)
        return val

    def character_selection(self):
        return self.next_event(self.start_event)



a_character = Events('character')
a_game = Game(a_character)
a_game.play()
