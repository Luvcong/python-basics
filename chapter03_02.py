# Chapter03-2
# 2) 문자형

str1 = 'pyton'

# 2-1) 변수 타입
print(type(str1))
print('----------')

# 2-2) 공백포함 문자 길이
print(len(str1))
print('----------')

# 2-3) 빈 문자열 선언
str2 = ''   # str2 = "" 동일
str3 = str()

print(type(str2), len(str2))
print(type(str3), len(str3))
print('----------')

# 2-4) 이스케이프 문자 사용
"""
\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : null 문자
"""

# 2-5) Raw String : 이스케이프 문자 무시
# r'문자열'
raw_str1 = r'D:\Python\pyton3'
print(raw_str1) # D:\Python\pyton3
print('----------')

# 2-6) 멀티라인(역슬래시) 출력
# \ : 변수 = 뒤에 역슬래시가 오면, 해당 변수에 값을 바인딩 한다는 의미
multi_str = \
'''
String
Multi line
Test
'''
print(multi_str)
print('----------')

# 2-7) 문자열 연산
str_o1 = 'Python'
str_o2 = 'Apple'
str_o3 = 'How are you doing?'
str_o4 = 'Seoul Deajeon Busan Jinju'

print(str_o1 * 3)           # PythonPythonPython
print(str_o1 + str_o2)      # PythonApple

# 문자열 존재 여부 체크
print('y' in str_o1)        # True
print('z' in str_o2)        # False
print('p' not in str_o2)    # False
print('----------')

# 2-8) 문자열 형변환
# str(값)
print(str(66), type(str(66)))
print('----------')

# 2-9) 문자열 함수 (upper, isalnum, startswith, count, endswith, isalpha...)

# 앞글자만 대문자로 변환
print(str_o1.capitalize())

# 마지막 문자 값 체크
print(str_o2.endswith('?')) # 문자열 마지막에 '?'가 존재하는지 확인

# 문자열 대체
print(str_o1.replace('thon', 'good'))   # Pygood

# 정렬
# 문자열을 입력받아 정렬 후 리스트로 반환
print(sorted(str_o1))

# 입력 문자열을 기준으로 분리 (리스트로 반환)
print(str_o4.split(' '))
print('----------')

# 2-10) 반복(시퀀스)
im_str = 'Good Boy!'
# dir : 사용가능한 class 모두 출력
print(dir(im_str))  # __iter__이 존재하면 반복문 사용 가능

# 출력
for i in im_str :
    print(i)
print('----------')

# 2-11) 슬라이싱
# 양수 : 앞에서부터 슬라이싱 진행 (index 0부터 시작)
# 음수 : 뒤에서부터 슬라이싱 진행 (index 1부터 시작)
str_s1 = 'Nice Python'

print(len(str_s1))  # 11

# index -1 까지 출력 (0, 1, 2번째까지의 index 문자열 출력)
print(str_s1[0:3])  # NIC

# 숫자 생략하고 : 만 입력하는 경우 전체 값 사용
print(str_s1[5:])   # Pyton
print(str_s1[:len(str_s1)])  # str_s1[:11]
print(str_s1[:len(str_s1) -1])  # str_s1[:10]
print(str_s1[1:9:2])

print(str_s1[-5])   # y

# index 1부터 포함 ~ 끝에서 2번째 index 직전까지
# Nice Pyth
print(str_s1[1:-2]) # ice Pyth

# 끝에서부터 index 5부터 ~ 마지막까지
print(str_s1[-5:])  # ython

# 처음 ~ 끝까지 2개 간격만큼 (앞에서부터)
print(str_s1[::2])  # Nc yhn

# 처음 ~ 끝까지 1개 간격만큼 (뒤에서부터)
print(str_s1[::-1]) # nohtyP eciN
print('----------')

# 2-12) 아스키코드(= 유니코드)

# 문자 -> 아스키코드
a = 'z'
print(ord(a))   # 122

# 아스키코드 -> 문자
print(chr(122)) # z