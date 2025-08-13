# *args = allows you to pass multiple non-key arguments
# *kwargs = allows you to pass multiple keyword-arguments
#           *unpacking operator

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1,2,3,4,5,6))

#args is a tuple
def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Dr.", "Shamiul", "Haque", "||")

print()

#kwargs is a dictionary
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="368 Fake st.", city="Mirpur", state="USM", zip="6300")