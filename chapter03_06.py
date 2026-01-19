# Chapter03-6
# 6) 집합(Set)
#  : 집합 자료형의 특징 (순서 보장 X / 중복 저장 X / 수정 가능 / 삭제 가능)

# 6-1) 선언
a = set()
b = set([1, 2, 3, 4, 5, 5, 5])
c = set([1, 2, 'Cat', 'Plate'])
e = {'foo', 'bar', 'baz', 'qux'}	# key 없이 선언하면 딕셔너리가 아닌, 집합 형태
f = {42, 'foo', (1, 2, 3), 3.14159}

# 중복 값 선언은 가능하나 출력시, 중복 값은 모두 제외되어 출력됨
print('b : ', b)

# 6-2) 변환
# 튜플 변환 (set -> tuple)
print(type(tuple(a)))

# 리스트 변환 (set -> list)
print(type(list(b)))
print('----------')

# 6-3) 길이
print(len(a))	# 0
print(len(b))	# 5 (중복 제외 길이 값 반환)
print('----------')

# 6-4) 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# & : 교집합
print('s1 & s2 : ', s1 & s2)				# {4, 5, 6}
print('s1 & s2 : ', s1.intersection(s2))	# {4, 5, 6}
print('----------')

# | : 합집합
print('s1 | s2 : ', s1 | s2)		# {1, 2, 3, 4, 5, 6, 7, 8, 9}
print('s1 | s2 : ', s1.union(s2))	# {1, 2, 3, 4, 5, 6, 7, 8, 9}
print('----------')

# - : 차집합
print('s1 - s2 : ', s1 - s2)			# {1, 2, 3}
print('s1 - s2 : ', s1.difference(s2))	# {1, 2, 3}
print('----------')

# 중복 원소 확인
# : 교집합이 있으면 False, 없으면 True
print('s1 & s2 : ', s1.isdisjoint(s2))	# False

# 부분 집합 확인
print('issubset : ', s1.issubset(s2))		# False : s1의 모든 원소가 s2에 포함되어 있으면 True
print('issuperset : ', s1.issuperset(s2))	# False : s2의 모든 원소가 s1에 포함되어 있으면 True
print('----------')

# 추가 및 제거
s1 = set([1, 2, 3, 4])
s1.add(21)
print('s1 : ', s1)	# {1, 2, 3, 4, 21}

# remove  : 지우려는 값이 없는 경우 'key Error' 예외 발생
# discard : 지우려는 값이 없는 경우에도 예외 발생 X
# clear() : 모든 값 삭제
s1.remove(21)
print('s1 : ', s1)	# {1, 2, 3, 4}

s1.discard(21)
print('s1 : ', s1)	# {1, 2, 3, 4}

s1.clear()
print('s1 : ', s1)	# set()