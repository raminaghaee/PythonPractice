for number in range(1, 20):
    prime = True
    for j in range(2, number):
        if number % j == 0:
            prime = False
            break
    if prime:
        print(number)
