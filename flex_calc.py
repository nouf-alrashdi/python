#Declaration
num_count = 10

number_1 = 10
number_2 = 20
number_3 = 30
number_4 = 40
number_5 = 50

# list is a collection of vriables
list_of_numbers = [10 , 20 , 30 , 40 ,50]

#input
for _ in range(3):
user_input = int(input("enter the number:"))
#assuming user gives you an input
list_of_numbers.append(user_input)

#process

#output(result)
print(list_of_numbers[2])

