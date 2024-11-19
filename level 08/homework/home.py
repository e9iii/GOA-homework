# 1)

age = int(input("Please enter your age: "))

print(age > 13 and age < 19)

# 2)

score = int(input("Please enter your score: "))

is_A = score >= 9
is_B = score >= 8 and score < 9
is_C = score >= 7 and score < 8
is_D = score >= 6 and score < 7
is_F = score < 6

print(is_A)
print(is_B)
print(is_C)
print(is_D)
print(is_F)

# 3)

print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

# 4)

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)
print(num1 == num2)
print(num1 != num2)

# 5. შექმენით a, b და c ცვლადები და მიანიჭეთ მათ ნებისმიერი მთელი რიცხვი. შექმენით ახალი 3 ცვლადი:
# is_a_greatest: ამ ცვლადში შეინახეთ True, თუ a არის უდიდესი ამ სამიდან.
# is_b_middle: ამ ცვლადში შეინახეთ True თუ b არის საშუალო მნიშვნელობა (არა უდიდესი ან უმცირესი).
# is_c_least: ამ ცვლადში შეინახეთ True, თუ c არის სამიდან უმცირესი.

# 5)
a = 15
b = 20
c = 5

is_a_greatest = a > b and a > c
is_b_middle = b > a and b < c or b < a and b > c
is_c_least = c < a and c < b

print(is_a_greatest)
print(is_b_middle)
print(is_c_least)

# 6)

score = 70

is_pass = score >= 50
is_high_pass = score >= 75 and score < 90
is_perfect = score == 100
is_failing = score < 50

print(is_pass)
print(is_high_pass)
print(is_perfect)
print(is_failing)

# 7)

P = True
Q = False

P_and_not_Q = P == True and Q == False
not_P_and_Q = P == False and Q == False
P_xor_Q = P == True and Q == True