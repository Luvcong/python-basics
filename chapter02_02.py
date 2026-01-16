# Chapter02-2

# 1) 변수
# 기본 선언
n = 700

print(n)
print(type(n))  # n에 담겨있는 값의 type 출력
print('----------')

# 동시 선언
x = y = z = 700
print(x, y, z)
print('----------')

# 재선언 : 마지막에 선언된 값이 덮어씌워짐
var = 75
var = 'Change Value'
print(var)
print(type(var))
print('----------')

# 2) Object References
# 2-1) 변수 값 할당 상태 : type에 맞는 object 생성 -> 값 생성 -> console 출력

# ex1)
print(300)          # (int(300)) 동일
print(int(300))
print('----------')

# ex2)
n = 777
print(n, type(n))
print('----------')

m = n
print(m, n)     # 777 777
print(type(m), type(n))
print('----------')

n = 400
print(m, n)     # 777 400
print(type(m), type(n))
print('----------')

# 2-2) id(identity) 확인 : 객체의 고유 값 확인
m = 800
n = 655
print(id(m))    # 4444430608
print(id(n))    # 4444430704
print(id(m) == id(n))   # False
print('--------')

m = 800
n = 800
print(id(m))    # 4444430608
print(id(n))    # 4444430608
print(id(m) == id(n))   # True
# 같은 오브젝트 참조 : 똑같은 값의 중복 변수를 사용하는 경우 1개의 Object로 생성하여 사용 (최적화)
print('--------')

# 3) 다양한 변수 선언
# Camel Case  :  numberOfCollegeGraduates
# Pascal Case :  NumberOfCollegeGraduates
# Snake Case  :  number_of_college_graduates


# 예약어는 변수명으로 불가능