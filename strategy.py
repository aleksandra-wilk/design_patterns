from abc import ABC, abstractmethod

# Strategy
class Strategy(ABC):
    
    @abstractmethod
    def execute(self):
        pass

# Concreate Strategy 1
class Flying(Strategy):

    def execute(self):
        print("I'm flying")

# Concrete Strategy 2
class Swimming(Strategy):

    def execute(self):
        print("I'm swimming")

# Concreate Strategy 3
class Walking(Strategy):

    def execute(self):
        print("I'm walking")
    
# Context
class Duck:

    def __init__(self, move_type: Strategy):
        self.strategy = move_type

    def set_moving_type(self, move_type: Strategy):
        if not isinstance(move_type, Strategy):
            raise NotImplementedError("Wrong move type.")
        self.strategy = move_type

    def move(self):
        return self.strategy.execute()


def main():
    d1 = Duck(Flying())
    d1.move()
    d1.set_moving_type(Walking())
    d1.move()

main()