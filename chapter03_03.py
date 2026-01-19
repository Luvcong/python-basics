# Chapter03-3
# 3) 리스트(list)
# : 자료구조에서 중요
# : Python은 고정 배열 자료형이 없음 (일반적으로 list가 배열 역할하나 동일하지는 않음)
#   > 외부 모듈을 사용해서 array 등 사용 가능
# : 리스트 자료형 특징 (순서 존재 / 중복 존재 / 수정 가능 / 삭제 가능)

a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, 'Ace', 'Base', 'Caption']
e = [1000, 10000, ['Ace', 'Base', 'Caption']]
f = [21.42, 'foobar', 3, 4, False, 3.14159]

# 3-1) 인덱싱
print('d : ', type(d), d)
print('d : ', d[1])                 # 10000
print('d : ', d[0] + d[1] + d[1])   # 21000   
print('d : ', d[-1])                # Caption
print('e : ', e[-1][1])             # Base
print('e : ', list(e[-1][1]))       # ['B', 'a', 's', 'e']
print('----------')

# 3-2) 슬라이싱
print('d : ', d[0:3])       # [1000, 10000, 'Ace']
print('d : ', d[2:])        # ['Ace', 'Base', 'Caption']
print('e : ', e[-1][1:3])   # ['Base', 'Caption']
print('----------')

# 3-3) 리스트 연산
# : 리스트로 연산하면 리스트로 반환
print('c + d : ', c + d)    # [70, 75, 80, 85, 1000, 10000, 'Ace', 'Base', 'Caption']
print('c * 3 : ', c * 3)    # [70, 75, 80, 85, 70, 75, 80, 85, 70, 75, 80, 85]
# print('Test + c[0] : ', 'Test' + c[0])   # TypeError: can only concatenate str (not "int") to str
print('Test + c[0] : ', 'Test' + str(c[0]))   # Test70
print('----------')

# 3-4) 값 비교
print(c == c[:3] + c[3:])   # True

# id 값 비교
temp = c
print(c == temp)
print(id(c), id(temp))  # 동일 identity
print('----------')

# 3-5) 리스트 수정, 삭제
# 수정
c[0] = 4
print('c : ', c)

c[1:2] = ['a', 'b', 'c']
print('c : ', c)    # [4, 'a', 'b', 'c', 80, 85]

c[1] = ['a', 'b', 'c']
print('c : ', c)    # c :  [4, ['a', 'b', 'c'], 'b', 'c', 80, 85]

c[1:2] = [['a', 'b', 'c']]
print('c :' , c)    # c :  [4, ['a', 'b', 'c'], 'b', 'c', 80, 85]
print('----------')

# 삭제
# 빈 리스트로 선언하기 보다, del을 이용해서 리스트 삭제를 많이 사용
c[1:3] = []         # [4, 'c', 80, 85]
print('c : ', c)

del c[2]
print('c : ', c)    # [4, 'c', 85]
print('----------')

# 3-6) 리스트 함수
a = [5, 2, 3, 1, 4]
print('a : ', a)    

# append(n) : 리스트 뒤에 값 추가
a.append(10)
print('a : ', a)    # [5, 2, 3, 1, 4, 10]

# extend() : 리스트 뒤에 값 추가
# ex = [8, 9]
# a.extend(ex)
# print('a : ', a)

"""
a.append("abc") : 객체 1개의 단위로 값 추가
# [1, 2, 'abc']

a.extend("abc") : 각 요소 단위로 값 추가
# [1, 2, 'a', 'b', 'c']

"""

# sort : 정렬
a.sort()
print('a : ', a)    # [1, 2, 3, 4, 5, 10]

# reverse : 역순 정렬
a.reverse()
print('a : ', a)    # [10, 5, 4, 3, 2, 1]

# index(n) : index값 반환
print('a : ', a.index(3), a[3])

# insert(n) : 위치 지정하여 값 삽입
a.insert(2, 7)
print('a : ', a)    # [10, 5, 7, 4, 3, 2, 1]

# 삭제
# del / remove / pop / clear

# del a[n] : n에 해당하는 index 값 삭제
del a[3]
print('a : ', a)    # [10, 5, 7, 3, 2, 1]

# remove(n) : n과 동일한 값 삭제
a.remove(10)
print('a : ', a)    # [9, 7, 5, 4, 3, 2, 1]

# pop() : 마지막 index에 해당하는 원소를 꺼낸 뒤 리스트 반환
a.pop()
print('a : ', a)    # [9, 7, 5, 4, 3, 2]

# clear() : 모든 값 삭제

# count() : 특정 값 개수 확인
print(a.count(2))   # 1

# 반복문 활용
while a:
    data = a.pop()
    print(data)