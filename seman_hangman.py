def say_hello():
    print("hello")

say_hello()
    
def hangman(word, guessed_letter):
    placeholder = ''
    for letter in word:
        if letter in guessed_letter:
            placeholder += letter
        else:
            placeholder += '-'
    return placeholder

word = input("Enter a word: ").lower()  

tries = 0
guessed_letters = []

while tries < 6:
    guess = input("Enter one letter or type quit end the game: ").lower()

    if guess == 'quit':
        print("You quit the game!")
        break

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print(f"You've already guessed '{guess}' try again.")
        continue

    guessed_letters.append(guess)

    hangman_display = hangman(word, guessed_letters)
    print(hangman_display)

    if hangman_display == word:
        print("Congratulations you guessed the word!")
        break

    tries += 1

if tries == 6:
    print(f"You've used all 6 tries. The word was '{word}'.")
    
