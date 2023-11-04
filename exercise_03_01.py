hours = input('Enter Hours: ')
rate = input('Enter Rate: ')

if float(hours) > 40:
    overtime = (float(hours) - 40) * float(rate) * 1.5
    pay = 40 * float(rate) + overtime
    print('Pay:',pay)
else:
    pay = float(hours) * float(rate)
    print("Pay:",pay)

