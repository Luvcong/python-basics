# Chapter10-1
# Hangman(행맨) 미니게임 (2)
# 프로그램 완성 및 최종 테스트

# 시간 처리
import time
# 랜덤
import random
# csv 처리
import csv
# 사운드
import pygame

# 처음 인사
name = input('What is your name ?')
print('Hi ! '+ name, "Time to play hangman game !")

time.sleep(1)
print()

print('Start loading...')
print()
time.sleep(0.5)

words = []
with open('./resource/word_list.csv', 'r') as f :
    reader = csv.reader(f)
    next(reader)
    for c in reader :
        words.append(c)

random.shuffle(words)
q = random.choice(words)

# 정답 단어 (공백제거
word = q[0].strip()

# 추측 단어
guesses = ''

# 횟수
turns = 10

pygame.mixer.init()
good_sound = pygame.mixer.Sound('./sound/good.wav')
bad_sound = pygame.mixer.Sound('./sound/bad.wav')

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
        good_sound.play()
        time.sleep(1)
        print("Congratulations! The Guesses is correct.")
        break
    print()

    print()
    print('Hint : {}'.format(q[1].strip()))
    guess = input('guess a character : ')
    
    guesses += guess

    if guess not in word :
        turns -= 1
        print('Oops ! Wrong')
        print('You have ', + turns, 'more guesses!')
        bad_sound.play()
        if turns == 0 : 
            print("You hangman game failed. Bye!")