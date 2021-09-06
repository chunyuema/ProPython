def fibonnaciGenerator(num):
    a, b, cntr = 0, 1, 0
    while True:
        if cntr > num:
            return
        else:
            yield a
            a, b = b, a+b
            cntr += 1


fib = fibonnaciGenerator(5)
print(type(fib))  # <class 'generator'>
for res in fib:
    print(res)
