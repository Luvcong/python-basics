# Chapter03-5
# 5) 딕셔너리(Dictionary)
#  : 범용적으로 가장 많이 사용
#  : key와 value로 이루어져 있음
#  : 딕셔너리 자료형 특징 (순서 보장 X / 키 중복 X / 수정 가능 / 삭제 가능)

# 5-1) 선언
a = {'name': 'Kim', 'phone': '01012345678', 'birth': '870124'}
b = {0: 'Hello python!'}
c = {'arr': [1, 2, 3, 4]}

# d, e, f 모두 동일
d = {
	 'Name' : 'Niceman',
	 'City'   : 'Seoul',
	 'Age': '33',
	 'Grade': 'A',
	 'Status'  : True
}
e =  dict([
	 ( 'Name', 'Niceman'),
	 ('City', 'Seoul'),
	 ('Age', '33'),
	 ('Grade', 'A'),
	 ('Status', True)
])
f =  dict(
	 Name   = 'Niceman',
	 City   = 'Seoul',
	 Age    = '33',
	 Grade  = 'A',
	 Status = True
)

# 5-2) 값 출력
print('a : ', a['name'])       # 속성 접근
print('a : ', a.get('name'))   # get() 사용
# 속성으로 접근 시, 해당 key가 없는 경우 'KeyError' 발생
# get()으로 접근 시, 해당 key가 없는 경우 None 출력 -> 해당 방법을 많이 사용
print('----------')

# 5-3) 값 추가 및 수정
#  : 새로운 key를 사용하면 추가 / 기존 key를 사용하면 수정
a['name'] = 'kim'       
a['address'] = 'seoul'
print('a : ', a)
print('----------')

# update() 함수 사용하여 추가 및 수정 가능
f.update(Age = 30)
print('f : ', f)    # {'Name': 'Niceman', 'City': 'Seoul', 'Age': 30, 'Grade': 'A', 'Status': True}

# 변수를 이용하여 추가 및 수정 가능
temp = {'ABC': 'abc'}
f.update(temp)      # {'Name': 'Niceman', 'City': 'Seoul', 'Age': 30, 'Grade': 'A', 'Status': True, 'ABC': 'abc'}
print('f : ', f)
print('----------')

# 5-4) len() : 길이 확인 (key 개수 반환)
print('a: ', len(a))
print('b: ', len(b))
print('c: ', len(c))
print('d: ', len(d))
print('----------')

# dict_keys, dict_values, dict_items : 반복문(__iter__)에서 사용 가능
# 5-5) keys() : key 값 출력
print('a : ', a.keys())         # dict_keys(['name', 'phone', 'birth', 'address'])
print('a : ', list(a.keys()))   # ['name', 'phone', 'birth', 'address']
print('----------')

# 5-6) values() : value 값 출력
print('a : ', a.values())       # dict_values(['Kim', '01012345678', '870124', 'seoul'])
print('a : ', list(a.values())) # ['kim', '01012345678', '870124', 'seoul']
print('----------')

# 5-7) items() : key, value 값 모두 출력
print('a : ', a.items())        # dict_items([('name', 'kim'), ('phone', '01012345678'), ('birth', '870124'), ('address', 'seoul')])
print('a : ', list(a.items()))  # [('name', 'kim'), ('phone', '01012345678'), ('birth', '870124'), ('address', 'seoul')]
print('----------')

# 5-8) pop() : 특정 key에 해당하는 값을 꺼낸뒤 새로운 딕셔너리 반환
a.pop(('name'))
print('a : ', a)    # {'phone': '01012345678', 'birth': '870124', 'address': 'seoul'}
b.pop(0)            # {}
print('b : ', b)
print('----------')

# 5-9) popitem() : 랜덤으로 key 값을 꺼낸뒤 새로운 딕셔너리 반환
print(d.popitem())  # ('Status', True)
print('d : ', d)    # {'Name': 'Niceman', 'City': 'Seoul', 'Age': '33', 'Grade': 'A'} => Stats 값이 삭제됨
print('----------')

# 5-10) in : 값 존재 여부를 bool 형태로 반환
print('a : ', 'birth' in a) # True
print('a : ', 'Birth' in a) # False