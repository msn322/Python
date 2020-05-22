employer_file_2 = open("exployee.txt", "r")
employer_file_2.close()


employee_file = open("exployee.txt", "a")
employee_file.write("Toby - HR")

#for emp in employee_file.readlines():
#    print(emp)

employee_file.close()