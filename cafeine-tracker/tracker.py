
import datetime
from user import User
from drink import CaffeinatedDrink

user = User()

drinks = {  
    'filtered_coffee' : CaffeinatedDrink('filtered_coffee', 70),
    'espresso' : CaffeinatedDrink('espresso', 130),
    'tea' : CaffeinatedDrink('tea', 11)
    }

user.add_drink(drinks['filtered_coffee'], datetime.datetime.strptime('08:30', "%H:%M"))
user.add_drink(drinks['filtered_coffee'], datetime.datetime.strptime('10:30', "%H:%M"))
user.add_drink(drinks['tea'], datetime.datetime.strptime('15:15', "%H:%M"))

blood_level = user.get_cafeine_level()
print('Caffeine in blood:', blood_level, 'mg.')
print('Number of drinks running through my veins:')
for drink in drinks:
    print(drink + ':', drinks[drink].quantity_to_drink(blood_level))

cafeine_func = user.get_cafeine_function()
print(cafeine_func(0))
print(cafeine_func(5.7))

user.plot_cafeine_decay_from_now()

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

print('\nYour current cafeine level:')
print(user.get_cafeine_level(), 'mg')
'''
