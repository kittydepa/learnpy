def cheese_and_crackers(cheese_count, boxes_of_crackers): #the name of the function, and the args
    print(f"You have {cheese_count} cheeses!") #curly braces = user input
    print(f"You have {boxes_of_crackers} boxes of crackers!") #prints le user input on box #
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:") #1st thing the user sees
cheese_and_crackers(20, 30) #user does not see this per say, but this is calling the function,
#aka, for the above to be read.

print("OR, we can use variables from our script:")
amount_of_cheese = 10 #where does the amount of come from? hmm, python inbuilt function?
amount_of_crackers = 50 # OHH these are VARIABLES we are creating! duh!
 # then, see next like! Those variables become the functions args
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)  # 10 + 20 = cheese amount, the other is crackerz


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
