# Chapter09-01
# 1) 파일 읽기 및 쓰기

# 읽기 : r
# 쓰기 : w
# 추가 : a
# 텍스트 : t
# 바이너리 : b

# 상대 경로 (../, ./)
# 절대 경로 (/Users/jinheekim/peach/study/python-basics)

# 1-1) 파일 읽기 (R : Read)
# ex 1)
# 텍스트로 읽을 경우 : rt, r (t는 기본값으로 작성하지 않아도 가능)
# 바이너리로 읽을 경우 : rb
# encoding을 생략하면 기본 값은 UTF-8
f = open('./resource/it_news.txt', 'r', encoding='UTF-8')

# 속성 확인
print(dir(f))
print('----------')

# 인코딩 확인
print(f.encoding)
print('----------')

# 파일 이름 확인
print(f.name)
print('----------')

# 모드 확인
print(f.mode)
print('----------')

# 파일 읽기
cts = f.read()
print(cts)
print('----------')

# 반드시 close
f.close()

# ex 2) with 문 사용
# with문 사용시 close()를 사용하지 않아도 자동으로 자원 반납
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f :
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))

print()
print('----------')

# ex 3) read()
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f :
    c = f.read(20)  # 20byte만큼 출력
    print(c)        # Right now gamers can
    c = f.read(20)
    print(c)        # pay just $1 for acc
    print('----------')

    """
    같은 read(20)을 실행하더라도 동일한 위치로 실행되는 것이 아님
    커서가 존재하여 현재 내가 읽은 위치를 알 수 있음
    seek(0, 0)을 사용하면 파일의 맨 처음으로 이동 (seek(from, to))
    """

    f.seek(0, 0)
    c = f.read(20)  
    print(c)        # Right now gamers can
    print('----------')

# ex 4) readline : 한 줄 씩 읽기
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f :
    line = f.readline()
    print(line)
    print('----------')

# ex 5) readlines : 전체를 읽은 후 라인 단위 리스트로 저장
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f :
    cts = f.readlines()
    print(cts)
    print()
    for c in cts :
        print(c, end = '')
    print('----------')

# 1-2) 파일 쓰기
# ex 1) write
with open('./resource/contents1.txt', 'w') as f :
    f.write('I Love Python\n')

# ex 2) append
with open('./resource/contents1.txt', 'a') as f :
    f.write('I Love Python2\n')

# ex 3) writelines : 리스트 -> 파일
with open('./resource/contents2.txt', 'w') as f :
    list = ['Orage\n', 'Apple\n', 'banana\n', 'melon']
    f.writelines(list)

# ex 4) print : file 옵션을 사용하면 콘솔에 출력되지 않고, 지정한 파일에 작성됨
with open('./resource/contents3.txt', 'w') as f :
    print('Test Text Write', file = f)
    print('Test Text Write', file = f)
    print('Test Text Write', file = f)