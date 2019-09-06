
import datetime
import numpy as np
import matplotlib.pyplot as plt
from drink import Consumption

class User:

    def __init__(self):
        self.consumptions = []

    ## Private methods

    @staticmethod
    def _datetime_to_float(moment):
        ''' Converts the given datetime to a float (only for the time, the date is discarded).

        :param moment: the datetime for which we want the time in a float format.
        :return: the time in float format, e.g, a datetime with as time 08:30 will be 
        converted to 8,5. 
        '''
        moment_time = moment.time()
        moment_float = moment_time.hour + moment.minute / 60
        return moment_float


    ## Public methods

    def add_drink(self, drink, consumed):
        ''' Adds a consumption for the user
        '''
        consumption = Consumption(drink, consumed)
        self.consumptions.append(consumption)

    def get_caffeine_level(self):
        '''
        '''
        now = User._datetime_to_float(datetime.datetime.now())
        caffeine = 0
        for cons in self.consumptions:
            consumed_time = User._datetime_to_float(cons.consumed)
            time_passed = now - consumed_time
            caffeine += cons.drink.get_quantity(time_passed)
        return caffeine

    def get_caffeine_function(self):
        ''' Returns a mathematical function of the caffeine decay starting from now.

        :return: TODO
        '''
        now = User._datetime_to_float(datetime.datetime.now())
        caffeine_funcs = []
        for cons in self.consumptions:
            consumed_time = User._datetime_to_float(cons.consumed)
            time_passed = now - consumed_time
            lambda_func = cons.drink.get_quantity_lambda(time_passed)
            caffeine_funcs += [lambda_func] #lambda x : cons.drink.get_quantity(time_passed + x)
        caffeine_func = lambda x : sum([func(x) for func in caffeine_funcs])
        return caffeine_func

    def plot_caffeine_decay_from_now(self):
        '''
        TODO
        '''
        caffeine_func = self.get_caffeine_function()
        x = np.linspace(0, 24, 12*60)
        y = [caffeine_func(x_val) for x_val in x]
        plt.figure(figsize=(12,4))
        plt.title('Caffeine decay')
        plt.plot(x, y, label='caffeine')
        plt.plot([0,24],[11,11],label='tea') # TODO dit beter maken
        plt.xlabel('Hours from now')
        plt.ylabel('Caffeine in blood (in mg)')
        plt.legend()
        plt.show()

    def plot_caffeine_decay_today(self):
        time_stamps_floats = [User._datetime_to_float(cons.consumed) for cons in self.consumptions]
        
        raise NotImplementedError # TODO