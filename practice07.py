# 윤년 확인기
# year에 입력된 년도가 4로 나누어 떨어지면 윤년, 100으로 나누어떨어지면 윤년이 아니고,
# 400으로 나누어 떨어지면 윤년임을 이용한다
year=int(input("년도를 입력하세요:"))

if((year%4==0 and year%100!=0) or year% 400==0):
    print(year,"년은 윤년입니다.")
else:
    print(year,"년은 윤년이 아닙니다.")
