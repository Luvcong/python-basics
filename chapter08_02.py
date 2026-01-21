# Chapter08-2
# 2) 외장(External) 함수
# 종류 : sys, pickle, os, shutil, glob, temfile, time, random 등

# 1-1) sys
import sys
print(sys.argv)
print('----------')

# 강제종료
# sys.exit()

# python package 위치
print(sys.path)
print('----------')

# 1-2) pickle : 객체 파일 읽기, 쓰기
import pickle

# 쓰기
f = open('test.obj', 'wb')
obj = { 1 : 'python', 2 : 'study', 3 : 'basic'}
pickle.dump(obj, f)
f.close()   # close() 객체 닫아주기 **
print('----------')

# 읽기
f = open('test.obj', 'rb')
data = pickle.load(f)
print(data, type(data))
f.close()   # close() 객체 닫아주기 **
print('----------')

# 1-3 ) os : 환경 변수, 디렉터리(파일) 처리 관련, 운영체제 작업 관련
# mkdir, rmdir(비어있으면 삭제, 내용이 있으면 삭제되지 않음), rename.. 등

import os
print(os.environ)
print('----------')
print(os.environ['USER'])
print('----------')

# 현재 경로
print(os.getcwd())
print('----------')

# 1-4) time : 시간 관련 처리
import time

print(time.time())

# 형태 변환
print(time.localtime(time.time()))  # time.struct_time(tm_year=2026, tm_mon=1, tm_mday=20, tm_hour=13, tm_min=50, tm_sec=42, tm_wday=1, tm_yday=20, tm_isdst=0)
print(time.ctime()) # Tue Jan 20 13:50:42 2026
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))  # 2026-01-20 13:53:34

# 시간 간격 발생
for i in range(5) :
    print(i)
    # time.sleep(2)
print('----------')

# 1-5) random : 난수 발생π
import random

print(random.random())          # 0 ~ 1 실수
print(random.randint(1, 45))    # 설정한 수에서 랜덤으로 값 출력
print(random.randrange(1, 45))  # 1 ~ 45 사이에서 랜덤 값 출력 (range의 경우 n-1)
d = [1, 2, 3, 4, 5]
random.shuffle(d)
print(d)    # [2, 3, 4, 1, 5]

numbers = [1, 2, 3, 4, 5]
print(random.shuffle(numbers))  # None

"""
[참고]
두번째 코드가 None으로 출력되는 이유 : in-place 변경 메서드이기 떄문

in-place 변경 메서드
- list.sort() / list.reverse() / random.shuffle() => 반환 값이 모두 None
- 제자리(in-place)에서만 진행되고, 아무것도 반환되지 않음

첫번째 코드는 값이 출력되는 이유
- 1) random.shuffle(d) 실행
- 2) 랜덤으로 리스트 섞임
- 3) 반환 값은 None
- 4) print(d) => 이미 섞인 리스트 출력
"""
d = [1, 2, 3, 4, 5]
c = random.choice(d)
print(c)

print('----------')

# 1-6) webbrowser : 본인 OS의 웹 브라우저 실행
import webbrowser
# webbrowser.open('http://www.naver.com')           # 일반적인 URL 열기
# webbrowser.open_new('http://www.naver.com')       # 별도의 브라우저 창에서 열기
# webbrowser.open_new_tab('http://www.naver.com')   # 새 탭에서 열기