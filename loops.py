### Part 1. Loops that print even numbers from 1-10

### a. For loop
# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i)
#     continue


## b. While loop
# i = 0

# while i  < 10: # This is true
#     i += 2
#     print(i)



# # c. Recursive loop
# def number(first, last):
#     if first % 2 != 1:
#         print(f"{first}")
    
#     if first == last:
#         return
#     else:
#         number(first + 1, last) # how tf did this work


# number(1, 11)



# # d. Using 'break' AND continue, for no. 1-10 divisible by 2
# for i in range (1, 101):
#     # Skip number 4 though
#     if i == 4:
#         continue
#     if i % 2 == 0:
#         print(i)
#     if i == 10:
#         break




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



# # c. Recursive loop
# def number(first, last):
#     if first % 3 == 0:
#         print(f"{first}")
    
#     if first == last:
#         return
#     else:
#         number(first + 1, last)

# print("== number ==")
# number(3, 30) # No idea how this works yet...


# def number2(first, last):
#     print(f"{first}")
#     if first == last:
#         return
#     else:
#         number(first + 3, last)

# print("== number2 ==")
# number2(3, 30)



# # d. Using break and continue, for no. 1-30, divisible by 3
# for i in range(1, 101):
#     # Skip no. 6 though
#     if i == 6:
#         continue
#     if i % 3 == 0:
#         print(i)
#     if i == 30:
#         break
