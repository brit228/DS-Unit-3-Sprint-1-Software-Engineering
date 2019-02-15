"""Report functions and utilities for Acme Corporation Product class and
subclasses."""

import acme
import random


def generate_products(amount=30):
    """Generates a specified number of Product objects with random attributes.
    The name attribute is a combination of a selection from
    ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved'], a space and a
    selection from ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']. The
    price attribute is a random integer between 5 and 100, inclusive. The
    weight attribute is a random integer between 5 and 100, inclusive. The
    flammability attribute is a random float between 0.0 and 2.5 inclusive.
    Args:
        amount (int): amount of products to generate (default 30)
    Returns:
        (list(Product)) list of length `amount` of randomly generated Product
            classes
    """

    adj_list = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
    noun_list = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']
    return [acme.Product("{} {}".format(random.choice(adj_list),
                                        random.choice(noun_list)),
                         random.randint(5, 100), random.randint(5, 100),
                         random.uniform(0.0, 2.5)) for i in range(amount)]


def inventory_report(prod_list):
    """Prints summary of a list of Acme Corporation Product objects. Summary
    includes number of unique product names, average price of products, average
    weight of products and average flammabilities.
    Args:
        prod_list (list(Product)): list of Product objects
    Returns:
        None"""
    names = []
    prices = []
    weights = []
    flammabilities = []
    for p in prod_list:
        names.append(p.name)
        prices.append(p.price)
        weights.append(p.weight)
        flammabilities.append(p.flammability)
    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print("Unique product names:", len(list(set(names))))
    print("Average price:", sum(prices) / len(prices))
    print("Average weight:", sum(weights) / len(weights))
    print("Average flammability:", sum(flammabilities) / len(flammabilities))


if __name__ == '__main__':
    """If running as a program, run generate_products function with default
    amount and create summary using inventory_report function."""
    inventory_report(generate_products())
