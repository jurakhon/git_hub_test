import random


words = {
"github": "is a web-based interface that uses Git, the open source version control software that lets multiple people make separate changes to web pages at the same time.",
"google": "is an internet search engine. It uses a proprietary algorithm that’s designed to retrieve and order search results to provide the most relevant and dependable sources of data possible.",
"instagram": "is a free photo and video sharing app available on iPhone and Android. People can upload photos or videos to our service and share them with their followers or with a select group of friends."
}


word, explanation = random.choice(list(words.items()))
guessed = ["_"] * len(word)
attempts = 10

print("Welcome to the POLY CHUDES!")
print(f"Hint: {explanation}")

while attempts > 0:
    print("Word: ", *guessed)
    guess = input("Guess a letter: ").lower()

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print(f"NO. {attempts} attempts left.")

    if "_" not in guessed:
        print(f"Congratulations! You guessed the word: {word}")
        break
else:
    print(f"You lost. The word was: {word}")