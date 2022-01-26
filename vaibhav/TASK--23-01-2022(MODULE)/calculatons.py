def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def Age(present_date, present_month, present_year,birth_date,birth_month, birth_year):

    calculated_date = abs(present_date - birth_date)
    calculated_month = abs(present_month - birth_month)
    calculated_year = present_year - birth_year
    print("\t\tPresent Age")
    print("Your exact age is: ",calculated_year," Years",calculated_month,"months and",calculated_date,"days")

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def si(p,r,t):
    return (p*r*t)/100

def ye(year):
    if year%4==0 and year%100!=0:
        print(year," is a leap year")
    elif year%100==0:
        print(year, " is not leap year")
    elif year%400==0:

        print(year, " is a leap year")
    else:
        print(year," is not leap year")