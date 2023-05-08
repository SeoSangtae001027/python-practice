subway = [10, 20, 30]
print(subway) # [10, 20, 30]
subway = ["유재석", "강호동", "조세호"]  # 리스트로 묶을 수 있음.
print(subway)
print(subway.index("조세호")) # 조세호는 몇번쨰에 있는지 찾을 수 있음. 0부터 시작
subway.append("하하") # 어펜드를 이용해 리스트 마지막에 하하를 추가함.
print(subway)
subway.insert(1, "정형돈") # 인서트를 이용해 1번에 정형돈을 추가함
print(subway)
print(subway.pop()) # 팝을 이용해 리스트 마지막을 제거함.
print(subway)
subway.append("유재석")
print(subway)
print(subway.count("유재석")) # 리스트 내에 값은 값이 몇개인지 출력함. 2
num_list = [5, 2, 4, 3, 1]
num_list.sort() # 소트를 이용해 정렬
print(num_list)
num_list.reverse() # 리버스를 이용해 역순으로 정렬
print(num_list)
num_list.clear() # 클리어를 이용해 리스트 값을 모두 지울 수 있음.
print(num_list)
num_list = [5, 2, 4, 3, 1]
mix_list = ["조세호", 20, True] # 리스트는 다양한 자료형을 사용할 수 있음.
print(mix_list)
num_list.extend(mix_list) # 익스텐드를 이용해 리스트끼리 합칠 수도 있음.
print(num_list)