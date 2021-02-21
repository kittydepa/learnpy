def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice


"""
# Meant to be execture in another file?
from decorators import wrapper_do_twice

@wrapper_do_twice
def say_whee():
    print("Whee!")

say_whee()"""
