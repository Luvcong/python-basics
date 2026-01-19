# Chapter05-1
# 함수식 및 람다(Lambda)

# 5-1) 함수식
# ex 1
def fisrt_func(a) :
    print('hello, ', a)

word = 'python'
fisrt_func(word)

# ex 2)
def return_func(a) :
    return 'hello, ' + str(a)

x = return_func('python')

print(x)
print('----------')

# ex 3) 다중 반환
def func_mul(x) :
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3
x, y, z = func_mul(10)

print(x, y, z)
print('----------')

# 튜플 반환
def func_mul2(x) :
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)
q = func_mul2(10)
print(type(q), q)
print('----------')

# 리스트 반환
def func_mul3(x) :
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]
p = func_mul3(10)
print(type(p), p)
print('----------')

# 딕셔너리 반환
def func_mul4(x) :
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1' : y1, 'v2' : y2, 'v3' : y3}

d = func_mul4(30)
print(type(d), d, d.get(''), d.items(), d.keys()) 
print('----------')

# 중요 **
# *args (튜플 자료형에서 사용)
# **kwarge (교집합 자료형에서 사용)

# *args (unpacking)
def args_func(*args) :
    for i, v in enumerate(args) :
        print('Result : {}'.format(i), v)
    print('-----')

# 가변적으로 매개변수 사용 가능
args_func('Lee')
args_func('Lee', 'Park')
args_func('Lee', 'Park', 'Kim')

# **Kwargs(unpacking)
def kwargs_func(**kwargs) :
    for val in kwargs.keys() :
        print('{}'.format(val), kwargs[val])
    print('-----')

kwargs_func(name1='Lee')
kwargs_func(name1='Lee', name2='Park')
kwargs_func(name1='Lee', name2='Park', name3='Cho')

# 전체 혼합
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)
print('----------')

example(10, 20, 'Lee', 'Kim', 'Park', age1 = 20, age2 = 30, age3 = 40)

# 중첩 함수
def nested_func(num):
    def func_in_func(num):
        print(num)
    print("In func")
    func_in_func(num + 100)

nested_func(100)
print('----------')

# 실행불가 (정의되지 않은 함수)
# func_in_func(1000)

# 5-2) 람다식
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리)할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화
# 람다식을 남발하는 경우 오히려 가독성이 감소
"""
def mul_func(x, y) :
    return x * y
"""

# 일반적 함수
def mul_func(x, y) :
    return x * y

# 람다식 함수
lambda x, y : x * y

# 일반적 함수 -> 할당
def mul_func2(x, y) :
    return x * y
mul_func_var = mul_func2
print(mul_func_var(5, 10))
print(mul_func2(5, 10))
print('----------')

# 람다 함수 -> 할당
lambda_mul_func = lambda x, y : x * y
print(lambda_mul_func(5, 10))
print('----------')

# 함수를 인자로 받을 때 람다식 사용을 많이 함
def func_final(x, y, func):
    print('>>>> ', x * y * func(100, 100))

func_final(10, 20, lambda_mul_func)
print('----------')

# Hint 1)
# word   : 매개변수가 문자열이어야 함
# num    : 매개변수가 정수여야 함
# -> int : 반환 값은 정수
def tot_length1(word: str, num: int) -> int:
    return len(word) * num

print('hint exam1 : ', tot_length1("i love you", 10))

# Hint 2)
# -> None : 반환 값 없음
def tot_length2(word: str, num: int) -> None:
    print('hint exam2 : ', len(word) * num)

tot_length2("niceman", 10)