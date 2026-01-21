# Chapter08-1
# 1) 내장(Built-in) 함수
# str(), int(), tuple() 등..

# 1-1) abs() : 절대값
print(abs(-2))
print('----------')

# 1-2) all, any : iterable 요소 검사 (참, 거짓인지 판별)
# all : 모두 True 여야 Ture 값 반환
# any : 하나라도 True인 경우 True 값 반환
print(all([1, 2, 3]))       # True
print(all([1, '', True]))   # False
print(any([1, 2, 0]))       # True
print('----------')

# 1=3) chr : 아스키 -> 문자 / ord : 문자 -> 아스키
print(chr(65))
print(ord('A'))
print('----------')

# 1-4) enumerate : index + Iterable 객체 생성
for i, name in enumerate(['abc', 'bcd', 'efg']) :
    print(i, name)
print('----------')

# 1-5) filter : 반복 가능한 객체 요소를 지정한 하뭇 조건에 맞는 값 추출
def  conv_pos(x) :
    return abs(x) > 2

print(list(filter(conv_pos, [1, -3, 2, 0, 5, 2])))

# conv_pos() 함수를 만들지 않고도 람다 함수를 이용해서 만들 수 있음
print(list(filter(lambda x : abs(x) > 2, [1, -3, 2, 0, 5, 2])))
print('----------')

# 1-6) id : 객체의 주소값(reference) 반환
print(id(int(5)))
print(id(4))
print('----------')

# 1-7) len : 요소의 길이 반환
print(len('abcdfg'))
print(len([1, 2, 3, 4, 5, 6, 7]))
print('----------')

# 1-8) max, min : 최대값, 최소값
print(max(1, 2, 3))
print(max('pythonstudy'))
print(min([1,2,3]))
print(min('pythonstudy'))
print('----------')

# 1-9) map : 반복 가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x) :
    return abs(x)

print(list(map(conv_abs, [1, -3, 2, 0, -5, 9])))
# 람다 활용 시,
print(list(map(lambda x : abs(x), [1, -3, 2, 0, -5, 9])))
print('----------')

# 1-10) pow : 제곱값 반환
print(pow(2, 10))
print('----------')

# 1-11) range : 반복 가능한 객체(Iterable) 반환
print(range(1, 10, 2))
print(list(range(1, 10, 2)))
print(list(range(0, -15, -1)))
print('----------')

# 1-12) round : 반올림
print(round(6.5781, 2)) # 6.58
print(round(6.5781))    # 7 (2번째 인자를 넘겨주지 않으면 첫번째 자리에서 바로 반올림 처리)
print('----------')

# 1-13) sorted : 반복 가능한 객체(Iterable)를 정렬 후 반환 
print(sorted([1, 8, 2, 5, 3, 9]))
print(sorted(['p','y','t','h','o','n']))    # ['h', 'n', 'o', 'p', 't', 'y'] 알파벳 순서 오름차순
print('----------')

# 1-14) sum : 반복 가능한 객체(Iterable) 합 반환
print(sum([6,7,8,9,10]))
print(sum(range(1,101)))
print('----------')

# 1-15) type : 자료형 확인
print(type(3))
print(type({}))
print(type(()))
print(type([]))

# 1-16) zip : 반복 가능한 객체(Iterable)의 요소를 묶어서 튜플 형태로 반환
print(list(zip([10,20,30],[40,50,777])))            # [(10, 40), (20, 50), (30, 777)]
# 40은 반환되지 않음 / 요소를 묶을때 짝이 맞는 것만 반환
print(list(zip([10,20,30, 40],[40,50,777])))        # [(10, 40), (20, 50), (30, 777)]
print(type(list(zip([10,20,30],[40,50,777]))[0]))   # <class 'tuple'>