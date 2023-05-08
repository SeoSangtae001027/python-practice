from random import *    
# 랜덤함수는 같은 여러 문장을 실행해도 출력값이 다름.
print(random()) 
# 랜던함수는 실행할 떄마다 출력값이 다름. 0.0 이상 1.0 미만
print(random() * 10 )
# 0.0d 이상 10.0 미만
print(int(random() * 10))
# int를 이용해서 정수값 출력
print(int(random() * 10 + 1))
# 1.0 이상 11.0 미만

# 로또 만들기
print(int(random() * 45 + 1)) # 1이상 45이하
print(int(random() * 45 + 1)) # 1이상 45이하
print(int(random() * 45 + 1)) # 1이상 45이하
print(int(random() * 45 + 1)) # 1이상 45이하
print(int(random() * 45 + 1)) # 1이상 45이하
print(int(random() * 45 + 1)) # 1이상 45이하

print(randrange(1,46)) # 1 ~ 46 미만의 임의의 값
print(randint(1,45)) # 1, 45를 포함하고 사이의 임의의 값