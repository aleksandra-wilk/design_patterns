class Singleton():
    # automatically inherits from the object class

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # super().__new__(cls) running __new__ in the object class
            # creating empty object of class cls (Singleton)
            cls._instance = super().__new__(cls)
            print("One and only object")
        return cls._instance


class Example(Singleton):
    def __init__(self, id):
        self.id = id


my_obj1 = Example(1)
my_obj2 = Example(2)

print(my_obj1)
print(my_obj2)
print(my_obj1 is my_obj2)

my_obj1.variable = "Variable 1"
print(my_obj2.variable)

