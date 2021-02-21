# Composition

class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class Child(object):

    def __init__(self):       # This allows for it to be possible to get the Other stuff? Even though it is its own Class
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD AFTER OTHER altered()")

son = Child()
son.implicit()
print("-----")
son.override()
print("-----")
son.altered()

"""
# Inhertance

class Parent(object):
	def altered(self):
		print("PARENT altered…")

class Child(Parent):
	def altered(self):
            print("CHILD BEFORE PARENT altered.")
            super(Child, self).altered() # This prints 'Parent altered'
            print("CHILD AFTER PARENT altered…")

dad = Parent()
son = Child()

dad.altered()
print("---------------------")
son.altered()
"""
