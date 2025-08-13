# return = statement used to end a function
#          and send a result back to the caller

def add(x, y):
    return x+y

def sub(x, y):
    return x-y

def mul(x, y):
    return x*y

def div(x, y):
    return x/y

print(add(1, 2))
print(sub(1, 2))
print(mul(1, 2))
print(div(1, 2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return f"{first} {last}"

full_name = create_name("Shamiul", "haque")
print(f"Hello, {full_name}")