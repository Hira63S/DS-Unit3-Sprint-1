"""Acme class that has multiple different attributes"""

from random import randint


class Product:
    """Defining the attributes and init"""

    def __init__(self, name=None, price=10, weight=20, flammability=0.5,
                 identifier=None):

        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

    def stealability(self):
        ratio = self.price/self.weight
        if ratio < 0.5:
            print('Not so stealable')
        elif 0.5 <= ratio < 1:
            print('kind stealable')
        else:
            print('stealable')

    def explode(self):
        multiple = self.flammability * self.weight
        if multiple < 10:
                print('...fizzle.')
        elif multiple >=10 and multiple < 50:
                print('...Boom!')
        else:
                print('...BABOOM!!')


class BoxingGlove(Product):
    """Adding a subclass of product which
    inherits variables from parent class"""

    def __init__(self, name=None, price=10, weight=10, flammability=0.5,
                 identifier=None):
        super().__init__(name=name, price=price, weight=weight,
                         flammability=flammability, identifier=identifier)

    def punch(self):
        if self.weight < 5:
            print('That tickles.')
        elif 5 <= self.weight < 15:
            print('Hey that Hurt!')
        else:
            print('OUCH!')

    def explode(self):
        prod = self.flammability * self.weight
        print("...it's a glove")
