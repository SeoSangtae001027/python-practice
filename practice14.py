# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu)) # 중괄호를 이용해 셋으로 들어감

menu = list(menu)       # 타입을 리스트로 변경함.
print(menu, type(menu)) # 대괄호로 리스트를 출력함.

menu = tuple(menu)
print(menu, type(menu)) # 소괄호로 튜플을 출력함.

menu = set(menu)
print(menu, type(menu))