given_list = [5,4,4,3,1,5]

total3 = 0

i = 0
while i < len(given_list) and given_list[i] > 0:
    total3 += given_list[i]
    i += 1

print(total3)

given_list2 = given_list + [-2, 3, -5]

total4 = 0
for element in given_list2:
    if element < 0:
        break
    total4 += element
print(element)

total4_index = 0
for index in range(len(given_list2)):
    if given_list2[index] < 0:
        print(given_list2[index])
        print(index)
        break

a = ["apple", "chiku", "bananas"]
for i in range(len(a)):
    for j in range(i+1):
        print(a[i])


# sum of only negetive numbers
given_list2 = given_list + [-2,-3, -5]
print(given_list2)
total4_neg = 0
for index in range(len(given_list2)):
    if given_list2[index] < 0:
        total4_index += given_list2[index]
print("the value of all negetive = "  + str(total4_index))
