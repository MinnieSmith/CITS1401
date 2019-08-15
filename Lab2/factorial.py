def factorial ():
    number = input("please input factorial value:")
    number = int(number)
    fact = 1
    for i in range(1, number+1):
        fact = fact * i
    print("The factorial of " + str(number) + " is: ")
    print(fact)


factorial()