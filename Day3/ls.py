import os

for root, dirs, files in os.walk("."):
    for filename in files:
        print(filename)
    print(dirs)

# define string
string = "Python is awesome, isn't it?"
substring = "is"

count = string.count(substring)

# print count
print("The count is:", count)