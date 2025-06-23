import random

# Predefined list of words
words = ["apples", "banana", "cherry", "grapes", "orange"]

# Randomly select a word
word = random.choice(words)
hidden_word = ["_"] * len(word)
guessed_letters = []
tries = 6

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.\n")

# Main game loop
while tries > 0 and "_" in hidden_word:
    print("Word:", " ".join(hidden_word))
    guess = input("🔤 Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single valid letter.\n")
        continue

    # Already guessed
    if guess in guessed_letters:
        print("🔁 You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in word:
        print("✅ Good job!\n")
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
    else:
        tries -= 1
        print("❌ Wrong guess! Tries left:", tries, "❤️\n")

# Final result
if "_" not in hidden_word:
    print("\n🏆 Congratulations! You guessed the word:", word)
    print("🎉 You Win!")
else:
    print("\n💀 Game Over. The word was:", word)
    print("😢 Better luck next time!")
