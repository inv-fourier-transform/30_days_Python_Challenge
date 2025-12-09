import math

def prime_check(num: int):
    if num < 2:
        return f"{num} is not a prime number"
    if num == 2:
        return f"{num} is the only even prime number"
    if num%2 == 0:
        return f"{num} is not a prime number"

    limit = int(math.sqrt(num))
    for i in range(3, limit+1, 2):
        if num % i == 0:
            return f"{num} is not a prime number"
    return f"{num} is a prime number"

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(prime_check(number))

