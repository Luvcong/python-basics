# Chapter06-2
# 모듈(Module)
# : 함수, 변수, 클래스 등 python 구성 요소 등을 모아놓은 파일

def add(x, y) :
    return x + y

def subtract(x, y) :
    return x - y

def multiply(x, y) :
    return x * y

def divide(x , y) :
    return x / y
    
def power(x, y) :
    return x ** y

# __name__ 사용
# main 영역 안에 코드를 작성하면 외부에서 import 하더라도 해당 코드는 실행 안됨
if __name__ == '__main__' :
    print('-' * 15)
    print('called! inner!')
    print(add(5, 5))
    print(subtract(15, 5))
    print(multiply(5, 5))
    print(divide(10, 2))
    print(power(5, 3))
    print('-' * 15)