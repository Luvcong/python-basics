# Chapter05-0
# 함수
# : 프로그래머가 이름을 통해서 정의 후 필요할 때 마다 호출
# : 반복 되는 코드를 한 번 구현 후 재사용 가능한 코드의 집합
# : 함수 구현 -> 재사용, 루틴(프로시저, 서브루틴)
"""
def function_name(parameter):
    code
"""

# https://www.kodable.com/learn/kids-learn-with-functions

# 종류
# 1. 매개변수가 필요한 함수
# 2. 매개변수가 필요하지 않은 함수
# 3. 결과값을 반환하는 함수(return)
# 4. 결과값을 반환하지 않는 함수

# ex 1) 매개변수가 필요한 함수
def function1(a, b) :
    print("ex1 호출", a, b)

# ex 2) 매개변수가 필요없는 함수
def function2():
    print('ex2 호출')

# ex 3) 결과값 반환 X 함수
def function3(a, b) :
    print('ex3 호출', a, b)

# ex 4) 결과값 반환 O 함수
def function4(a, b) :
    return a + b

# 함수 실행
function1(1, 2)
function2()
function3(1, 2)
function4(1, 2)

result = function4(50, 2)
print('ex4 호출', result)
print('ex4 호출', function4(50, 2))