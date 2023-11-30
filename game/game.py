import random

#RULES OF THE GAME

#Rock destroys Scissor
#Paper wraps Rock
#Scissor cuts Paper

words = ['rock','paper','scissor']

rand_word = random.choice(words)

score = 0

for i in range(1,4):
    guessed_word = input("Enter Your Choice: ").lower()
    if guessed_word == 'rock':
        if rand_word == 'rock':
            score = score
            print("a tie")
            print(score)
        elif rand_word == 'paper':
            score = score - 1
            print("Paper wraps rock, YOU LOST")
            print(score)
        elif rand_word == 'scissor':
            score = score + 1
            print("Rock destroys scissor, YOU WON")
            print(score)
        else:
            print("Invalid input!")
    elif guessed_word == 'paper':
        if rand_word == 'paper':
            score = score 
            print("a tie")
            print(score)
        elif rand_word == 'rock':
            score = score + 1
            print("Paper wraps rock, YOU WON")
            print(score)
        elif rand_word == 'scissor':
            score = score - 1
            print("Scissor cuts paper, YOU LOST")
            print(score)
        else:
            print("Invalid input!") 
    elif guessed_word == 'scissor':
        if rand_word == 'scissor':
            score = score
            print("a tie")
            print(score)
        elif rand_word == 'paper':
            score = score + 1
            print("Scissor cuts paper, YOU WON")
            print(score)
        elif rand_word == 'rock':
            score = score - 1
            print("Rock destroys scissor, YOU LOST")
            print(score)
        else:
            print("Invalid input!")                           
    else:
        print("Invalid input!")