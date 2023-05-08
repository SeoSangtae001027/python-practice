python = "Python is Amazing"
print(python.lower()) # 전부 소문자로 전환됨.
print(python.upper()) # 전부 대문자로 전환됨.
print(python[0].isupper()) # []안에 들어가는 알파벳이 대문자인지 참거짓을 확인함. 참
print(len(python)) # 문자열의 길이를 측정해줌. 17
print(python.replace("Python", "Java")) # 문자열의 파이썬을 자바로 바꿔줌.

index = python.index("n") # 파이썬 문자열에서 n이 몇번째 사용되었는지 계산해줌. 5
print(index)
index = python.index("n", index + 1) # 첫번째 n 다음의 n이 몇번째 사용되었는지 계산해줌.
print(index)
print(python.find("n")) # n이 몇번쨰 자리에 있는지 출력해줌.
print(python.find("Java")) # 파이썬 문자열에 자바는 없는데 find를 이용하면 -1을 출력해줌.
# index를 이용하여 자바를 찾을 경우 오류가 발생됨.
print(python.count("n")) # 파이썬 문자열에서 n이 총 몇번 사용되었는지 출력해줌.