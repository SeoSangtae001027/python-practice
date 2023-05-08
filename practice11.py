cabinet = {3:"유재석", 100:"김태호"} # 3이 키의 역할, 유재석이 값을 의미함.
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3)) # 겟을 이용해 위의 값과 같은 값을 출력함.
# 만약 키에 값이 없을 경우 대괄호를 이용하면 오류가 발생되고 겟을 이용하면 None값을 출력함.
print(cabinet.get(5))
print(cabinet.get(5, "사용 가능")) # 키에 값이 없으면 None대신 사용 가능을 출력함.
print(3 in cabinet) # 사전자료값에 3이라는 키가 있는지 확인할 수 있음. True
# 키는 숫자뿐만 아닌 문자로도 가능함
cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
cabinet["A-3"] = "김종국" # 기존에 키의 값을 바꿀 수 있음.
cabinet["C-29"] = "조세호" # 새로운 키와 값을 추가할 수 있음.
del cabinet["A-3"] # 딜리트를 이용해 키와 값을 없앨 수 있음.
print(cabinet.keys()) # 키들만 출력해줌.
print(cabinet.values()) # 밸류값들만 출력해줌.
print(cabinet.items()) # 키와 밸류값을 쌍으로 출력해줌.
cabinet.clear() # 모든 내용을 삭제해줌.