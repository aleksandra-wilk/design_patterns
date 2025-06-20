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

    def notify(self, title, tag):
        for observer in self._observers:
            observer.update(title, tag)

    def add_video(self, title, tag):
        print(f"New video added with title: {title}")
        tag = tag
        self.notify(title, tag)


class Follower(Observer):

    def __init__(self, nickname, intrest):
        self.nickname = nickname
        self.intrest = intrest

    def update(self, title, tag):
        if self.intrest == tag:
            print(f'{self.nickname} liked "{title}" video')


def main():
    follower1 = Follower("alexandra159", "pilates")
    follower2 = Follower("MMalon", "gym")

    channel = Channel("Daily trainings")

    channel.attach(follower1)
    channel.attach(follower2)

    channel.add_video("10 minutes Pliates training for strong core", "pilates")
    channel.add_video("Exercises for upper body", "gym")


main()
