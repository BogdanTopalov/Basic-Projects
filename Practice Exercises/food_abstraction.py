from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def cook(self):
        pass


class FettuccineAlfredo(Product):
    def cook(self):
        print(f"Italian main course prepared: Fettuccine Alfredo")


class Tiramisu(Product):
    def cook(self):
        print(f"Italian dessert prepared: Tiramisu")


class DuckALOrange(Product):
    def cook(self):
        print(f"French main course prepared: Duck À L'Orange")


class CremeBrulee(Product):
    def cook(self):
        print(f"French dessert prepared: Crème brûlée")


class Factory(ABC):
    @abstractmethod
    def get_dish(self, type_of_meal):
        pass


class ItalianDishesFactory(Factory):
    def get_dish(self, type_of_meal):
        if type_of_meal == 'main':
            return FettuccineAlfredo()
        return Tiramisu()


class FrenchDishesFactory(Factory):
    def get_dish(self, type_of_meal):
        if type_of_meal == 'main':
            return DuckALOrange()
        return CremeBrulee()


class FactoryProducer:
    def get_factory(self, type_of_factory):
        if type_of_factory == 'italian':
            return ItalianDishesFactory()
        return FrenchDishesFactory()
