from random_word import RandomWords
from drawings import *

def generate_word():
    r = RandomWords()
    return r.get_random_word()
    # this function returns a random word string

def start_game():
    word = generate_word().lower()
    current_status = ["_"] * len(word) # stores the current status of game word
    used_letters = [] # stores ALL letters guessed
    num_mistakes = 0
    is_complete = False
    letters = "qwertyuiopasdfghjklzxcvbnm"
    print(word)

    print("Your word is " + str(len(word)) + " words long.")

    for space in current_status: # prints the current status
        print(space, end=" ")

    while num_mistakes < 10 and not is_complete:
        guessed_letter = (input("\nPlease enter a letter: ")).lower()

        if guessed_letter not in used_letters and guessed_letter in letters:
            used_letters.append(guessed_letter)
            if guessed_letter in word:
                for x in range(0, len(word)):
                    if word[x] == guessed_letter:
                        current_status[x] = guessed_letter # set the corresponding index to the letter
                print(" ")
                print_hangman(num_mistakes, current_status, used_letters, True)

                num_correct = 0
                for let in current_status:
                    if let != "_":
                        num_correct += 1 # if there is still a _ in the status, no win yet
                if num_correct == len(word):
                    is_complete = True
                    break
            else:
                print("That was not in the word!")
                num_mistakes += 1
                print(" ")
                print_hangman(num_mistakes, current_status, used_letters, False)
        else:
            print("You already used this letter or it is not a letter :( ")

    if num_mistakes == 0: 
        print("You're a master!")
        
    return is_complete

def print_hangman(mistakes, status, used_letters, correct):
    if mistakes == 1:
        one()
    elif mistakes == 2:
        two()
    elif mistakes == 3:
        three()
    elif mistakes == 4:
        four()
    elif mistakes == 5:
        five()
    elif mistakes == 6:
        six()
    elif mistakes == 7:
        seven()
    elif mistakes == 8:
        eight()
    elif mistakes == 0:
        start()
    else:
        game_over()

    for z in status:
        print(z, end=" ")

    print(" ")
    print("Used Letters: ", end=" ")
    for a in used_letters:
        print(a, end=", ")

    if correct:
        return "Good Job!"
    else:
        return "Try Again!"

print("Lets Play HangMan!")

win = start_game()

if win:
    print("\nWOOOO BABY!!!!!!!")
else:
    print("\nMaybe Next Time")
    
    
