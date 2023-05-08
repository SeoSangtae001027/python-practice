from random import *
count=0
for i in range(1,51):
    x=randint(5,51)
    if  5 <= x <=15:
        print("[o] {0}번째 손님 (소요시간 : {1})".format(i,x))
        count+=1
    elif x > 15:
        print("[ ] {0}번째 손님 (소요시간 : {1})".format(i,x))
print("총 탑승 승객: " +str(count))
    
    
    
    