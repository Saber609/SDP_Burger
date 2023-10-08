class Burger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Burger, cls).__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self):
        if not self.__initialized:
            self.description = "Burger"
            self.cost = 5.0
            self.__initialized = True

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

class IngredientStrategy:
    def cost(self):
        raise NotImplementedError("Subclasses must implement the cost() method.")

class BeefPatty(IngredientStrategy):
    def cost(self):
        return 2.50

class Cheese(IngredientStrategy):
    def cost(self):
        return 1.00

class Lettuce(IngredientStrategy):
    def cost(self):
        return 0.25

class Tomato(IngredientStrategy):
    def cost(self):
        return 0.50

class BurgerDecorator:
    def __init__(self, burger):
        self._burger = burger

    def get_description(self):
        return self._burger.get_description()

    def get_cost(self):
        return self._burger.get_cost()

class CustomBurger(BurgerDecorator):
    def __init__(self, burger, custom_description, custom_cost):
        super().__init__(burger)
        self.description = custom_description
        self.cost = custom_cost

if __name__ == "__main__":
    burger = Burger()
    burger = CustomBurger(burger, "Double Beef Patty Burger", burger.get_cost() + 2.50)
    burger = CustomBurger(burger, "With Cheese", burger.get_cost() + 1.00)
    burger = CustomBurger(burger, "With Lettuce", burger.get_cost() + 0.25)
    burger = CustomBurger(burger, "With Tomato", burger.get_cost() + 0.50)

    print("Burger Description:", burger.get_description())
    print("Total Cost:", burger.get_cost())