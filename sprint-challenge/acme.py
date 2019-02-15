"""Product classes for Acme corporation."""

import random


class Product:
    """Standard product class for Acme corporation. Assigns name, price,
    weight and flammability. Also randomly creates identifier attribute between
    1000000 and 9999999, inclusive.
    Args:
        name (str): name of product
        price (int): price of product (default 10)
        weight (int): weight of product (default 20)
        flammability (float) flammability of product (default 0.5)
    """

    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        """Returns stealability string of product.
        Args:
            None
        Returns:
            (str) Stealability of product as three possible outputs
        """

        ratio = self.price / self.weight
        if ratio < 0.5:
            return "Not so stealable..."
        elif ratio >= 0.5 and ratio < 1.0:
            return "Kinda stealable."
        return "Very stealable!"

    def explode(self):
        """Returns explosiveness string of product.
        Args:
            None
        Returns:
            (str) Explosiveness of product as three possible outputs
        """

        comb = self.flammability * self.weight
        if comb < 10:
            return "...fizzle."
        elif comb >= 10 and comb < 50:
            return "...boom!"
        return "...BABOOM!!"


class BoxingGlove(Product):
    """BoxingGlove product subclass based on Product class for Acme corporation.
    Args:
        name (str): name of product
        price (int): price of product (default 10)
        weight (int): weight of product (default 10)
        flammability (float) flammability of product (default 0.5)
    """

    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        """Returns explosiveness string of BoxingGlove.
        Args:
            None
        Returns:
            (str) Explosiveness of BoxingGlove as output '...it's a glove.'
        """

        return "...it's a glove."

    def punch(self):
        """Returns punch string of BoxingGlove.
        Args:
            None
        Returns:
            (str) Punch string of BoxingGlove as three possible outputs
        """

        if self.weight < 5:
            return "That tickles."
        elif self.weight >= 5 and self.weight < 15:
            return "Hey that hurt!"
        return "OUCH!"
