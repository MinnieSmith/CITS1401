def findPrime(n):
    count = 0
    for num in range(n):
        if num > 1:
            for i in range(2, n):
                if (num % i) == 0:
                    break
                else:
                    count += 1
                    print(i, count)


findPrime(10)
