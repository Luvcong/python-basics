# Chapter10-1
# Hangman(행맨) 미니게임 (1)
# 기본 프로그램 제작 및 테스트

# 시간 처리
import time

# 처음 인사
name = input('What is your name ?')
print('Hi ! '+ name, "Time to play hangman game !")

time.sleep(1)
print()

print('Start loading...')
print()
time.sleep(0.5)

# 정답 단어
word = "secret"

# 추측 단어
guesses = ''

# 횟수
turns = 10

while turns > 0 :
    failed = 0  # 실패 횟수

    for char in word :
        if char in guesses :    # 처음에는 공백이기 떄문에 절대 True 조건식에 들어가지 않음
            print(char, end = ' ')
        else :
            print("_", end = ' ')
            failed += 1

    print()
    if failed == 0 :
        print()
        print()
        print("Congratulations! The Guesses is correct.")
        break
    print()

    print()
    guess = input('guess a character : ')

    guesses += guess

    if guess not in word :
        turns -= 1
        print('Oops ! Wrong')
        print('You have ', + turns, 'more guesses!')

        if turns == 0 : 
            print("You hangman game failed. Bye!")