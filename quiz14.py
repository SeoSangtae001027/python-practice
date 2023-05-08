from random import *
# user = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# shuffle(user)
# chicken = sample(user,1)
# coffee = user - chicken
# shuffle(coffee)
# coffee = sample(coffee,3)
# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : " +chicken)
# print("커피 당첨자 : " +coffee)
# print("-- 축하합니다 --")

user = range(1,21)
print(type(user))
user = list(user)
shuffle(user)
x = sample(user,4)
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {}".format(x[0]))
print("커피 당첨자 : {}".format(x[1:]))
print("-- 축하합니다 --")





