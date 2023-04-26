import random

answer = random.randint(10, 100)
while True:
    user_input = int(input())
    if user_input == answer:
        print("정답입니다")
        break
    elif user_input < answer:
        print("up")
    else:
        print("down")
print("게임이 끝났습니다.")

# 조건문을 추가해서 사용자 인풋이 정답보다 작다면 up
# 정답보다 크다면 down을 프린트하게 해주세요
