"""Acme class that has multiple different attributes"""

from random import randint


class Product:
    """Defining the attributes and init"""

    def __init__(self, name=None, price =10, weight = 20, flammability = 0.5,
                identifier = None):

        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)


    def stealability(self):
        ratio = price/weight
        if ratio < 0.5:
            print('Not so stealable')
        elif 0.5 <= ratio < 1:
            print('kind stealable')
        else:
            print('stealable')




    def explode(self):
        prod = self.flammability * self.weight
        if prod < 10:
             print('"...fizzle."')
        elif 10 <= prod < 50:
            print('""...Boom!"')
        else:
            print('"...BABOOM!!"')




class BoxingGlove(Product):
    """Adding a subclass of product which inherits variables from parent class"""

    def __init__(self, name=None, price =10, weight = 10, flammability = 0.5,
                identifier = None):
        super().__init__(name = name, price = price, weight = weight,
                        flammability = flammability, identifier = identifier)


    def punch(self):
        if weight < 5:
            print('That tickles.')
        elif 5 <= weight < 15:
            print('Hey that Hurt!')
        else:
            print('OUCH!')

    def explode(self):
        prod = self.flammability * self.weight
        print("...it's a glove")
