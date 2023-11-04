hours = input('Enter Hours: ')
rate = input('Enter Rate: ')

try:
    if float(hours) > 40:
        overtime = (float(hours) - 40) * float(rate) * 1.5
        pay = 40 * float(rate) + overtime
        print('Pay:',pay)
    else:
        pay = float(hours) * float(rate)
        print("Pay:",pay)
except:
    pay = -1

if pay > 0:
    print("Pay:",pay)
else:
    print('Error, please enter numeric input')