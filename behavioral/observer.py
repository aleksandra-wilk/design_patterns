from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update(self):
        pass


class Subject(ABC):

    @abstractmethod
    def attach(self):
        pass

    @abstractmethod
    def detach(self):
        pass

    @abstractmethod
    def notify(self):
        pass


class Channel(Subject):

    def __init__(self, channel_name):
        self.channel_name = channel_name
        self._observers = []

    def attach(self, follower):
        self._observers.append(follower)

    def detach(self, follower):
        self._observers.remove(follower)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

    def add_video(self, title):
        print(f"New video added with title: {title}")
        self.notify(f"{self.channel_name} added a video: {title}")


class Follower(Observer):

    def __init__(self, nickname):
        self.nickname = nickname

    def update(self, message):
        print(f"{self.nickname} got a message: {message}")


def main():
    follower = Follower("alexandra159")
    channel = Channel("Daily Cooking")

    channel.attach(follower)
    channel.add_video("Dinner propositions")


main()
