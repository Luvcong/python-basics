# Chapter06-3
# 패키지
# python은 패키지로 분할 된 개별적인 모듈로 구성
# __init__.py : Python 3.3 ~ 없어도 패키지로 인식 -> 단, 하위 호환을 위해 작성 권장
#             : 해당 패키지에 있는 파일들 중 외부 import를 가능하게 할 파일명만 기재
# 상대경로 : ..(부모 디렉터리) / .(현재 디렉터리) -> 모듈 내부에서만 사용

# ex 1)
import sub.sub1.module1
import sub.sub2.module2

# 사용
sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()
print('----------')
sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()

print('----------')

# ex 2)
from sub.sub1 import module1
from sub.sub2 import module2 as m2 # Alias

module1.mod1_test1()
module1.mod1_test2()

m2.mod2_test1()
m2.mod2_test2()
print('----------')

# ex 3)
from sub.sub1 import *  # *로 정의하는건 비권장
from sub.sub2 import *

module1.mod1_test1()
module1.mod1_test2()

module2.mod2_test1()
module2.mod2_test2()
