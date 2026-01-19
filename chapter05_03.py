# Chapter05-2
# Input 사용법

# 1) 기본 타입 (str)
# ex 1)
name = input('Enter Your Name : ')
grade = input('Enter Your Grade : ')
company = input('Enter Your Company name : ')

print(name, grade, company)

# # ex 2)
number = input('Enter number : ')
print('type of number : ', type(number))    # 숫자를 입력해도 Input의 기본 타입은 str !

# ex 3)
first_number = int(input('Enter number 1 : '))
second_number = int(input('Enter number 2 : '))
total = first_number * second_number
print('first * second = ', total)

# ex 4)
float_number = float(input('Enter a float number : '))

print('input float : ', float_number)
print('input type : ', type(float_number))

# ex 5)
print('FirstName - {0}, LastName - {1}'.format(input('Enter first name : '), input('Enter Last name : ')))