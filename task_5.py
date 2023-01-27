def Prime():
    number = int(input('insert your number: '))
    if number >2:
        for i in range (2,number):
            if number % i == 0:
                print("Your number isn't prime\n"), Prime()
            else:
                print("Your number is prime\n"), Prime()
            break 
    elif number == 1: print("Your number isn't prime\n"), Prime()
    elif number == 0: print("Your number neutral\n"), Prime()
    else: print("I can't calculate your number, please try again"), Prime()
Prime()
        
