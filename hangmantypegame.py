import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

lives_remaining = 5
correct_guesses = []

print("Welcome to Hangman!\n")

while lives_remaining > 0:
    # Show current progress
    display_word = [letter if letter in correct_guesses else "_" for letter in chosen_word]
    print("Current word: " + " ".join(display_word))

    user_input = input("Guess a letter: ").lower()

    if user_input in chosen_word:
        if user_input not in correct_guesses:
            correct_guesses.append(user_input)
            print("✅ Yes, you are correct, please continue.")
        else:
            print("⚠️ You've already guessed that letter.")
    else:
        lives_remaining -= 1
        print(f"❌ Try again. You have {lives_remaining} lives remaining.")

    # Check if all letters are guessed
    if all(letter in correct_guesses for letter in chosen_word):
        print("\n🎉 You win! The word was:", chosen_word)
        break

if lives_remaining < 1:
    print("\n💀 Oops, you lose. The word was:", chosen_word)






