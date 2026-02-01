import random

#list of predefined word
word_list = ["python","intern","coding","program","alpha"]

#Randomly choose a word
secret_word = random.choice(word_list)
guessed_letters = []
attempts = 6

print("Welcome to Hangman Game!")
print("Guess the word, one letter at a time.")
print("_" * len(secret_word))

while attempts > 0:
    guess = input("Enter a letter: ").lower()
    
    #check for valid input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue
    
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    
    guessed_letters.append(guess)
    
    if guess in secret_word:
        print("Good guess!")
    else:
        attempts -= 1
        print(f"Wrong guess! Attempts left:{attempts}")
        
    #Display current progress
    display_word =" "
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += " _ "
    print(display_word)
    
    #Check if user won
    if "_" not in display_word:
        print("Congratulationss! You guessed the word correctly.")
        break
    #if attempts are finished
    if attempts == 0:
        print(f"Game Over! The word was '{secret_word}'.")
        
            
