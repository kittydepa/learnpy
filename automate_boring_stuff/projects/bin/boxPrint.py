'''
Ch 10 - Practicing Raising Exceptions() from 'Automate the Boring Stuff with Python' No Starch Press
'''

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2')
    
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    
    print(symbol * width)


for sym, w, h, in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:                          # if an Exception object needs to be returned from boxPrint(), then it will store it into the variable named 'err'
        print('An exception happened: ' + str(err))   # We convert the Exception object (err) into a string to produce a user-friendlt error message