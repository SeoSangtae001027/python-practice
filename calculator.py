#덧셈, 뺄셈, 곱셈, 나눗셈을 할 수 있는 계산기 프로그램을 만드시오.
#입력의 각 줄에는 숫자가 하나씩 주어진다. 주어진 두 숫자의 덧셈, 뺄셈, 곱셈, 나눗셈을 순서대로 계산을 하고 결과를 출력한다.
#두 숫자의 계산 결과를 출력한다.

x = 300
y = 200
print("첫 번째 숫자를 입력하세요 : " +str(x))
print("두 번째 숫자를 입력하세요 : " +str(y))
value = x + y
print(str(x) +" + "+ str(y) +" = "+ str(value))
value = x - y
print(str(x) +" - "+ str(y) +" = "+ str(value))
value = x * y
print(str(x) +" * "+ str(y) +" = "+ str(value))
value = x / y
print(str(x) +" / "+ str(y) +" = "+ str(value))