# Chapter09-02
# 2) CSV 파일 읽기 및 쓰기

# CSV : MIME TYPE = text/csv

import csv

# ex 1)
with open('./resource/test1.csv', 'r') as f :
    reader = csv.reader(f)
    # next(reader)        # Header skip

    # 객체 확인
    print(reader)
    # 타입 확인
    print(type(reader))
    # 속성 확인
    print(dir(reader))  # __iter__ 존재
    print('----------')
    for c in reader :
        # print(c)
        print(' : '.join(c))    # list -> str 변경
print('----------')

# ex 2)
with open('./resource/test2.csv', 'r') as f :
    reader = csv.reader(f, delimiter='|')   #delimiter : 구분자 기호

    for c in reader : 
        print(c)

# ex 3) DictReader() : 딕셔너리 형태로 반환
with open('./resource/test1.csv', 'r') as f :
    reader = csv.DictReader(f)
    print(reader)
    print(type(reader))
    print(dir(reader))

    # for c in reader :
        # print(c)    # {'Name': 'Afghanistan', 'Code': 'AF'} ..
    
    for c in reader :
        for k, v in c.items() :
            print(k, v)
        print('----------')

# ex 4)
# 하나의 리스트가 하나의 레코드로 인식됨
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]]
with open('./resource/write1.csv', 'w', encoding='utf-8') as f :
    print(dir(csv))
    wt = csv.writer(f)

    # dir 확인
    print(dir(wt))
    print(type(wt))

    for v in w :
        wt.writerow(v)

# ex 5)
with open('./resource/write2.csv', 'w', newline='') as f :
    # 필드명
    fields = ['one', 'two', 'three']

    # Dic Writer
    wt = csv.DictWriter(f, fieldnames=fields)

    # Header Writer
    wt.writeheader()

    for v in w :
        wt.writerow({'one': v[0], 'two': v[1], 'three': v[2]})
