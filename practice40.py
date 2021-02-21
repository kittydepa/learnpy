# Now pass the lyrics as a separate variable, and pass that variable to the class to use instead
class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

tainted_love = ["Sometimes I feel I've got to",
                    "Run away",
                    "I've got to, get away",
                    "Don't really want anymore from me to make things right"]

this_is_the_new = ["Are you motherf*ckers ready",
                        "For the new $@#%",
                        "Stand up and admit"]

print("{Tained Love}")
tainted_love_song = Song(tainted_love) # Need to make it as a new variable! Then tell it to load the list of lyrics
tainted_love_song.sing_me_a_song() # Then do the func

print(" ")

print("{This Is the New...}")
this_is_song = Song(this_is_the_new)
this_is_song.sing_me_a_song()




# Tthe original
""" class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

tainted_love = Song(["Sometimes I feel I've got to",
                    "Run away",
                    "I've got to, get away",
                    "Don't really want anymore from me to make things right"])

this_is_the_new = Song(["Are you motherf*ckers ready",
                        "For the new $@#%",
                        "Stand up and admit"])

print("{Tained Love}")
tainted_love.sing_me_a_song()

print(" ")

print("{This Is the New...}")
this_is_the_new.sing_me_a_song()
"""
