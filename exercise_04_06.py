def computepay(hours, rate):

    try:
        if float(hours) > 40:
            overtime = (float(hours) - 40) * float(rate) * 1.5
            pay = 40 * float(rate) + overtime
            return pay
        else:
            pay = float(hours) * float(rate)
            return pay
    except:
        pay = -1

    if pay > 0:
        return pay
    else:
        return('Error, please enter numeric input')

hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
print(computepay(hours,rate))