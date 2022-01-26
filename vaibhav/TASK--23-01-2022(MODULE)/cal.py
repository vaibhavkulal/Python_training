import calculatons
def swtich():
    print("1->Addition\n2->subtraction\n3->FIND age\n4->Multiplication\n5->Division\n6->SIMPLE INTEREST\n7->leap year\n8->division(useing Exception")
    option=int(input("enter your choice"))

    if option==1:
        #Enter two numbers for additions
        print("Enter two numbers for additions")
        a=int(input("Enter the number \n"))
        b=int(input("Enter the number \n"))
        print("Sum of ",a,"and",b,"is",calculatons.add(a,b))
    elif option==2:
        #Enter two numbers for subtraction
        print("Enter two numbers for subtractions")
        a=int(input("Enter the number\n"))
        b=int(input("Enter the number\n"))
        print("Differnce of ",a,"and",b,"is",calculatons.sub(a,b))
    elif option==3:
        #ENTER THE PRESENT DATE
        print("FIND AGE")
        present_date =int(input("enter present DATE\n"))
        present_month =int(input("enter present MONTH\n"))
        present_year =int(input("enter present YEAR\n"))
        #ENTER YOUR BIRTH DATE/MONTH/YEAR
        birth_date = int(input("Enter the birth DATE\n"))
        birth_month =int(input("Enter the birth MONTH\n"))
        birth_year = int(input("Enter the birth YEAR\n"))
        calculatons.Age(present_date, present_month, present_year, birth_date, birth_month, birth_year)
    elif option==4:
        #Enter two numbers for Multiplication
        print("Enter two numbers for Multiplication")
        a=int(input("Enter the number\n"))
        b=int(input("Enter the number\n"))
        print("Product of ",a,"and",b,"is",calculatons.mul(a,b))
    elif option==5:
        #division
        print("Enter two numbers for divison")
        a=int(input("Enter the number\n"))
        b=int(input("Enter the number\n"))
        print("Quotitent of ",a,"and",b,"is",calculatons.div(a,b))
    elif option==6:
        #SIMPLE INTEREST
        print("SIMPLE INTEREST")
        p=int(input("Enter the amount\n"))
        r=float(input("Enter the rate of interest\n"))
        t=int(input("Enter the year\n"))
        print("Simple interest for",p,"is",calculatons.si(p,r,t))
    elif option==7:
        #Leapyear
        print("LRAP YEAR")
        year=int(input("enter the year\n"))
        calculatons.ye(year)
     elif option==8:
        a = int(input("enter the number\n"))
        b = int(input("enter thye number\n"))
     try:
       print(div.d(a,b))
     except Exception as e:
       print("Exception:-",e)
    else:
        print("Incorrect Selection")
swtich()
