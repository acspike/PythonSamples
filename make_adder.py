def make_adder(num):
    def adder(x):
        return x + num
    return adder

def call_with_4(f):
    return f(4)

def my_print(x):
    print x

add2 = make_adder(2)
add4 = make_adder(4)

print call_with_4(add2)
print call_with_4(add4)
call_with_4(my_print)
