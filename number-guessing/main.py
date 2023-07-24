import random

print("Welcome! You are going to guess the number I hold in my mind. I will tell you if you are off to down or up. Have fun!\n")

str_upper_bound = input("Before the start, tell me what you want the upper limit be? Lower limit is 0 (zero).\n")
n_upper_bound = int(str_upper_bound)

print("Lower limit(included): 0")
print("Upper limit(included): " + str_upper_bound)

print("Hmm!")
n_correct_number = random.randint(0,n_upper_bound)
print("Alright! I picked a number!")

print("Now! Give it a shot!")

while(True):
    n_number_guessed = int(input("Your Guess: "))

    if(n_correct_number == n_number_guessed):
        print("You did it! Congrats!!!")
        break
    elif(n_correct_number > n_number_guessed):
        print("Go up")
    else:
        print("Go down")