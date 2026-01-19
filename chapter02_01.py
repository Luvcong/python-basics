# Chapter02-1

# 1) Print 사용법

# 1-1) 기본 출력
# 작은 따옴표 ''' -> 가장 많이 사용
# 큰 따옴표   """
# 작은 따옴표 3개 ```
# 큰 따옴표 3개   """
print('python')
print() # 개행
print('python')
print('----------')

# 1-2) separator 옵션 : 원하는 포맷 형식으로 출력 
print('P', 'Y', 'T', 'H', 'O', 'N')
print('P', 'Y', 'T', 'H', 'O', 'N', sep=',')
print('010', '1234', '5678', sep='-')
print('python', 'test.com', sep='@')
print('----------')

# 1-3) end 옵션 : 출력문 끝 부분의 포맷을 지정하는 옵션
print('Welcome to', end=' ')    # print는 기본적으로 개행을 진행하지만, end 옵션을 이용하여 띄어쓰기 등으로 사용할 수 있음
print('IT News', end=' ')
print('Web Site')
print('----------')

# 1-4) file 옵션
import sys
print('Learn Python', file=sys.stdout)  # sys.dtdout : console out 의미
print('----------')

# 2) format 사용 (% , .format)
# d : 숫자   (3)
# s : 문자열 ('python')
# f : 소수   (3/1445454)

# 설정한 format에 맞춰서 파라미터 값을 넣어야 함
print('%s %s' % ('one', 'two'))    

# 내부적으로 입력한 값에 맞춰서 출력됨 (숫자, 문자 등 상관없이 입력 가능)
print('{} {}'.format('one', 'two'))
print('{} {}'.format(1, 'two'))

# {} (중괄호) 안에 숫자를 입력하면, 해당 숫자에 맞는 Index의 파라미터 값이 출력됨
print('{1} {0}'.format('one', 'two'))   # two one
print('----------')

# 2-1) %s
# 입력한 문자열 포함하여 최소 10자리 문자열 출력
# 양수로 입력하는 경우 : 왼쪽에 공백 채움
# 음수로 입력하는 경우 : 오른쪽에 공백 채움
print('%10s' % 'python')
print('{:>10}'.format('python'))

print('%-10s' % 'python')
print('{:10}'.format('python'))

# 중앙 정렬
print('{:^10s}'.format('python'))

# 공백을 '_'로 출력
print('{:_>10}'.format('python'))   # ____python

# '.'을 붙이는 경우 입력한 숫자만큼 문자열 출력 (절삭)
print('%.5s'% 'hi') # hi
print('%.5s'% 'pythonstydy')    # pytho

# 10자리 공간 확보 + 5자리만 출력
print('{:10.5}'.format('pythonsutdy'))  # pytho
print('----------')

# 2-2) %d
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

print('%4d' % (42))
print('{:4d}'.format(42))
print('----------')

# 2-3) %f
print('%f' % (3.1434343434343434))     # 3.143434
print('{:f}'.format(3.1434343434343434))

print('%1.8f' % (3.1434343434343434))  # 3.14343434

# 6자리 문자열 중 소수 2자리까지 출력
# 입력 값에서 정수가 1개이기 때문에 나머지는 0으로 채움
print('%06.2f' % (3.1434343434343434))  # 003.14
print('{:06.2f}'.format(3.1434343434343434))
