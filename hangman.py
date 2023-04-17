'''
The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the word.
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters before the game is over.
'''

# Output
'''
You have 6 tries left.
Used letters:
Word: _ _ _ _
Guess a letter: a

You have 6 tries left.
Used letters: a
Word: _ a _ a
Guess a letter: j

You have 6 tries left.
Used letters: j a
Word: j a _ a
Guess a letter: v
You guessed the word java !
'''
import sys
import string


def hangman(word):
    tries = 6
    guessed = False
    used_letters = []
    matched_letters = []

    while tries > 0: 

        print("\n")
        print(f"You have {tries} tries left.")
        print(f"Used letters: {' '.join(used_letters)}")
        print("Word: ", " ".join([("_" if l not in matched_letters else l) for l in word]))

        try:
            guess = str(input("Guess a letter: "))

            if len(guess) > 1: raise ValueError

            elif guess in string.digits or guess in string.punctuation:
                raise ValueError

            elif guess in used_letters:
                print("You already guessed this letter. Choose a different one.")

            elif str.lower(guess) in word:
                matched_letters.append(str.lower(guess))
                used_letters.append(str.lower(guess))

            else:
                print(f"The letter '{guess}' is not in the word")
                used_letters.append(guess)
                tries -= 1

                if tries == 0:
                    return print("You loose. :(")

            if all(letter in matched_letters for letter in word):
                return print(f"You guessed the word '{word}'.\n")

        except ValueError:
            print("You can only enter a letter [a-z].")


if __name__ == "__main__":
    hangman(word=str.lower(sys.argv[1]))

