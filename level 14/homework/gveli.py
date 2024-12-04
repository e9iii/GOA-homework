# name = input("enter your name: ")
# res = " ".join(name)
# print("Result:", res)

# number = int(input("enter number: "))
# if number % 2 == 0:
#     print(f"{number}:even")
# else:
#     print(f"{number}:odd")

# number = float(input("enter number: "))
# if number > 0:
#     print(f"{number}: is positive")
# elif number < 0:
#     print(f"{number}: is negative")
# else: 
#     print(f"{number}: is zero")
    
# number1 = float(input("enter number: "))
# number2 = float(input("enter number: "))
# if number1 == number2:
#     print(f"{number1} and {number2}: equal")
# else:
#     print(f"{number1} and {number2} is not equal")

# number = float(input("enter number: "))
# if number > 100 and number % 2 == 0:
#     print(f"{number}: 100-ზე მეტია და არის ლუწი")
# else:
#     print(f"{number}: არ არის 100-ზე მეტი ან ლუწი")

number = int(input("enter number: "))
if number % 5 == 0 or number % 10 == 0:
    print(f"{number} is divisible by 5 or 10.")
else:
    print(f"{number} is not divisible by 5 or 10.")