class Singleton():
# automatically inherits from the object class
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            # super.().__new__(cls) running __new__ in the object class
            # creating empty object of class cls (Singleton)
            cls._instance = super().__new__(cls)
            print("One and only object")
        return cls._instance
    
my_obj1 = Singleton()
my_obj2 = Singleton()

print(my_obj1)
print(my_obj2)
print(my_obj1 is my_obj2)