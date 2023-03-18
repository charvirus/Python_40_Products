import random

number = random.randint(1, 100)

game_count = 1

while True:
    my_number = int(input("1~100 사이의 숫자를 입력 : "))

    if my_number > number:
        print("보다 작다")
    elif my_number < number:
        print("보다 크다")
    elif my_number == number:
        print(f"정답, {game_count}회의 시도")
        break

    game_count = game_count + 1
