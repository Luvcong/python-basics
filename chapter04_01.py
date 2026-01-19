# Chapter04-1
# 1) 제어문 (if)

# 4-1) 기본 형식
print(type(True))
print(type(False))
print('----------')

# ex 1)
if True :
    print('python')

if False : 
    print('hello')
print('----------')

# ex 2)
if False :
    print('bad !')  # false이기 떄문에 실행되지 않음
else :
    print('good !')
print('----------')

# 4-2) 관계연산자 종류
# >, >=, <, <=, ==, !=
x = 15
y = 10

print(x == y)   # False
print(x != y)   # True
print(x > y)    # True
print(x < y)    # False
print(x <= y)   # False
print('----------')

# 4-3) 참, 거짓 판별 종류
city = ''
if city :
    print('You are in : ', city)
else :
    print('Plz enter your city')
print('----------')

city2 = 'Seoul'
if city2 :
    print('You are in : ', city2)
else :
    print('Plz enter your city')
print('----------')

# 4-4) 논리연산자 **
# and, or, not
# https://www.tutorialspoint.com/python/python_operators.htm

a = 75
b = 40
c = 10

print('and : ', a > b and b > c)  # True : a > b > c
print('or  : ', a > b or b > c)   # True
print('not : ', not a > b)        # False
print('not : ', not b > c)        # False
print(not True)     # False
print(not False)    # True
print('----------')

# 4-5) 산술, 관계, 논리 우선순위
print('e1 : ', 3 + 12 > 7 + 3)                  # True
print('e2 : ', 5 + 10 * 3 > 7 + 3 * 20)         # False
print('e3 : ', 5 + 10 > 3 and 7 + 3 == 10)      # True
print('e4 : ', 5 + 10 > 0 and not 7 + 3 == 10)  # False
print('----------')

score1 = 90
socre2 = 'A'

if score1 >= 90 and socre2 == 'A' :
    print('Pass')
else :
    print('Fail')
print('----------')

# ex 3)
id1 = "vip"
id2 = "admin"
grade = 'platinum'

if id1 == 'vip' or id2 == 'admin' :
    print('관리자 인증')

if id2 == 'admin' and grade == 'platinum' : 
    print('최상위 관리자')
print('----------')

# 4-6) if-elif : 다중 조건문
num = 77

if num >= 90 :
    print('Grade : A')
elif num >= 80 :
    print('Grade : B')
elif num >= 70 :
    print('Grade : C')
else:
    print('과락')
print('----------')

# 4-7) 중첩 조건문
grade = 'A'
total = 95

if grade == 'A' :
    if total >= 90 :
        print("장학금 100%")
    elif total >= 80 :
        print("장학금 80%")
    else:
        print("장학금 70%")
else:
    print("장학금 50%")
print('----------')

# 4-8) in, not in
q = [10, 20, 30]
w = {70, 80, 90, 90}
e = {"name": 'Lee', "city": "Seoul", "grade": "A"}
r = (10, 12, 14)

print(15 in q)      # False
print(90 in w)      # True
print(12 not in r)  # True
print("name")       # key 검색 : True
print("seoul" in e.values())  # value 검색 : False
