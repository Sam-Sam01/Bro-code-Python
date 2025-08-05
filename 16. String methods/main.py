# Here we will learn about string methods

name = input("Enter your full name: ")
phn_num = input("Enter your phone number: ")

res = len(name)
print(res)

#In Python, the find() method is primarily used with strings to locate the starting index of the first occurrence of a specified substring within another string. 
# If not found it returns -1
first_ocarence = name.find(" ")
print(first_ocarence)

#The str.rfind() method in Python is used to find the last occurrence of a specified substring within a string. It returns the highest index in the string where the substring is found. If the substring is not found, it returns -1.
last_ocarence = name.rfind("a")
print(last_ocarence)

cap_name = name.capitalize()
print(cap_name)

upper_name = name.upper()
print(upper_name)

lower_name = name.lower()
print(lower_name)

title_name = name.title()
print(title_name)

#The isdigit() method in Python is a built-in string method used to determine if all characters within a string are digits. 
res_digit = name.isdigit()
print(res_digit)

#The isalpha() method in Python is a built-in string method used to check if all characters within a string are alphabetic. It returns True if all characters in the string are letters (a-z, A-Z) and there is at least one character in the string; otherwise, it returns False.
res_alpha = name.isalpha()
print(res_alpha)

res_dash = phn_num.count("-")
print(res_dash)

phn_num = phn_num.replace("-", "")
print(phn_num)