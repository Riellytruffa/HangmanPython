import random
from words import words
import string 



def get_valid_word(words): 
    word = random.choice(words)  # chooses random word from words.py file 
    while '-' in word or ' ' in word: 
        word = random.choice(words)
        
        
        return word.upper()

def hangman(): 
    word = get_valid_word(words) 
    word_letters = set(word)  # Amount of letters
    alphabet = set(string.ascii_uppercase) 
    used_letters = set()  # Used Letters

    lives = 6

    
    while len(word_letters) > 0 and lives > 0: 
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print('Current word: ', ' '.join(word_list))
    
    
    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(used_letters)
                
        else:
                lives = lives - 1 
                print('Letter is not in the word!')
    
    
    elif user_letter in used_letters:
        print('You have already used that character. Please try again.') # User uses same character
    
    
    else:
        print('Invalid character. Please try again') 
    
    if lives == 0:
     print('You died, sorry. The word was', word)
    print('You guessed the word', word, '!!')


user_input = input('Type something: ')
print(user_input)



