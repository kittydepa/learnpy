from textwrap import dedent
import time

print("---------------------------------------------")
print(" ")
print("We are going to play MadLibs!")
time.sleep(1)
print(" ")
time.sleep(1)
print("The prompt will ask you to type in a specific word, (like an noun, a verb, etc.)")
time.sleep(1)
print("The only rule is: please just right ONE word per prompt, unless otherwise specified.")
time.sleep(1)
print(" ")
print("Let's go!")
time.sleep(1)
print(" ")
print("---------------------------------------------")
print(" ")

print("Give me an adjective: ")
adj1 = input("> ")
time.sleep(1)

print("Give me a place: ")
place1 = input("> ")
time.sleep(1)

print("Give me a noun: ")
noun1 = input("> ")
time.sleep(1)

print("Give me an adjective: ")
adj2 = input("> ")
time.sleep(1)

print("Give me an animal: ")
animal1 = input("> ")
time.sleep(1)

print("Give me an adjective: ")
adj3 = input("> ")
time.sleep(1)

print("Give me an animal: ")
animal2 = input("> ")
time.sleep(1)

print("Give me a noun: ")
noun2 = input("> ")
time.sleep(1)

print("Give me another noun: ")
noun3 = input("> ")
time.sleep(1)

print("Give me an emotion: ")
emo1 = input("> ")
time.sleep(1)

print("Give me the name of a celebrity: ")
celeb = input("> ")
time.sleep(1)

print("Give me the PAST TENSE of a verb: ")
verb1 = input("> ")
time.sleep(1)

print("Give me a color: ")
color1 = input("> ")
time.sleep(1)

print("Give me another PAST TENSE verb: ")
verb2 = input("> ")
time.sleep(1)


# Let the story start!
print("---------------------------------------------")
print("Okay, let's see the story now!")
time.sleep(1)
print(" ")
print(dedent(f"""One {adj1} day, Cristian and Kitty went for a really long walk, all the way to {place1}.
On the way there, Kitty got hungry. So Cristian asked her if she wanted any of the {noun1} that they brought.
Kitty eagerly took the {noun1} and started chomping away on it like a {adj2} {animal1}. Cristian felt as
embarrassed as a {adj3} {animal2}.

After eating, Cristian and Kitty kept walking. On their way to {place1} they saw a wild {noun2}.
It was sooo tiny! Cristian's eyes got as wide as a {noun3}, and begged Kitty if they could keep it.
Kitty hesitated at first, but then felt as {emo1} as {celeb} did when they first {verb1}, so she said yes.
Cristian turned {color1} because he was so filled with joy. Kitty and Cristian {verb2}, and then
ran all the way to {place1}.

The end."""))
