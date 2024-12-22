import random

def jumble_word(word):
    # Convert the word into a list of characters and shuffle them
    jumbled_word = list(word)
    random.shuffle(jumbled_word)
    return ''.join(jumbled_word)

def play_word_jumble():
    words = ['python', 'hangman', 'computer', 'keyboard', 'mouse', 'gamer', 'programming']
    word_to_guess = random.choice(words)
    jumbled_word = jumble_word(word_to_guess)

    print("Welcome to Word Jumble!")
    print("Unscramble the letters to form a word.")
    print("Jumbled word:", jumbled_word)

    guess = input("Your guess: ").lower()

    while guess != word_to_guess:
        print("Incorrect guess. Try again!")
        guess = input("Your guess: ").lower()

    print("Congratulations! You've guessed the word correctly:", word_to_guess)

play_word_jumble()
