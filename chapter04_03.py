# Chapter04-3
# 3) 반복문 (while)
#  : 조건을 만족하는 동안 계속 반복문 실행
"""
while <expr>:
    <statement(s)>
"""

# ex 1)
n = 5
while n > 0 :   # while True 인 경우 조건 상관 없이 무조건 반복문 실행
    n = n - 1
    print(n)
print('----------')

# ex 2)
a = ['foo', 'bar', 'baz']
while a :
    print(a.pop())

# ex 3)
n = 5
while n > 0 :
    n -= 1
    if n == 2 :
        break
    print(n)
print('Loop Ended')

# ex 4)
m = 5
while m > 0 :
    m -= 1
    if m == 2 :
        continue
    print(m)
print('Loop Ended')
print('----------')

# ex 5)
i = 1
while i <= 10 :
    print('i : ',i)
    if i == 6:
        break
    i += 1
print('----------')

# 3-1) while-else 구문
n = 10
while n > 0 :
    n -= 1
    print(n)
    if n == 5 :
        break
else :
    print('else out')
print('----------')

# ex 6)
a = ['foo', 'bar', 'baz', 'qux']
s = 'kim'
i = 0

while i < len(a) :
    if a[i] == s :
        break
    i += 1
else:
    print(s, 'not found in list.')
print('----------')

# ex 7)
a = ['foo', 'bar', 'baz']
while True :
    if not a :
        break
    print(a.pop())