'''
Using functions to do a task
without deployment of loops or
any other control structures in
python
N/B: this can be done in any other 
language but I prefer doing it in C

-this is the basis of modular programming
'''
def border():
    print("+ - - - -", end=" ")

def content():
    print("|        ", end=" ")

def end_border():
    print("+", end=" ")
    print("")

def end_content():
    print("|", end=" ")
    print("")

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def draw_2_grid():
    do_twice(border); end_border()
    do_twice(content); end_content()
    do_twice(content); end_content()
    do_twice(content); end_content()
    do_twice(content); end_content()

def draw_4_grid():
    do_four(border); end_border()
    do_four(content); end_content()
    do_four(content); end_content()
    do_four(content); end_content()
    do_four(content); end_content()
print("2 x 2 grid")
print("-"*10); print("-"*10)
do_twice(draw_2_grid); do_twice(border); end_border()
print(""); print("")
print("-"*20)
print(""); print("")
print("4 x 4 grid")
print("-"*10); print("-"*10)
do_four(draw_4_grid); do_four(border); end_border()