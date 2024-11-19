# 1) (1, 50 , 2) დარინტეთ რაც გინდათ! while/for
# 2) კვადრატი დავხაზოთ "*",  for/while
# 3) მართკუთხედი დავხაზე "*", for/while
# 4) for loop ( საიტერაციო ცვლადს დაარქვით num1 ) გამოვიყენოთ და შიგნით ჩავაშენოთ(შიგნიშთ კიდევ შევქმანთ) for loop (საიტერაციო ცვლადს დაარქვით num)  და დაპრიმტეთ მეორე ლუპში ორივე, საიტერაციო ცვლადის მნიშნვნელობა
# 5) difculty porject ( შექმნით, სარეგისტრაციო ფორმა ჩვენი, სოციალური ქსელისთვის <3 input, while, loop )
# for i in range(1,51,2):
#     print(i)
# i = 1
# while i <= 50:
#     print(i)
# #     i += 2
# size = 5
# for i in range(size):
#     print('*' * size)
# size = 5
# i = 0
# while i < size:
#     print('*' * size)
#     i += 1
# size = 5
# for i in range(size):
#     print('*' * size)
# size = 5
# i = 0
# while i < size:
#     print('*' * size)
#     i += 1
# for num1 in range(1,4):
#     for num in range(1,4):
#         print(f"num1: {num1}, num: {num}")

name = input("enter your name: ")
lastname = input("enter your lastname not necessary: ")
mail = input("enter your mail: ")
age = int(input("enter your age: "))
print(f"Name: {name}, LastName: {lastname}, Mail: {mail}, Age: {age}")
if age >= 18 :
    print("you are adult😎")
else:
    print("you are kid 🤣")