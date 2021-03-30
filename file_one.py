# Python file one module
import file_two

print("File one __name__ is set to: {}" .format(__name__))

if __name__ == "__main__": # If the current file is the MAIN file/module, then print this
    print("File one executed when ran directly.")
else:   # Else, tell me that it was NOT the main file, and just imported from another
    print("File one execture when imported.")
