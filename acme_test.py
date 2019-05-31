import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):

    """Making sure Acme products are the tops!"""


    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)


    #one to test default values like flammability_total
    def test_default_product_flammability(self):
        """Test default product flammability being 0.4."""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.4)


    def test_default_explosion(self):
        """Test default product explode and stealability."""
        prod = Product('Test Product', 200, 100, 10)
        self.assertEqual(prod.explode(), '"...fizzle"'),
        self.assertEqual(prod.stealability(), 'stealable')

class AcmeReportTests(unittest.TestCase):

    def test_default_num_products(self):
        """check it really receives a number of 30"""
        generated_products = generate_products() #from the previous REPORT
        self.assertEqual(len(generated_products), 30)

    def test_legal_names(self):

        ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
        NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

        #use assert in to check if all the names generated were valid names to generate, shouldn't be hard
        #get products from generate_products
        generated_products = generate_products()
        for product in generated_products:
            product_name = product.name.split() #need to split the product names
            ADJ = product_name[0] #get the first part of the product_name
            NOUN = product_name[1] #get the second part of the product_name
            self.assertIn(ADJ, ADJECTIVES)
            self.assertIn(NOUN, NOUNS) #assertIn will tell us if they are the valid names found in the above lists



if __name__ == '__main__':
    unittest.main()
