from abc import ABC, abstractmethod


class Product:
    
    def __init__(self):
        self.parts = []
        
    def add(self, part):
        self.parts.append(part)


class Builder(ABC):
    
    @abstractmethod
    def produce_part_A(self):
        pass
    
    @abstractmethod
    def produce_part_B(self):
        pass
    
    @abstractmethod
    def produce_part_C(self):
        pass
    
    
class ConcreteBuilder1(Builder):
    
    def __init__(self):
        self.product = Product()
    
    def produce_part_A(self):
        self.product.add("Part A1")
        
    def produce_part_B(self):
        self.product.add("Part B1")
        
    def produce_part_C(self):
        self.product.add("Part C1")
    
    
class Director:
    
    def __init__(self):
        self._builder = None
        
    @property
    def builder(self):
        return self._builder
    
    @builder.setter
    def builder(self, builder):
        if not isinstance(builder, ConcreteBuilder1):
            raise NotImplemented("Object is not Builder class")
        self._builder = builder
    
    def build_product(self):
        self.builder.produce_part_A()
        self.builder.produce_part_B()
        self.builder.produce_part_C()
        return self.builder.product
        
    
if __name__ == "__main__":
    
    builder = ConcreteBuilder1()
    director = Director()
    director.builder = builder
    product = director.build_product()
    print(product.parts)
    
    
        