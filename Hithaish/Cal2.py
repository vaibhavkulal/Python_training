num_1 =input("Insert a number: ")

operation= input('''

Select the operation:

+ for addition

- for substract

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
