import hangman_visua
from words import *
import random
import string
from hangman_visua import *

def get_word(word):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letter = set()

    lives = 6

    # Getting user input
    while len(word_letters) > 0 and lives > 0:
        #letter used
        # ' '.join('a','b','c') --> ['a b c']

        print(f'You have "{lives}" chances to guess my word')
        print('Letters you used : ',' '.join(used_letter))

        # print(user_letter)
        word_list = [letter if letter in used_letter else '-' for letter in word]
        # print(lives_visual_dict[lives])
        print('\nCurrent word',' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet:
            used_letter.add(user_letter)
            if user_letter in word_letters :
                word_letters.remove(user_letter)
                print('')

            else:

                print(lives_visual_dict[lives])
                lives-=1
                print(f'you entered {user_letter} not in my word\n')

        elif user_letter in used_letter:
            print('\nYou have already used this letter,Guess another letter\n')
        else:
            print("\nThis is not valid letter\n")

    if lives == 0:
        print(lives_visual_dict[lives])
        print('You lost! chances are over.')
    else:
        print('Yay..you guessed my word, that is :', word)


# get_word(words)
hangman()