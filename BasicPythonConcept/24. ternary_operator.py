number1, number2 = map(int, input().strip().split())
minimum_number = number1 if number1 < number2 else number2
print(minimum_number)
