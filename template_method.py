from abc import ABC, abstractmethod


class Processes(ABC):

    def all_data(self):
        self.gather_materials()
        self.made_up_product()
        self.quality_control()
        self.end()

    @abstractmethod
    def gather_materials(self):
        pass

    @abstractmethod
    def made_up_product(self):
        pass

    @abstractmethod
    def quality_control(self):
        pass

    @staticmethod
    def end():
        print("All processes are completed.")


class First_Product(Processes):

    def gather_materials(self):
        print("Gathering material for the first product")

    def made_up_product(self):
        print("Mading up the first product")

    def quality_control(self):
        print("Perofrming quality control of the first product")


class Second_Product(Processes):

    def gather_materials(self):
        print("Gathering material for the second product")

    def made_up_product(self):
        print("Mading up the second product")

    def quality_control(self):
        print("Perofrming quality control of the second product")


def main():

    product_1 = First_Product()
    product_1.all_data()

    product_2 = Second_Product()
    product_2.all_data()


main()
