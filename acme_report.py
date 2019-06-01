"""Creating report on Acme Products by Randomly Generating names"""

from random import randint, sample, uniform, choice
from acme import Product
# can't import itertools
# Useful to use with random.sample to generate names
# need to give each product a random number for weight, price and flammability


def generate_products(num_products=30):
    """ Randomly sampling from two lists of names to form product Names

    Inputting: two lists with 5 names each, creating 30 num_products
    Outputting: list of product names with two letters each,

    num_products = 30, so outputs a list of 30 products

    """

    products = []
    ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
    NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
# giving a syntax error but I have tries re-typing
# and everything but won't go away
    for _ in range(num_products):
        product = Product(name = '{a} {b}'.format(a=choice(ADJECTIVES), b=choice(NOUNS)),
                     price=randint(5, 100),
                     weight=randint(5, 100),
                     flammability=uniform(0.0, 2.5))

        products.append(product)
    # products.append(Product(name=name, price = price, weight = weight,
    # flammability = flammability))
    return products
# products = random.sample(set(itertools.product(ADJECTIVES , NOUNS)), 30)
# can't use itertools


def inventory_report(products):
    #so we need price, weight and flammability for this REPORT
    #we need to set unique_names as an empty list first
    unique_names = []
    price_total = 0
    weight_total = 0
    flammability_total = 0
    product_count = len(products)

"""to make the report, we need to put unique names with
their weight, price and flammability_total"""
for product in products:
    unique_names.append(product.name)
    price_total += product.price
    weight_total += product.weight
#
    average_price = (price_total/product_count)
    average_weight = (weight_total/product_count)
    average_flammability = (flammability_total/product_count)

    print('\n\n--------ACME CORPORATION OFFICIAL INVETORY REPORT--------\n')
    print('Unique Product Names:', len(set(unique_names)))
    print('Average Price:', average_price)
    print('Average Weight:', average_weight)
    print('Average flammability', average_flammability)

if __name__ == '__main__':
    inventory_report(generate_products())
