from abc import ABC, abstractmethod


class Builder(ABC):
    
    @abstractmethod
    def add_dough(self):
        pass
    
    @abstractmethod
    def add_sauce(self):
        pass
    
    @abstractmethod
    def add_cheese(self):
        pass


class Pizza:
    def __init__(self):
        self.dough = None
        self.sauce = None
        self.cheese = None
        
    def __str__(self):
        return f"Dough: {self.dough}, sauce: {self.sauce}, cheese: {self.cheese}"
        
        
class PizzaBuilder(Builder):
    
    def __init__(self):
        self.pizza = Pizza()
    
    def add_dough(self):
        self.pizza.dough = True
        return self
        
    def add_sauce(self):
        self.pizza.sauce = True
        return self
        
    def add_cheese(self):
        self.pizza.cheese = True
        return self
        
    def pizza_ready(self):
        return self.pizza
    
    
if __name__ == "__main__":
    builder = PizzaBuilder()
    pizza = builder.add_cheese().add_sauce().add_dough().pizza_ready()
    print(pizza)
             
    