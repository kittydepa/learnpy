def divide(x, y):
    print(f'{x}/{y} is {x / y}')

    if y <= 1:
        raise Exception("Sorry, no numbers less than 2 here. I made an exception this time.")

divide(14, 7)
divide(10, 1)
