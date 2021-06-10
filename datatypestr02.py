# 문자열을 출력할 때 줄을 개행해서 출력하고 싶다면 \n 탈출문자
# 를 활용한다. 이문자는 커서가 이 지점에 닿으면 enter키를
# 눌러서 커서를 다음줄로 내려달라는 요청이다.

s1 = "first\nsecond"
print(s1)

s2 = "first\n\nsecond"
print(s2)