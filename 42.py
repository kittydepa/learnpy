# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    print("This is for you.")

chicken = Animal()
chicken


## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name
        print("Dog here.")

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name
        print(name, " is a person.")
        ## Person has-a pet of some kind
        self.pet = None


## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## what is dis -
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary
        print(name, " makes ", salary)

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")
rover

## Satan is-a Cat
satan = Cat("Satan")

## Tiger, is-a  cat
tiger = Cat("Tiger")

## Mary is-a person
mary = Person("Mary")
mary

## Mary has-a Cat
mary.pet = [satan, tiger, rover] # list of pets
#Taken from REDDIT! The above and below...
mary.pet = {'cats': [satan, tiger], 'dog': [rover]} # dict of list of pets


## Frank is-a employee, ..... Frank has-a salary
frank = Employee("Frank", 120000)
frank
gigi = Employee("Gigi", "no money")

## Frank has-a dog
frank.pet = rover

# flipper is-a fish
flipper = Fish()

## Crouse is a salmon (??)
crouse = Salmon()

## Harry is a Halibut
harry = Halibut()
