#module = A file containing code you want to include in your program use 'import' to include a
#         module (built-in or your own) useful to break up a large program reusable separate files

#print(help('modules'))

#import math {importing module}
#import math as m {import module as m}
#from math import e {only importing one data}

import example

result_pi = example.pi
result_square = example.square(4)
result_cube = example.cube(5)
result_circumference = example.circumference_of_circle(7)
result_area = example.area_of_circle(7)

print(result_pi)
print(result_square)
print(result_cube)
print(result_circumference)