# 예: http://naver.com
# 규칙1 : http:// 부분은 제외
# 규칙2: 처음 만나는 . 이후 부분은 제외
# 규칙3: 남은 글자 중 처음 세자리 + 글자 개수 + 글자 내 e 개수 + !

url = "http://naver.com"
password = url.replace("http://", "")
password = password[:password.index(".")]

print("생성된 비밀번호 : " +password[:3] + str(len(password)) + str(password.count("e")) + "!")

final_password = password[:3] + str(len(password)) + str(password.count("e")) + "!"

print("{0} 의 비밀번호는  {1} 입니다.".format(url, final_password) )