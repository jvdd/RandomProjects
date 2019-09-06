
import datetime
from user import User
from drink import CaffeinatedDrink

user = User()

drinks = {  # Coffee drinks at work
    'filtered_coffee' : CaffeinatedDrink('filtered_coffee', 70),
    'espresso' : CaffeinatedDrink('espresso', 130),
    'cappuccino' : CaffeinatedDrink('cappuccino', 130), # same as esprosso since it is composed of espresso
    'latte' : CaffeinatedDrink('latte', 130), # same as esprosso since it is composed of espresso
    'cafe_au_lait' : CaffeinatedDrink('cafe_au_lait', 70), # same as coffee since it is composed of coffee
    'tea' : CaffeinatedDrink('tea', 11)
    }


user.add_drink(drinks['espresso'], datetime.datetime.strptime('08:30', "%H:%M"))
user.add_drink(drinks['filtered_coffee'], datetime.datetime.strptime('10:15', "%H:%M"))
user.add_drink(drinks['cafe_au_lait'], datetime.datetime.strptime('13:15', "%H:%M"))

blood_level = user.get_caffeine_level()
print('Caffeine in blood:', blood_level, 'mg.')
print('Number of drinks running through my veins:')
for drink in drinks:
    print(drink + ':', drinks[drink].quantity_to_drink(blood_level))

caffeine_func = user.get_caffeine_function()
print(caffeine_func(0))
print(caffeine_func(5.7))

day_func = user.get_day_function()
print(day_func(8))
print(day_func(10))
print(day_func(12))
print(day_func(14))


user.plot_caffeine_decay_today()
#user.plot_caffeine_decay_from_now()

'''
inp = ' '
while inp.upper() != 'Q':
    print('What kind of drink did you have?')
    print('Options are:', [drink for drink in drinks])
    drink = input()
    while not drink in drinks:
        print(drink, 'is not an option!')
        print('Please enter one of these options:', [drink for drink in drinks])
        drink = input()
    isValid = False
    while not isValid:
        try:
            time = datetime.datetime.strptime(input('Enter the time when you consumed your drink in the format hh:mm '), "%H:%M")
            isValid = True
        except ValueError:
            print('Wrong format!')
            print('Try again! hh:mm')
    user.add_drink(drinks[drink], time)
    print('\nEnter Q to stop adding consumption, otherwise press enter.')
    inp = input()

print('\nYour current caffeine level:')
print(user.get_caffeine_level(), 'mg')
'''
