from math import log
import requests
import random
import string

# calling api to select a word
url = "https://www.randomlists.com/data/words.json"
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}
response = requests.get(url,headers=headers,timeout=5)
word_list = response.json()["data"]

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_word(word_list)
    word = word.upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print("you have", lives, "life left. you used the letters: ", " ".join(used_letters))
        word_lists = [letter if letter in used_letters else "-" for letter in word]
        print("current word: "," ".join(word_lists))

        user_letter = input("guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("the letter", user_letter, "was in the word")
            else:
                lives -= 1
                print("letter not in the word")
        elif user_letter in used_letters:
            print("you already used that letter")
        else:
            print("you used an invalid letter")
    
    if lives == 0:
        print("you died. the word was", word.lower())
    else:
        print("you guessed the word: ", word.lower(), "!!")

hangman()

# user_guess_count = 5
# user_guesses = ""
# user_guess = input("guess a letter: ")

# for letter in random_word:
#     print(letter)


