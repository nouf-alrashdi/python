# Declaration
first_number = 0
second_number = 0
operation = ""
result = 0

# Take Input
first_number = int(input("Please enter the 1st number: ")) # "10" -> 10
second_number = int(input("Please enter the 2nd number: ")) # "20" -> 20
operation = input("Please enter one of + - * or /: ")

# Processing Input
if operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = second_number - first_number
elif operation == "*":
    result = first_number * second_number
elif operation == "/":
    if second_number > 0:
        result = first_number / second_number

# Output
print("Result is: ", result, "!!!")
print("End of Script")