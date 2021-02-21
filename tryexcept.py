def divide(x, y):
    try:
        print(f'{x}/{y} is {x / y}')
    except ZeroDivisionError as e:
        print(e)
    finally:
        print("Okay, on to the next problem.")

divide(10, 2)
divide(10, 0)
divide(10, 4)
