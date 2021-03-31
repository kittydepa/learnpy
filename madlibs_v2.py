from textwrap import dedent
import time

# What I want to do: Make the original code less repetitive
story = " "

x = input("Here: ")

story.append(x)


print(story)
# # Let the story start!
# print("---------------------------------------------")
# print("Okay, let's see the story now!")
# time.sleep(1)
# print(" ")
# print(dedent(f"""One {adj1} day, Cristian and Kitty went for a really long walk, all the way to {place1}.
# On the way there, Kitty got hungry. So Cristian asked her if she wanted any of the {noun1} that they brought.
# Kitty eagerly took the {noun1} and started chomping away on it like a {adj2} {animal1}. Cristian felt as
# embarrassed as a {adj3} {animal2}.
#
# After eating, Cristian and Kitty kept walking. On their way to {place1} they saw a wild {noun2}.
# It was sooo tiny! Cristian's eyes got as wide as a {noun3}, and begged Kitty if they could keep it.
# Kitty hesitated at first, but then felt as {emo1} as {celeb} did when they first {verb1}, so she said yes.
# Cristian turned {color1} because he was so filled with joy. Kitty and Cristian {verb2}, and then
# ran all the way to {place1}.
#
# The end."""))
