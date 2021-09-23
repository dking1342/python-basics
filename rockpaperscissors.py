import random

def play():
    user = input("choose r for rock, p for paper or s for scissors: ")
    computer = random.choice(["r","p","s"])

    if user == computer:
        return "tie"
    if is_win(user,computer):
        return "You won!"

    return "You lost!"

def is_win(player,computer):
    if player == "r" and computer == "s" or player == "s" and computer == "p" or player == "p" and computer == "r":
        return True

print(play())