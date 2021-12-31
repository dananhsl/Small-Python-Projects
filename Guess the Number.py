import random
logo = '''
  _____                   __  __         _  __           __          
 / ___/_ _____ ___ ___   / /_/ /  ___   / |/ /_ ____ _  / /  ___ ____
/ (_ / // / -_|_-<(_-<  / __/ _ \/ -_) /    / // /  ' \/ _ \/ -_) __/
\___/\_,_/\__/___/___/  \__/_//_/\__/ /_/|_/\_,_/_/_/_/_.__/\__/_/   
                                                                  
'''
print(logo)
print("Welcome to the Number Guessing Game!")
numbers = list(range(1, 101))

def play_game():
    print("I'm thinking of a number between 1 and 100.\n You will have 5 tries to guess the number.")
    random_number = random.choice(numbers)
    print (f"Psst. The number is {random_number}")
    attempts = 0
    while attempts < 5:
        user_choice = int(input("Make a guess: "))
        attempts = attempts + 1
        if user_choice > random_number:
            if attempts < 5:
                print("That's too high. Try again.")
            else:
                print("That's too high.")
        elif user_choice < random_number:
             if attempts < 5:
                 print("That's too low. Try again.")
             else:
                 print("That's too low.")
        elif user_choice == random_number:
            break

    if user_choice == random_number:
        if attempts <=3:
            print(f"Well done. It only took you {attempts} attempts to guess the number!")
        if attempts > 3:
            print(f"Well done. It took you {attempts} attempts to guess the number.")

    if user_choice != random_number:
        print("You lose.")

    while input("Do you want to play again? Type 'y' for yes and 'n' for no.").lower() == "y":
        play_game()


play_game()
