#keyword arguments = an argument preceded by an identifier helps with readability
#                    order of arguments doesn't matter

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello("Hello", "Mr.", last="Sam", first="Shit")

for x in range(1,11):
    print(x)

print('1', '2', '3', '4', '5', sep= '-')

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phn_num = get_phone(country=+880, area=19, first=763, last=12715)

print(phn_num)