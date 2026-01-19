# Chapter03-4
# 4) 튜플(Tuple)
# : 튜플 자료형 특징 (순서 존재 / 중복 존재 / 수정 불가 / 삭제 불가) => 불변

# 4-1) 선언
a = ()
b = (1,)    # 원소 1개를 선언할때는 끝이 , 로 끝나야 함
c = (11, 12, 13, 14)
d = (100, 1000,'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

# 4-2) 인덱싱
# : 리스트와 동일하게 인덱싱 가능

# 튜플 -> 리스트 변환 가능
print('e : ', type(list(e)))
print('----------')


# 4-3) 수정 (불가)
# d[0] = 1500
# print('d : ', d)

# 4-4) 슬라이싱
#  : 리스트와 동일하게 슬라이싱 가능

# 4-5) 튜플 연산
print('c + d : ', c + d)
print('c * 3 : ', c * 3)
print('----------')

# 4-6) 튜플 함수
a = (5, 2, 3, 1, 4)
print('a : ', a)
print(a.index(3))
print(a.count(2))

#  ** 4-7) 팩킹 & 언팩킹 (Packing & Unpacking)
# 팩킹
t = ('foo', 'bar', 'baz', 'qux')
print(t)
print(t[0])
print(t[-1])

# 언팩킹(1) : 하나의 패키지로 되어있는 값을 풀어서 각 원소에 대입
(x1, x2, x3, x4) = t
print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

# 팩킹 & 언팩킹
t2 = 1, 2, 3 # () 없이 선언해도 튜플
t3 = 4,

x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

print(t2)   # (1, 2, 3)
print(t3)   # (4,)
print(x1, x2, x3)   # 1, 2, 3
print(x4, x5, x6)   # 4, 5, 6