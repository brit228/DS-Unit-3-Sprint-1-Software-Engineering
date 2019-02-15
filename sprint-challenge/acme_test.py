"""Unittests for acme module and acme_report module."""

import unittest
from acme import Product, BoxingGlove
from acme_report import generate_products


class AcmeProductTests(unittest.TestCase):
    """Testing default Product attributes and functions.
    Args:
        None
    """

    def test_default_product_price(self):
        """Test default product price being 10.
        Args:
            None
        Returns:
            None"""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_stealability(self):
        """Test default product stealability function output being
        'Kinda stealable.'.
        Args:
            None
        Returns:
            None"""
        prod = Product('Test Product')
        self.assertEqual(prod.stealability(), "Kinda stealable.")

    def test_default_explode(self):
        """Test default product explode function output being '...boom!'.
        Args:
            None
        Returns:
            None"""
        prod = Product('Test Product')
        self.assertEqual(prod.explode(), "...boom!")


class AcmeReportTests(unittest.TestCase):
    """Testing acme_report module outputs.
    Args:
        None
    """

    def test_default_num_products(self):
        """Test default generate_products function output being list with of
        length of 30.
        Args:
            None
        Returns:
            None"""
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        """Test default generate_products function output Product objects
        having legal name attributes.
        Args:
            None
        Returns:
            None"""
        adj_list = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
        noun_list = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']
        prods = generate_products()
        for p in prods:
            self.assertEqual(p.name.count(" "), 1)
            self.assertIn(p.name.split(" ")[0], adj_list)
            self.assertIn(p.name.split(" ")[-1], noun_list)


if __name__ == '__main__':
    """Run unittests."""
    unittest.main()
