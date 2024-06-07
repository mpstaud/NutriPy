from functions import maintenance_calories, lose_one_lb_per_week, lose_two_lbs_per_week,gain_one_lb_per_week, gain_two_lbs_per_week
weight = int(input('Enter your weight:'))


print('If you want to lose 1 lb per week, press A.')
print('If you want to lose 2 lbs per week, press B.')
print('If you want to maintain weight, press C.')
print('If you want to gain 1 lb per week, press D.')
print('If you want to gain 2 lbs per week, press E.')
selection = input('Enter you selection please: ')

if selection == 'A':
    print("You'll want to eat around " + str(lose_one_lb_per_week(weight)) + ' Calories')
elif selection == 'B':
    print("You'll want to eat around " + str(lose_two_lbs_per_week(weight)) + ' Calories')
elif selection == 'C':
    print("You'll want to eat around " + str(maintenance_calories(weight)) + ' Calories')
elif selection == 'D':
    print("You'll want to eat around " + str(gain_one_lb_per_week(weight)) + ' Calories')
else:
    print("You'll want to eat around " + str(gain_two_lbs_per_week(weight)) + ' Calories')


