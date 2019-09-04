
import datetime
import numpy as np
import matplotlib.pyplot as plt
from drink import Consumption

class User:

    def __init__(self):
        self.consumptions = []

    def add_drink(self, drink, consumed):
        ''' Adds a consumption for the user
        '''
        consumption = Consumption(drink, consumed)
        self.consumptions.append(consumption)

    def get_cafeine_level(self):
        '''
        '''
        now = datetime.datetime.now().time()
        now = now.hour + now.minute / 60
        cafeine = 0
        for cons in self.consumptions:
            consumed_time = cons.consumed.time()
            consumed_time = consumed_time.hour + consumed_time.minute / 60
            time_passed = now - consumed_time
            cafeine += cons.drink.get_quantity(time_passed)
        return cafeine

    def get_cafeine_function(self):
        ''' Returns a mathematical function of the cafeine decay starting from now.
        '''
        now = datetime.datetime.now().time()
        now = now.hour + now.minute / 60
        cafeine_funcs = []
        for cons in self.consumptions:
            consumed_time = cons.consumed.time()
            consumed_time = consumed_time.hour + consumed_time.minute / 60
            time_passed = now - consumed_time
            lambda_func = cons.drink.get_quantity_lambda(time_passed)
            cafeine_funcs += [lambda_func] #lambda x : cons.drink.get_quantity(time_passed + x)
        cafeine_func = lambda x : sum([func(x) for func in cafeine_funcs])
        return cafeine_func

    def plot_cafeine_decay(self):
        cafeine_func = self.get_cafeine_function()
        x = np.linspace(0, 12, 12*60)
        y = [cafeine_func(x_val) for x_val in x]
        plt.figure(figsize=(12,4))
        plt.title('Cafeine decay')
        plt.plot(x, y)
        plt.xlabel('Hours from now')
        plt.ylabel('Cafeine in blood (in mg)')
        plt.show()