# Chapter03-1
# 1) 숫자형

# 1-1) python 자료형
"""
- int     : 정수
- float   : 실수
- complex : 복소수
- bool    : 불린
- int     : 정수
- str     : 문자열 (시퀀스)
- list    : 리스트 (시퀀스)
- tuple   : 튜플   (시퀀스)
- set     : 집합
- dict    : 사전
"""

# 1-2) 데이터 타입
str1  = "python"
str2  = 'Anaconda'
bool  = True
# float = 10.0
# int   = 7
list  = [str1, str2] # ['python', 'Anaconda']
dict  = {
    'name'    : 'Machine Learning',
    'version' : 2.0
}
tuple = (7, 8, 9)   # tuple = 7, 8, 9 와 동일
set   = {7, 8, 9}

# 데이터 타입 출력
print(type(str1))
print(type(str2))
print(type(bool))
# print(type(float))
# print(type(int))
print(type(dict))
print(type(tuple))
print(type(set))
print('----------')

# 1-3) 숫자형 연산자
"""
- +
- -
- *
- /
- // : 몫 반환
- %  : 나머지 반환
- abs(x) : 절대값 반환
- pow(x, y) : x에 y제곱 계산 => x ** y 와 동일
- int(x)
- float(x)
- complex(x) : 복소수값 반환
"""

# 1-4) 형 변환
a = 3.  # 3.0 과 동일 (소수점 뒤 0 생략 가능)
b = 6
c = .7
d = 12.7

print(type(a), type(b), type(c), type(d))
print('----------')

print(float(b))        # 정수 -> 실수 (6.0)
print(int(c))          # 실수 -> 정수 (0)
print(int(True))       # bool -> 정수
print(int(False))      # bool -> 정수
print(complex(3))      # 정수 -> 복소수
print(complex('3'))    # 문자 -> 복소수
print(complex(False))  # Bool -> 복소수
print('----------')

# 1-5) 수치 연산 함수
print(abs(-7))

x, y = divmod(100, 8)   # divmod : 몫과 나머지 출력
print(x, y)

print(pow(5, 3), 5 ** 3)

# 1-6) 외부 모듈
import math

print(math.pi)  # 원주율
print(math.ceil(5.1))   # x 이상의 수 중에서 가장 작은 정수 값 반환