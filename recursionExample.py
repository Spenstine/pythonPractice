def do_n(f, n):
    if n <= 0:
        return
    f(n)
    do_n(f, n - 1)

def print_sipe(n):
    print("sipe:  ", n)

do_n(print_sipe, 4)