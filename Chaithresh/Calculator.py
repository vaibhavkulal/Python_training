num_1 =input("Insert a number: ")
operation= input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

num_2=input("Insert a number: ")
if operation == "+": 
    print('{} + {} = '.format(num_1, num_2))
    print(str(int(num_1) +int(num_2)))

elif operation == "-":
    print('{} - {} = '.format(num_1, num_2))
    print(str(int(num_1) -int(num_2)))

elif operation == "*":
    print('{} * {} = '.format(num_1, num_2))
    print(str(int(num_1) *int(num_2)))

elif operation == "/":
    print('{} / {} = '.format(num_1, num_2))
    print(str(int(num_1) /int(num_2)))

else:
    print('You have not typed a valid operator')
