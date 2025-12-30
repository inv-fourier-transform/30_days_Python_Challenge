def generate_fib(n:int):
    a=0
    b=1
    count=0

    while True:
        if count == n:
            return
        yield a
        a,b = b, a+b
        count +=1

def generate_fib_alt(n:int):

    a=0
    b=1

    for i in range(n):
        yield a
        a,b = b, a+b


if __name__  == "__main__":
    generator_obj = generate_fib(4)
    for i in generator_obj:
        print(i)
    print("*********************")
    generator_obj2 = generate_fib_alt(5)
    for j in generator_obj2:
        print(j)

