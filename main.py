import random

from hangman_words import word_list

chosen_word = random.choice(word_list)

lives = 6
print(f"Random choose is {chosen_word}")
from hangman_art import logo

print(logo)
display = []
word_len = len(chosen_word)
for _ in range(word_len):
    display += "_"
print(display)
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win")

    from hangman_art import stages

    print(stages[lives])
