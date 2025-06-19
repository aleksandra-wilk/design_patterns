from abc import ABC, abstractmethod


# Receiver
class Vaccum():
    def map(self):
        print("I know how to map the room.")

    def scan(self):
        print("I know how to scan the room.")


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class Mapping(Command):
    def __init__(self, vaccum):
        self.vaccum = vaccum

    def execute(self):
        self.vaccum.map()


class Scanning(Command):
    def __init__(self, vaccum):
        self.vaccum = vaccum

    def execute(self):
        self.vaccum.scan()

# Invoker
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def perform(self):
        self.command.execute()


def main():

    vaccum = Vaccum()
    map_the_room = Mapping(vaccum)
    scan_the_room = Scanning(vaccum)

    remote_control = RemoteControl()
    remote_control.set_command(scan_the_room)
    remote_control.perform()
    
    remote_control.set_command(map_the_room)
    remote_control.perform()


main()
