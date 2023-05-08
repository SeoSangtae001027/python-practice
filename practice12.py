# 튜플은 리스트보다 빠르지만 변경할 수 없음.
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") 튜플은 add를 사용할 수 없음.

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby) 

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)