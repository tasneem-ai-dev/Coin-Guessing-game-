import random 
def coin_toss_randint():
    random_variable=random.randint(0,1)
    if random_variable==0:
        return "Heads"
    else:
        return "Tails"

def coin_toss_random():
    random_variable=random.random()
    if random_variable < 0.5 :
        return "Heads"
    else :
        return "Tails" 
####_________main_code
print(f"Welcome to the Coin Guessing Game!\nChoose a method toss the coin: ")           
print(f"1. Using random.randint()\n2. Using random.random()")
user_choice=int(input("Enter your choice (1 or 2): "))
#Check the user's choice and call the appropriate function
if user_choice==1:
    result=coin_game_random_randint()
elif user_choice==2:
    result=coin_game_random_random()
else:
    print("Invaild choice. Please select either 1 or 2")        
if user_choice ==1 or user_choice ==2:
    user_guess=input("Enter your guess (Heads or Tails): ").capitalize()    
    if user_guess == result:
        print(f"Congratulations! You won!\nThe computer's coin toss result was: {result}.")
    else:
        print(f"Sorry, you lost!\nThe computer's coin toss result was: {result}.")
