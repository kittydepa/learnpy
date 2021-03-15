# Given a list of integers, use a vector and return the mean (the average value), 
# median (when sorted, the value in the middle position), and mode 
# (the value that occurs most often; a hash map will be helpful here) of the list.


# # Step 1. make a random list of numbers to work with
# import random 

# list = []

# for i in range(0, 5):
#     n = random.randint(1, 10)
#     list.append(n)

# print(list) # Manually enter the output of this into list, so we are working with the same set of no.

l= [9, 7, 7, 9, 4]


# # 1a. Calculate the mean
# list = [9, 7, 7, 9, 4]

# total = sum(list)
# x = total / (len(list))

# print(x)



# # 1b. Calculate the median
# from numpy import median 

# list.sort()
# print("This is the list, when it is sorted: \n", list)

# print("")

# x = median(list)
# print("The median of the list is: \n", x)



# 1c. Calculate the mode
import statistics

x = statistics.mode(list)

print("This is the mode: ", x)

## Help https://www.nobledesktop.com/learn/python/mode-in-python







