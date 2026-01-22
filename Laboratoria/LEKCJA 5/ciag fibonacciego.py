def fibonacci(limit):
    a = 0
    b = 1

    for x in range(limit):
        yield a
        a, b = b, a+b

for i in fibonacci(10):
    print (i)