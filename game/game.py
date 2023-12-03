import random

#RULES OF THE GAME

#Rock destroys Scissor
#Paper wraps Rock
#Scissor cuts Paper

words = ['rock','paper','scissor']

rand_word = random.choice(words)

score = 0
total_score1 = 0
total_score2 = 0
total_score3 = 0
total_score = 0

for i in range(1,4):
    guessed_word = input("Enter Your Choice: ").lower()
    if guessed_word == 'rock':
        if rand_word == 'rock':
            total_score1 = score
            print("a tie")
            print(f"SCORE: {total_score1}")
        elif rand_word == 'paper':
            total_score2 = total_score1 - 1
            print("Paper wraps rock, YOU LOST")
            print(f"SCORE: {total_score2}")
        elif rand_word == 'scissor':
            total_score3 = total_score2 + 1
            print("Rock destroys scissor, YOU WON")
            print(f"SCORE: {total_score3}")
        else:
            print("Invalid input!")
    elif guessed_word == 'paper':
        if rand_word == 'paper':
            total_score1 = score
            print("a tie")
            print(f"SCORE: {total_score1}")
        elif rand_word == 'rock':
            total_score2 = total_score1 - 1
            print("Paper wraps rock, YOU WON")
            print(f"SCORE: {total_score2}")
        elif rand_word == 'scissor':
            total_score3 = total_score2 + 1
            print("Scissor cuts paper, YOU LOST")
            print(f"SCORE: {total_score3}")
        else:
            print("Invalid input!") 
    elif guessed_word == 'scissor':
        if rand_word == 'scissor':
            total_score1 = score
            print("a tie")
            print(f"SCORE: {total_score1}")
        elif rand_word == 'paper':
            total_score2 = total_score + 1
            print("Scissor cuts paper, YOU WON")
            print(f"SCORE: {total_score2}")
        elif rand_word == 'rock':
            total_score3 = total_score2 - 1
            print("Rock destroys scissor, YOU LOST")
            print(f"SCORE: {total_score3}")
        else:
            print("Invalid input!")                           
    else:
        print("Invalid input!")

total_score = total_score1 + total_score2 + total_score3        


print(f"TOTAL SCORE: {total_score}")


