#arguments
def f(number):
    print(number)
n = int(input())
f(n)
#parameters
def f2(name):
    print(name)
f2("Nurali")
#default parameter values
def f3(name = "noname"):
    print(f"Hello, {name}")
f3()
#keyword arguments
def f4(name, phone):
    print(name, phone)
f4(name="Nurali", phone=+77777777777)
#returning
def f5(x, y):
    return x*y
res = f5(3, 6)
print(res)