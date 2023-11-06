
num = 0
tot = 0.0

while True :

    sval = input("Enter a number: ")

    try:

        sval = int(sval)
        num = num + 1
        tot = tot + sval

    except:

        if sval == 'done':
            print(tot,num,tot/num)
            break
        else:
            print('Invalid input')




        
