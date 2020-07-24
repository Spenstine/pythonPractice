def mult(x, y):
    counter_x = len(str(x))
    counter_y = len(str(y))
    if counter_y > counter_x:
        n = counter_y
    else:
        n = counter_x
    n_over_two = int(n/2)
    whole_n = n_over_two * 2
    if n == 1:
        return x * y
    else:
        a = x // 10**(n_over_two)
        b = x % 10**(n_over_two)
        c = y // 10**(n_over_two)
        d = y % 10**(n_over_two)
        return 10**whole_n * mult(a, c) + mult(b, d) + 10**(n_over_two) * (mult((a + b), (c + d)) - mult(a, c) - mult(b, d))

x = int(input("x: "))
y = int(input("y: "))
print("formula:  ", mult(x, y), end= "   ")
print("actual:  ", x * y)
if mult(x, y) == x * y:
    print(True)
