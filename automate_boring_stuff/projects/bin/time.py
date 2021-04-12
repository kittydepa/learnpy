# Ch 15 in 'Automate the boring stuff'

# import time
# x = time.time() 

# print(x) 
'''
time.time() will print out how many seconds have passed since the
Unix epoch (a common time reference in programming), which is the
date: 12 AM, Jan 1, 1970.

These Epoch time stamps can be used to *profile* code, or i.e., 
measure how long it takes for a piece of code to run.
You can do this by calling time.time() before and after a block of code
'''

# -------------------------------------------------

# import time
# def calcProd():
#     # calculate tje produce of the first 100, 000 numbers
#     product = 1
#     for i in range (1, 100000):
#         product = product * i
#     return product

# startTime = time.time()
# prod = calcProd()
# endTime = time.time()
# print('The result is %s digits long.' % (len(str(prod))))
# print('Took %s seconds to calculate.' % (endTime - startTime))

# -------------------------------------------------

# import time
# for i in range(3):
#     print('Tick')
#     time.sleep(1)
#     print('Tock')
#     time.sleep(1)

# time.sleep(5)