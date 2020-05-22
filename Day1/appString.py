# Variables storing Number, Stri
from math import *

my_num = -5
print(ceil(3.7))

print(abs(my_num))
print(pow(2,3))
print(round(3.7))


my_list = [1,4,2,4,5]
my_bool = False
my_string = "Girrafe\nAcademy"
my_dict = { "Mano": 7, "Ranoo": 3, "Sakht": 15 }

print(my_string.upper().isupper())
print(my_string.isupper())
print(len(my_string))
print(my_string[0])
print(my_string.index("Gir"))

name = input("Enter some value Choduu: ")
number = input("Enter a number: ")
print(number)
print(name + " Thanks for writing")

is_even = False
is_number = False
is_changed = False

if is_even and is_number:
    print("Yes we have even number")
else:
    print("Number is odd")