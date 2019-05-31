"""Creating report on Acme Products by Randomly Generating names"""

from random import randint, sample, uniform, choice
from acme import Product
#can't import itertools
# Useful to use with random.sample to generate names

#need to give each product a random number for weight, price and flammability
def generate_products(num_products=30):
    """ Randomly sampling from two lists of names to form product Names

    Inputting: two lists with 5 names each, randomly sampling and creating 30 num_products
    Outputting: list of product names with two letters each,

    num_products = 30, so outputs a list of 30 products with names chosen randomly from two lists

    """

    products = []

    ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
    NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
#giving a syntax error but I have tries re-typing and everything but won't go away
    for _ in range(num_products):
        name = (random.choice(ADJECTIVES)) + ' ' + random.choice(NOUNS))
        price = randint(5,100)
        weight = randint(5,100)
        flammability = uniform(0.0,2.5)
    #use append to put it all together
        products.append(Product(name=name, price = price, weight = weight,
                            flammability = flammability))
    return products
#    products = random.sample(set(itertools.product(ADJECTIVES , NOUNS)), 30)
#can't use itertools



def inventory_report(products):
    #so we need price, weight and flammability for this REPORT
    #also, we need unique names in products, wonder if we can use value_counts and get names from there

    #we need to set unique_names as an empty list first
    unique_names = []
    price_total =  0 #for all num_products
    weight_total = 0
    flammability_total = 0
    no_of_products = len(product) #going to need this to calculate the Average

#to make the report, we need to put unique names with their weight, price and flammability_total
    for product in products:
        unique_names.append(product.name)
        price_total += product.price
        weight_total += product.weight
        flammabiliy_total += product.flammability

    average_price = (price_total/product_count)
    average_weight = (weight_total/product_count)
    average_flammability = (flammability_total/product_count)


    print('\n\n--------ACME CORPORATION OFFICIAL INVETORY REPORT--------\n')
    print('Unique Product Names:', len(set(unique_names)))
    print('Average Price:', average_price)
    print('Average Weight:', average_weight)
    print('Average flammability', average_flammability)
    print(f'Average price: {winning_team_average: .1f}')
    print(f'Average Score of Losing Team: {losing_team_average:.1f}\n')

"""
$ python acme_report.py
ACME CORPORATION OFFICIAL INVENTORY REPORT
Unique product names: 19
Average price: 56.8
Average weight: 54.166666666666664
Average flammability: 1.258097155966675
"""
if __name__ == '__main__':
    inventory_report(generate_products())
