# Operator and Operator Precedence :

# Types of operator in python:
# 1. Arithmetic Operator : +(unary), +(binary), -(unary), -(binary), /, *, %, //, **.
a, b = 123, 20
print(+a)
print(-b)
print(a + b)
print(a - b)
print(a / b)
print(a * b)
print(a % b)
print(a//b)
print(a**b)
print("\n\n")
# 2. Assignment Operator : =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=.
c = 25
a += 1
print(a)
c -= b
print(c)
a *= 2
print(a)
a /= 3
print(a)
b %= c
print(b)
a //= 2
print(a)
b **= 3
print(b)
b ^= 3
print(b)
c >>= 6
print(c)
b <<= 4
print(b)
print("\n\n")
# 3. Bitwise Operator : & | ^ ~ << >>
a = 15
b = 4
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << b)
print(a >> b)
print("\n\n")
# 4. Comparison Operator : ==, !=, <, >, <=, >=.
print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)
print("\n\n")
# 5. Logical operator : and, or, not.
a = True
b = False
print(a and b)
print(a or b)
print(not b)
print("\n\n")
# 6. Identity Operator : is, is not.
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1, 2, 3]
y3 = [1, 2, 3]
print(x1 is not y1)
print(x2 is y2)
print(x3 is y3)
print(id(y3), "and", id(x3))
print("\n\n")
# 7. Membership operator : in, not in
x = 'Hello world'
y = {1: 'a', 2: 'b'}
print('H' in x)
print('hello' not in x)
print(1 in y)
print('a' in y)


# Operator Precedence :
#      ()           **      +, -, ~     *,/,//,%,+-     <<, >>, &, ^, |     ==, !=, >, >=, <, <=    is, is not
# parenthesis      expo     unary       arithmetic          bitwise                comparison       identity
#      in, not in       not, and, or
#      membership          logical
