# Chapter06-1
# OOP (객체지향 프로그래밍), Self, 인스턴스 메서드, 인스턴스 변수

# class    : 속성(변수)과 동작(메서드)를 정의 / 실제 메모리에 객체가 생성되지는 않음
# obejct   : 메모리에 존재하는 모든 값
# instance : 클래스를 통해 실제로 생성된 객체 / 메모리에 실제로 존재 (각 인스턴스는 자기만의 상태를 갖고 있음)
#   > 특정 클래스에서 생성된 객체
#   > 인스턴스 메서드는 항상 자기 자신을 첫번째 인자로 받음 (slef)

# 네임스페이스  : 객체를 인스턴스화 할 때 저장된 공간을 의미
# 클래스 변수   : 직접 접근 가능, 공유
# 인스턴스 변수 : 객체마다 별도 존재


# ex 1)
# class Dog : (object)를 명시적으로 기재하지 않아도 가능
class Dog(object) :     # object 상속
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age) :
        self.name = name
        self.age = age

# 클래스 정보
print(Dog)

# 인스턴스화
a = Dog('mikky', 2)
b = Dog('baby', 3)

# 비교
print(a == b, id(a), id(b)) # False

# 네임스페이스
# __dict__ : 클래스의 속성들을 확인할 수 있음
print('dog1', a.__dict__)
print('dog2', b.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog' :
    print('{0} is a {1}'.format(a.name, a.age))

print(Dog.species)
print(a.species)
print(b.species)

# ex 2)
# Self
class SelfTest :
    def func1() :       # 클래스 메서드
        print('Func1 called')
    def func2(self) :   # 인스턴스 메서드
        print(id(self))
        print('Func2 called')
print('----------')

f = SelfTest()

# 위에서 만든 func1, func2 함수가 포함되어 있는걸 확인할 수 있음
print(dir(f))

# f.func1() # 예외발생
f.func2()   # 예외가 발생하지 않음 'self' 파라미터 값이 넘어오기 떄문 (인스턴스 메서드)


# 클래스로 바로 접근 
SelfTest.func1()
print('----------')

# ex 3)
# 클래스 변수, 인스턴스 변수
class Warehouse :
    # 클래스 변수
    stock_num = 0 # 재고

    def __init__(self, name) :
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self) :
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Kim')

print(Warehouse.stock_num)

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before : ', Warehouse.__dict__)
print(user1.stock_num)

del user1
print('after : ', Warehouse.__dict__)
print('----------')

# ex 4)
class Dog2(object) :     # object 상속
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def info(self) :
        return '{} is {} years old'.format(self.name, self.age)
    
    def speack(self, sound) :
        return '{} says {} !'.format(self.name, sound)
    
# 인스턴스 생성
c = Dog2('peach', 4)
print(c.info())

# 메서드 호출
print(c.speack('Mung Mung'))