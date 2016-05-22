# prints fib numbers up to max set
max = 10000000

def fib(f1, f2):
    fib = f1 + f2
    while fib < max:
        fib = f1 + f2
        f1 = f2
        f2 = fib
        print("fib = ", fib)
        # print("f1 = ", f1)
        # print("f2 = ", f2)
fib(0, 1)

print('******************')

# returns the Xth fib num, up to max2 set
max2 = 2
def F(n):
    if n < 2:
        newfib = n
        print('top n = ', newfib, '\n******************')
        return newfib
    else:
        print('bot n - 2 = ', F(n-2))
        print('bot n - 1 = ', F(n-1), '\n******************')
        newfib = F(n-2) + F(n-1)
        return newfib
print('FIB = ', F(max2))

