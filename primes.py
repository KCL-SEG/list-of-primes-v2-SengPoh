"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    if (number_of_primes < 1):
        raise ValueError("value must be at least 1")

    currentNum = 2
    for i in range(number_of_primes):
        while True:
            isPrime = True
            for n in range(2, currentNum):
                #if number is divisible
                if (currentNum % n == 0):
                    currentNum = currentNum + 1
                    isPrime = False
                    break
            
            if (isPrime):
                list.append(currentNum)
                currentNum = currentNum + 1
                break

    return list
