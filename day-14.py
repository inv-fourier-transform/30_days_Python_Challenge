def fact(n:int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(fact(n))
