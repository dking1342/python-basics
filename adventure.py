
# adventure game
'''
data types
str "hello"
int 8, 9, -10
float -1.2, 2.4
bool True False
'''

def check_health(points):
    if points > 0:
        return True
    else:
        return False

adventures = [
    {
        "question":"You reach a lake, do you swim across or walk around (swim/walk)? ",
        "answer": "walk",
        "bonus": 2,
        "incorrect": 5
    },
    {
        "question":"You reach a lake, do you swim across or walk around (swim/walk)? ",
        "answer": "walk",
        "bonus": 2,
        "incorrect": 5
    },
    {
        "question":"You reach a lake, do you swim across or walk around (swim/walk)? ",
        "answer": "walk",
        "bonus": 2,
        "incorrect": 5
    }
]

print("Welcome to the game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

# using format
# output = "Hello {name} you are {age} years old".format(name = name,age = age)
# print(output)

if age >= 18:
    print("You can play the game")
    will_play = input("Do you want to play? (yes/no) ")
    
    if will_play.lower() == "yes":
        health_points = 10
        steps = 1
        print("Let's play!")
        print("You have", health_points, "points")

        for adventure in adventures:
            if steps <= len(adventures) and health_points > 0:
                user_input = input(adventure["question"])
                if user_input.lower() == adventure["answer"]:
                    print("Good choice... you have gained", adventure["bonus"], "points")
                    health_points += int(adventure["bonus"])
                    steps += 1
                else:
                    health_points -= int(adventure["incorrect"])
                    if health_points <= 0:
                        print("You have no health points left. You have lost. Please try again!")
                        break
                    else:
                        print("That was an ill fated choice. You now have", health_points, "points")
                        steps += 1                        
            if steps == len(adventure) and health_points > 0:
                print("You reached the end of the journey alive. Good job!")
                break

        # manual way of going through the game
        # user_direction_choice = input("First choice... Left or Right (left/right)? ")
        # if user_direction_choice.lower() == "left":
        #     user_answer = input("Nice... you reach a lake... do you swim across or walk around (swim/walk)? ")

        #     if user_answer.lower() == "walk":
        #         pass
        #     elif user_answer.lower() == "swim":
        #         pass
        # else:
        #     health_points -= 10
        #     print("You fell down and died")



    else:
        print("Thanks for visiting. Bye!")
# else if functionality
# elif age < 18 and age >= 13:
#     print("You can play but with adult supervision")
else:
    print("You are too young to play")
