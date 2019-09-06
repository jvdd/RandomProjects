
import datetime
import numpy as np
import matplotlib.pyplot as plt
from drink import Consumption
from helper import datetime_to_float

class User:

    def __init__(self):
        self.consumptions = []

    ## Private methods


    ## Public methods

    def add_drink(self, drink, consumed):
        ''' Adds a consumption for the user
        '''
        consumption = Consumption(drink, consumed)
        self.consumptions.append(consumption)

    def get_caffeine_level(self):
        '''
        '''
        now = datetime_to_float(datetime.datetime.now())
        caffeine = 0
        for cons in self.consumptions:
            consumed_time = datetime_to_float(cons.consumed)
            time_passed = now - consumed_time
            caffeine += cons.drink.get_quantity(time_passed)
        return caffeine

    def get_caffeine_function(self):
        ''' Returns a mathematical function of the caffeine decay starting from now.

        :return: TODO
        '''
        now = datetime_to_float(datetime.datetime.now())
        caffeine_funcs = []
        for cons in self.consumptions:
            consumed_time = datetime_to_float(cons.consumed)
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

    def get_day_function(self):
        time_stamps_floats = [datetime_to_float(cons.consumed) for cons in self.consumptions]
        # wrapper for each lambda function that is 0 if the time (starting from 00:00) is
        # before the consumption time and otherwise the lambda method in terms of 
        # the time passed since the consumption time.
        day_funcs = []
        for cons, consumed_time in zip(self.consumptions, time_stamps_floats):
            lambda_func = cons.drink.get_quantity_lambda_day(consumed_time)
            day_funcs += [lambda_func]
        day_func = lambda x : sum([func(x) for func in day_funcs])
        return day_func

    def plot_caffeine_decay_today(self):
        '''
        TODO
        '''
        day_func = self.get_day_function()
        x = np.linspace(0, 24, 12*60)
        y = [day_func(x_val) for x_val in x]
        plt.figure(figsize=(12,4))
        plt.title('Caffeine in blood')
        now = datetime_to_float(datetime.datetime.now())
        plt.plot(now, day_func(now), 'r*', mfc='none', markersize=10, label='now')
        plt.plot(x, y, label='caffeine')
        plt.plot([0,24],[11,11],label='tea') # TODO dit beter maken
        plt.xlabel('Hour of the day')
        plt.xticks([i for i in range(25)])
        plt.ylabel('Caffeine in blood (in mg)')
        plt.legend()
        plt.show()