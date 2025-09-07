import random

word_list = ("aardvark", "baboon", "camel")
chosen_word = random.choice(word_list)

lives_remaining = 5
correct_guesses = []

while lives_remaining > 0:
    user_input = input("Guess a letter: ")

    if user_input in chosen_word:
        print("Yes, you are correct, please continue")
        correct_guesses.append(user_input)
    else:
        lives_remaining -= 1
        print(f"Try again. You have {lives_remaining} lives remaining")

    all_guessed = True
    for letter in chosen_word:
        if letter not in correct_guesses:
            all_guessed = False
            break

    if all_guessed:
        print(f"🎉 Congrats! You won. The word was '{chosen_word}'")
        break

if lives_remaining < 1:
    print("💀 Oops, you lose.")




