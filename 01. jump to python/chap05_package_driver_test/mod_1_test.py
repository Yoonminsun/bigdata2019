# import mod_1
# from mod_1 import * # *은 __로 시작하는 것들을 제외한 모든 이름을 import 한다, 일반적으로 좋은 방법은 아님
# from mod_1 import mul
# import mod_1 as mod  # as 다음의 이름을 import한 모듈에 직접 연결한다, 따라서 as 다음의 이름으로 사용 가능
from mod_1 import mul as mod_mul # mod_mul이라는 이름으로 mod_1의 mul을 import 하여 사용한다다

# print(mod_1.mul(2,4))
# print(mul(2,4))
# print(mod.mul(2,4))
print(mod_mul(2,4))
