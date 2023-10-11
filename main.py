import random
from hangman_art import logo
from hangman_words import word_list
from hangman_art import stages

print(logo)
chosen_word = random.choice(word_list).lower()
word_length = len(chosen_word)

end_of_game = False
lives = 6

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Adivinhe uma letra: ").lower()


    if guess in display:
        print(f"Você já tentou a letra '{guess}'.")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:

        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"Você perdeu. O time era {chosen_word.capitalize()}.")


    print(f"{' '.join(display)}")


    if "_" not in display:
        end_of_game = True
        print("\nVocê venceu!")

    print(stages[lives])