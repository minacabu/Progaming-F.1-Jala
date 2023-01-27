hourPerDay = int(input('How many hours you work per day?'))
dayPerMouth = int(input('How many days you work per mouth?'))
hourTax= 20

salary = round(hourTax*hourPerDay*dayPerMouth)
totalHours=dayPerMouth*hourPerDay
print(f'You gain USD {salary} per mouth and USD {salary/totalHours} per worked hour')
