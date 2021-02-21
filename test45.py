#import characters from  (character file)

from sys import exit
from random import randint
from textwrap import dedent
#from file_name_raw import function_name
# https://stackoverflow.com/questions/20309456/call-a-function-from-another-file


class Room(object):

    def enter(self):
        print("---NA---")
        exit(1)
rwetewfhsdkjhfdkslhfj 

# Setting up the games mechanisms, e.g. go to next room, start with Characters, etc.
class Game(object):

    def __init__(self, quest):
        self.quest = quest

    def play(self):
        current_event = self.quest.character_selection()
        last_event = self.quest.next_event('finished')

        while current_event != last_event:
            next_event_name = current_event.enter()
            current_event = self.quest.next_event(next_event_name)

        current_event.enter()

# First Room - Intro + Pick a character
class Characters(Room):
    def enter(self):
            print("                                 ")
            print("Welcome to Kitty's Version of Children of Morta, and adventure RPG.")
            print(dedent("""
                  ----------------------------------------------------------------
                  Now it's time to choose a character.

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
                print(" ----------------------------------------------------------------")
                return 'mary'

            elif selection.lower() == "mark" or selection.lower() == "lucy":
                print("Good choice. This character dabbles a bit in magic and is very swift.")
                print(" ----------------------------------------------------------------")
                return 'mary'

            elif selection.lower() == "kevin" or selection.lower() == "joey":
                print("Good choice. This character is quite skillfull and strong.")
                print(" ----------------------------------------------------------------")
                return 'mary'

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
        print("You made it out in one piece!!! Good job.")
        exit(1)


class MiniGame(object):

    def enter(self):
        print(dedent("""
              You enter a special room where three tiles lay before you.
              Stepping on one of the tiles will reward you with a powerup.
              However, stepping on the other two will have its consequences.
              Which tile do you choose to step on, tile 1, 2 or 3?"""))

        tile_choice = input("> ")

        if tile_choice == "1":
            print("That was not the correct tile. You lose half of your health.")
            return 'death'
        elif tile_choice == "2":
            print("That was not the correct tile. A giant Oger appears and kills you with a single blow.")
            return 'death'
        elif tile_choice == "3":
            print("You got the powerup! You are rewarded with... nothing!")
            return 'cave'


class RescueMary(MiniGame):

    def enter(self):
        print("Mary time")
        print(dedent("""
              You enter into the Silk Caves. There are monsters all around you.
              You have several options """))

        action = input("> ")

        if "1" in action:
            print("You fight them, and win. Woohooo!")
            super(RescueMary, self).enter()

        else:
            print("Damn, they clobbered you.")
            return 'death'


# Dict with all events, and the code for how to go from 1 room to the next
class Events(object):

    events = {
    'character': Characters(),
    'mini_game': MiniGame(),
    'mary': RescueMary(),
    'death': Death(),
    'finished': Finished(), # AKA Anai-Dya's Dominion
    }

    def __init__(self, start_event):
        self.start_event = start_event

    def next_event(start, event_name):
        val = Events.events.get(event_name)
        return val

    def character_selection(self):
        return self.next_event(self.start_event)



a_character = Events('character')
a_game = Game(a_character)
a_game.play()
