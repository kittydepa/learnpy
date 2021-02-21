from textwrap import dedent

# First, select a character
class Characters(object):

    def enter(self):
        print(dedent("""
              Now it's time to choose a character.
              The character to you choose will determine which quest you will complete.

              You can choose one of the following characters:
              John - the Warrior
              Linda - the Archer
              Kevin - the Assassin
              Mark - the Monk
              Lucy - the Pyromancer
              Joey the Brawler."""))

        selection = input("> ")

        if "john" or "mary" in selection.lower():
            print("Good choice. Your mission is to find and rescue Mary, the mother of Linda and wife of John.")
            return 'mary'

        elif "mark" or "lucy" in selection.lower():
            print("Good choice. Your mission to help find and deliver some herbs for Grandma.")
            return 'grandma'

        elif "kevin" or "joey" in selection.lower():
            print("Good choice. Your mission is to fight your way throught he dungeon, and defeat the Spider King at the end.")
            return 'fight'
