# Chapter02-1-ex1

# 1) Print 사용법 (추가)
# : 3가지 Format Practices

x = 50
y = 100
text = 308276567
n = 'Luv'

# 1-1) 출력
# %
ex1 = 'n = %s, s = %s, sum = %d' % (n, text, (x + y))
print(ex1)
print('----------')

# .format
ex2 = 'n = {n}, s = {s}, sum = {sum}'.format(n=n, s=text, sum=x+y)
print(ex2)
print('----------')

# f-string
ex3 = f'n = {n}, s = {text}, sum = {x+y}'
print(ex3)
print('----------')

# 구분기호 출력
m = 100000000
print(f'm : {m:,}')
print('----------')


# 1-2) 정렬
# ^ : 중앙 정렬
# < : 왼쪽 정렬
# > : 오른쪽 정렬

t = 20
print(f't : {t:10}')    # t :         20
print(f't : {t:^10}')   # t :     20    
print(f't : {t:<10}')   # t : 20        
print(f't : {t:>10}')   # t :         20
print('----------')

# 자리수에 있는 공백을 * 체워서 출력
print(f't : {t:*^10}')  # t : ****20****
print(f't : {t:*<10}')  # t : 20********
print(f't : {t:*>10}')  # t : ********20
print('----------')

