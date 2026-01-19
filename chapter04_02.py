# Chapter04-2
# 2) 반복문 (for)
"""
for i in <collection>
    <loop body>
"""

# range : 0부터 시작
for v1 in range(10) :
    print('v1 is. : ', v1)  # 0 ~ 9까지 출력

for v2 in range(1, 11) :    
    print('v2 is : ', v2)   # 1 ~ 10까지 출력

for v3 in range(1, 11, 2) :
    print('v3 is : ', v3)   # 1, 3, 5, 7, 9
print('----------')

# 1 ~ 1000까지의 합
total = 0
for num in range(1, 10) :
    total += num
print('total : ', total)

# sum() 함수를 사용해서 반복문을 사용하지 않고 바로 계산 가능
print('total : ', sum(range(1, 1001)))  # sum(리스트) => range가 내부적으로 리스트로 반환
print('4의 배수의 합 : ', sum(range(4, 1001, 4)))
print('----------')

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# ex 1)
names = ["Kim", "Park", "Cho", "Lee", "Choi", "Yoo"]
for name in names :
    print('You are name : ', name)

# ex 2)
lotto_numbers = [11, 19, 21, 32, 15, 33]
for number in lotto_numbers : 
    print('Currnet Numner : ', number)

# ex 3)
word = 'Beautiful'
for text in word : 
    print('word : ', text)

# ex 4)
my_info = {
    "name" : "Lee",
    "Age"  : 33,
    "City" : "Seoul"
}
for key in my_info :
    print(key, ":", my_info[key])
    print(key, ":", my_info.get(key))

for val in my_info.values():
    print('val : ', val)

# ex 5)
# isupper() : 대문자 체크 / upper() : 대문자로 변경
# islower() : 소문자 체크 / lower() : 소문자로 변경
name = 'FineApplE'
for n in name : 
    if n.isupper() :
        print(n)
    else :
        print(n.upper())
print('----------')

# 2-1) break : 불필요한 반복을 줄이기 위해 사용
# 조건을 만족하는 값이 나오면 반복문 종료
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for num in numbers :
    if num == 34 :
        print('Found 34')
        break
    else :
        print('Not Found 34 : ', num)
print('----------')

# 2-2) continue : 조건을 만족하는 값이 나오면 반복문을 실행하지 않고, 다음 반복문 실행
lt = ["1", 2, 5, True, 4.3, complex(4)]
for val in lt :
    if type(val) is bool :
        continue
    print('current Type : ', type(val))
print('----------')

"""
current Type :  <class 'str'>
current Type :  <class 'int'>
current Type :  <class 'int'>
current Type :  <class 'float'>
current Type :  <class 'complex'>

=> 'bool'은 출력되지 않았음
"""

# 2-3) for - else 구문
# 반복문 중간에 종료되지 않았을 경우에만 else 구문 실행됨
# (= 끝까지 확인했지만 만족하는 값이 없을때만 else 구문 실행)
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for number in numbers :
    if number == 11 :
        print('Found 11')
        break
else :
    print('Not Found 11...')
print('----------')

# 2-4) 구구단
for num1 in range(1, 10) :
    for num2 in range(1, 10) :
        print(f"{num1} X {num2} = {num1 * num2}")
print('----------')

# 변환 실습
name2 = 'Aceman'
print('Reversed : ', reversed(name2))       # <reversed object at 0x109c04f70>
print('List : ', list(reversed(name2)))     # ['n', 'a', 'm', 'e', 'c', 'A']
print('Tuple : ', tuple(reversed(name2)))   # ('n', 'a', 'm', 'e', 'c', 'A')
print('Set : ', set(reversed(name2)))       # {'m', 'c', 'a', 'e', 'A', 'n'}
