# 집합 (set) 중복이 안되며 순서가 없음.
my_set = {1, 2, 3, 3, 3}
print(my_set)  # {1, 2, 3} 이 출력됨.
java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"]) # 리스트를 셋으로 감쌀 수 있음.

# 교집합 (자바와 파이썬을 모두 할 수 있느 사람)
print(java & python)
print(java.intersection(python)) # 위의 문장과 같은 의미임.

# 합집합 (자바를 할 수 있거나 파이썬을 할 수 있는 사람)
print(java | python)
print(java.union(python))

# 차집합 (자바를 할 수 있지만 파이썬은 할 줄 모르는 사람)
print(java - python)
print(java.difference(python))
# (파이썬을 할 수 있지만 자바를 할 줄 모르는 사람)
print(python - java)
print(python.difference(java))

python.add("김태호") # 세트에 추가할 수 있음.
print(python)
java.remove("김태호") # 세트에 제거할 수 있음.
print(java)