sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬은 쉬워요."
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요.
"""
print(sentence3)
# 문자열 중 여러 문장을 출력할 때 큰따음표 3개를 사용한다.

jumin = "990120-1234567"
print("성별 : " +jumin[7])
# []는 필요한 정보만을 담음. 0번째부터 시작함. 
# 주민번호 뒷자리의 첫번째가 성별을 의미하기에 7임.
print("연 : " +jumin[0:2]) 
# 0부터 2직전까지의 숫자를 출력함. 99의 정보를 담기 위함.
print("월 : " +jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " +jumin[:6]) 
# 처음부터 6직전까지의 값을 출력해줌.
print("뒤 7자리 : " +jumin[7:])
# 7번째부터 끝까지의 값을 출력해줌.
print("뒤 7자리 (뒤에부터) : " + jumin[-7:])
# 뒤에서부터 -1부터 시작하여 문장을 구성할 수 있음.
