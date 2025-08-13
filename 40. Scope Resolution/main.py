# variable scope = where a variable is visible and accessible
# scope resolution = (LGEB) Local -> Enclosed -> Global -> Built-in

def func1():
    x = 1
    print(x)

def func2():
    x = 2
    print(x)

func1()
func2()

#enclosed
def outer():
    x = 1
    def inner():
        print(x)
    inner()

outer()

#global 
def func3():
    print(x)

def func4():
    print(x)

x = 3
func3()
func4()

#built-in
from math import e 
def func5():
    print(e)

e = 6
func5()