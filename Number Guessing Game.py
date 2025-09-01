import random

lowest_num = 1
highest_num = int(100)
guesses = 0

answer = random.randint(lowest_num, highest_num)
#  print(answer)

print("------------------------------------------------------------------------------------")
print("Number Guessing Game")
print("------------------------------------------------------------------------------------")
print(f"Select a Number between {lowest_num} and {highest_num} ")

while True:
    print("------------------------------------------------------------------------------------")
    guess = input(f"Enter your Guessing NUmber between {lowest_num} and {highest_num} : ")
    print("------------------------------------------------------------------------------------")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess > highest_num or guess < lowest_num :
            print("Your Guessed Number is Out of Range.")
            print("                                                                                    ")
            print(f"Select a Number between {lowest_num} and {highest_num} ")
        elif guess > answer:
            print("Too high! Try Again ")
            print("                                                                                    ")
            print(f"Select a Number between {lowest_num} and {highest_num} ")
        elif guess < answer:
            print("Too Low! Try Again ")
            print("                                                                                    ")
            print(f"Select a Number between {lowest_num} and {highest_num} ")
        elif guess == answer:
            print("\t CORRECT !")
            print("                                                                                    ")
            print(f"Number of Guesses is {guesses}")
            print("                                                                                    ")
            print(f"Your Guessed Number is {guess}")
            break
        else:
            break
    else:
        print("Invaild Guess!")
        print("                                                                                    ")
        print(f"Select a Number between {lowest_num} and {highest_num} ")
    