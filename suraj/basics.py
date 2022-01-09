# # Basic output function
# print("Hello World Python is awesome!!!!")

# # input function example to calculate age
# birth_year = input("Birth year : ")
# print(2022-int(birth_year))

# # String and String methods
# string="Python is awesome!!!"
# print(string[0:6])

# # Formatted string
# fname = 'John'
# lname = 'smith'
# message = fname + ' [' + lname +'] is a coder'
# print(message)
# msg=f'{fname} [{lname}] is a coder'
# print(msg)


# # conditional operators

# price = 1000000
# has_good_credit = False
# if has_good_credit :
#     down_payment = 0.1 * price
# else :
#     down_payment = 0.2 * price
# print(f"Down payment : {down_payment}")

# # logical operators

# # Excersize : Applicable for loan
# has_good_credit = True
# has_creminal_record = False
# if has_good_credit and not has_creminal_record :
#     print("Eligible for the load")
# else :
#     print("Not eligible for the loan")

# # Excersize : Good Bad name
# name = input("Enter your name : ")
# if len(name) < 3 :
#     print("Name must contains aleast 3 characters")
# elif len(name) > 10 :
#     print("Name can be maximum of 50 characters")
# else :
#     print("Name looks good !!!")

# # Excersize : Kilo Pound Convertor
# weight = int(input("Enter weight : "))
# unit = input("(L)bs or (K)g : ")
# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f"{converted} kilos")
# elif unit.upper() == "K" :
#     converted = weight/0.45
#     print(f"{converted} pounds")
# else :
#     print("Choose correct unit")

# # Excersize : Car Game 
# command = ""
# while True :
#     command = input(">").


# Dictionary
# dict = {
#     "fname":"Suraj",
#     "minitial":"S",
#     "lname" : "Savant",
#     "phone" : 1234,
# }




# #Excersize : Convert number as strings
# phone = input("Enter the number : ")
# phone_map ={
#     '1' : 'One',
#     '2' : 'Two',
#     '3' : 'Three',
#     '4' : 'Four'
# }
# to_string = ""
# for ph in phone :
#     to_string += phone_map.get(ph, '!') + " "
# print(to_string)

# # Excersize : Convert imojies
# input_msg = input("Enter msg > ")
# emoji_map = {
#     ":)" : "😂",
#     ":(" : "😒",
# }
# words = input_msg.split(" ")
# output_msg=""
# for word in words :
#     output_msg += emoji_map.get(word, word) + " "
# print(output_msg)













