from abc import ABC, abstractmethod


# Interface
class State(ABC):
    @abstractmethod
    def print():
        pass


# Context
class Printer():

    def __init__(self):
        self._state = Ready()

    def change_state(self, state):
        self._state = state

    def start_printing(self):
        self._state.print(self)


# Concrete States
class Ready(State):

    def print(self, printer):
        print("Printing has started")
        printer.change_state(InProgress())
        printer.start_printing()


class InProgress(State):

    def print(self, printer):
        print("Printing in progress...")
        printer.change_state(Finished())
        printer.start_printing()


class Finished(State):

    def print(self, printer):
        print("Printing is finished")
        printer.change_state(Ready())


def main():
    printer = Printer()
    printer.start_printing()


main()
