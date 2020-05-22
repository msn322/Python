
try:

    number = int(input("Enter Number please : "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError as error:
    print(error)