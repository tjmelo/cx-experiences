'''
App proposed (2):

- Get a base wage of a employee that who earns 14.25 an hour and has worked for 163 basic hours.
- The employee has worked for 20 extra hours to which earn the double.

- Input: wage base and hours worked.
- Ouput: Wage and hours multiplied.

'''

print('Starts app')

getInputedValueHour = input('Type the value of hour: ')
getInputedHoursWorked = input('Type total hours worked: ')
getInputedExtraHours = input('Type total of extra hours: ')

valueOfBaseHour = float(getInputedValueHour)
baseHoursWorked = float(getInputedHoursWorked)

valueOfExtraHours = valueOfBaseHour * 2
extraHoursWorked = float(getInputedExtraHours)

totalWageOfEmployee = (valueOfBaseHour * baseHoursWorked) + (valueOfExtraHours * extraHoursWorked)

print('The employee has earned: {0:.2f}'.format(totalWageOfEmployee))
