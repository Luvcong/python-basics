# Chapter07-1
# 1) 예외처리

# 예외(Exception) != 에러(Error)
# 예외는 프로그램 실행 중 예상 가능하고 처리할 수 있는 문제
# 에러는 운영환경에서 발생 (하드웨어적인 결함, 시스템 자체 문제 등)

# 예외 없는 것을 가정하고 프로그램 작성 -> 런타임 예외 발생 시 예외 처리 권장 (EAFP)
# : 모든 예외를 처음부터 발견하고 개발하기는 어려움 (예외는 항상 발생할 수 있음)

# 예외 종류
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError... 등
# 문법적으로는 예외가 없으나 코드 실행 단계에서 발생하는 예외 처리가 중요
    # 1) 예외는 반드시 처리 필요 **
    # 2) 로그를 남겨서 대응할 수 있도록
    # 3) 예외처리를 위임할 수 있음

# 1-1) SyntaxError : 문법 오류

# 1-2) NameError : 참조 오류

# 1-3) ZeroDivisionError : 0으로 나눌 때 발생

# 1-4) IndexError : 존재하지 않는 Index에 접근 시 발생

# 1-5) KeyError : 존재하지 않는 Key에 접근 시 발생

# 1-6) AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 시 발생

# 1-7) ValueError : 존재하지 않는 Value에 접근 시 발생

# 1-8) FileNotFoundError : 존재하지 않는 파일에 접근 시 발생
# f = open('test.txt')

# 1-9) TypeError : 자료형에 맞지 않는 연산 수행 시 발생
# x = [1, 2]
# y = (1, 2)
# z = 'test'
# print(x + y)    # list는 가변, 튜플은 불변이기 떄문에 연산 불가 => error 발생


# 예외처리 기본
# try : 에러가 발생 할 가능성이 있는 코드 실행
# except 에러명1 : 에러명에 해당하는 에러를 잡는 곳
# except 에러명2 :
# else : try 블록의 에러가 없을 경우 실행
# finally : 항상 실행

name = ['Kim', 'Lee', 'Park']

# ex 1)
try :
    z = 'Kim'   # 'Kim2' => except 실행 (else 미실행)
    x = name.index(z)
    print('{} Found it ! {} in name'.format(z, x + 1))
except ValueError :
    print('Not Found it ! - Occurred ValueError !')
else :
    print('Ok! else')

# print('---------')

# ex 2)
try :
    z = 'Kim'   
    x = name.index(z)
    print('{} Found it ! {} in name'.format(z, x + 1))
except Exception :  # except => 포괄적으로 작성 (모든 에러처리를 잡아줌)
    print('Not Found it ! - Exception !')
else :
    print('Ok! else')

print('---------')

# ex 3)
try :
    z = 'Kim2'  # 'Kim2' => except 실행 + finally 실행
    x = name.index(z)
    print('{} Found it ! {} in name'.format(z, x + 1))
except Exception as e :
    print(e)    # 예외 사유
    print('Not Found it ! - Exception !')
else :
    print('Ok! else')
finally :
    print('Ok ! finally')

print('---------')

# ex 4)
# 예외 발생 : raise
# rasie 키워드로 예외 직접 발생
try :
    a = 'Kim'
    if a == 'Kim':
        print('OK! Pass!')
    else:
        raise ValueError    # ValueError로 예외 직접 발생 시킴
except ValueError:          # ValueError 예외 처리 진행
    print('Occurred! Exception!')
else:
    print('Ok! else!')