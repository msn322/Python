friends = ["Jim", "Karen", "Bishop"]
len(friends)

for index in range(len(friends)):
    print(friends[index])
    print(index)

for friend in friends:
    print(friend)

for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("Not first")

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3,2))


