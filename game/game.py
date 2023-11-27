import random

#RULES OF THE GAME

#Rock destroys Scissor
#Paper wraps Rock
#Scissor cuts Paper

words = ['rock','paper','scissor']

rand_word = random.choice(words)

for i in range(1,4):
    guessed_word = input("Enter Your Choice: ").lower()
    if guessed_word == 'rock':
        if rand_word == 'rock':
            print("a tie")
        elif rand_word == 'paper':
            print("Paper wraps rock, YOU LOST")
        elif rand_word == 'scissor':
            print("Rock destroys scissor, YOU WON")
        else:
            print("Invalid input!")
    elif guessed_word == 'paper':
        if rand_word == 'paper':
            print("a tie")
        elif rand_word == 'rock':
            print("Paper wraps rock, YOU WON")
        elif rand_word == 'scissor':
            print("Scissor cuts paper, YOU LOST")
        else:
            print("Invalid input!") 
    elif guessed_word == 'scissor':
        if rand_word == 'scissor':
            print("a tie")
        elif rand_word == 'paper':
            print("Scissor cuts paper, YOU WON")
        elif rand_word == 'rock':
            print("Rock destroys scissor, YOU LOST")
        else:
            print("Invalid input!")                           
    else:
        print("Invalid input!")