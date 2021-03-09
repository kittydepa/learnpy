### Part 1. Loops that print even numbers from 1-10

## a. For loop

# for i in range(1, 1):
#     if i % 2 == 0:
#         print(i)
#     continue


## b. While loop

# i = 0

# while i  < 10: # This is true
#     i += 2
#     print(i)



# c. Recursive loop
def number(first, last):
    if first % 2 != 1:
        print(f"{first}")
    
    if first == last:
        return
    else:
        number(first + 1, last) # how tf did this work


number(1, 11)

# d. Using 'break'




### Part 2. Loops that print numbers divisible by 3, from 1-30

# # a. For loop
# for i in range(1, 31):
#     if i % 3 == 0:
#         print(i)

# # b. While loop
# i = 0

# while i < 30:
#     i += 3
#     print(i)

# c. Recursive loop


# d. Using break