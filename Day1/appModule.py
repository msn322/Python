fill_list = []
for x in range(1,101):
    fill_list.append(x)

print(fill_list)

sec_list = list(range(1,10))
print(sec_list)

third_list = {"one":"1","two":"2"}
print(third_list)


total = 0
for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
        total += i
print(total)