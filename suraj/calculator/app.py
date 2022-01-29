import calculation as cal
arthmetic = {
    '+': cal.add,
    '-': cal.minus,
    '*': cal.multiply,
    '/': cal.division,
    '%': cal.modulus
}

how_to_use = '''
Enter (operator) for operation  : (+) add, (-) minus, (*) multiply, (/) division, (%) modulus, (/q) Exit
OPERATOR > '''
while True:

    operation = input(how_to_use).lower()
    if operation in arthmetic:
        try:
            num1 = int(input("\nEnter first number  > "))
            num2 = int(input("Enter second number > "))
            result = arthmetic.get(operation)(num1, num2)
            print(f"\nRESULT : {num1} {operation} {num2} = {result}")
        except ZeroDivisionError as e:
            print(f"Error : {e}")
        except ValueError as e:
            print(f"ERROR : {e}")

    elif operation == '/q':
        print("\nThanks for using calculator")
        break
    else:
        print("\nERROR : PLEASE CHOOSE CORRECT OPTION")
