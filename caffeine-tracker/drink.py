
from helper import datetime_to_float


class Consumption:
    ''' Wrapper for a drink that keep tracks of when you consumed the drink
    '''

    def __init__(self, drink, consumed):
        ''' Initializes the parameters for a consumption.
        
        :param drink: the drink you consumed.
        :param consumed: the time of when you consumed the drink.
        '''
        self.drink = drink
        self.consumed = consumed

    def day_function(self, time):
        consumed_time = datetime_to_float(self.consumed)
        #time = datetime_to_float(time)
        diff = time - consumed_time
        if diff > 0:
            return self.drink.get_quantity(diff)
        return 0
        


class AbstractDrink:

    def __init__(self, name, quantity, half_life):
        ''' Initializes the parameters for a drink.

        :param name: the name of the drink.
        :param quantity: the amount of quantity of the substance that has the given half life is initially present
        :param half_life: the time required for a quantity to reduce to half of its initial value.
        '''
        self.name = name
        self.quantity = quantity
        self.half_life = half_life

    def get_quantity(self, time_passed):
        ''' Calculate the quantity of the substance that is left in a person its blood after the
        given period of time (since intake).

        :param time_passed: the time passed (in hours) since the drink was consumed.
        :return: the amount of the substance still left in the blood.
        '''
        return self.quantity * ( (1/2) ** (time_passed / self.half_life) )

    def get_quantity_lambda(self, time_passed):
        return lambda x : self.quantity * ( (1/2) ** ((time_passed +x) / self.half_life) )

    def get_quantity_lambda_day(self, consumed_float):
        return lambda x : self.quantity * ( (1/2) ** ((x - consumed_float) / self.half_life) ) if consumed_float <= x else 0

    def quantity_to_drink(self, quantity):
        '''
        '''
        return quantity / self.quantity


class CaffeinatedDrink(AbstractDrink):
    ''' A caffeinated drink.
    '''

    def __init__(self, name, caffeine):
        ''' Initializes the parameters for a caffeinated drink.

        :param name: the name of the caffeinated drink.
        :param caffeine: the amount of caffeine in the drink in mg.
        '''
        super().__init__(name, caffeine, half_life=5.7)
    