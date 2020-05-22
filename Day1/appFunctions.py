num1 = 3
num2 = 5
given_list = [ 4, 5, 8, 0]
my_dict = { "Mano": 7, "Ranoo": 3, "Sakht": 15 }



def sum(values):
    print(values)
    name_list = []
    age_list = []


    for name, age in values.items():
        print("My name is " + name + " and Age is " + str(age))

        name_list.append(name)
        age_list.append(age)

    return age_list,name_list

    # my_list = values[0:2]

sec_list, one_list  = sum(my_dict)
print(one_list)
print(sec_list)
print(type(one_list))



