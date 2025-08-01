''' Typecasting = the process  of convrting a variable from one data type to another.
str(), int(), float(), bool() '''

name = "Shamiul Haque"
age = 23
gpa = 3.33
is_student = True

print(type(name))
print(type(age))
print(type(gpa)) 
print(type(is_student))

# type cast start here

age = str(age)
print(age)
print(type(age))

gpa = int(gpa)
print(gpa)
print(type(gpa))