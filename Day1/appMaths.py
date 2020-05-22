given_list = [ 4, 5, 8, 0]

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        print("We reached this far")
        return num1
    elif num2 >= num1 and num2 >= num3:
        print("Num2 is a Major")
        return num2
    else:
        print("Num3 is a score")
        return num3

print(max_num(2,5,7))
