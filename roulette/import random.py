import random

def main():
    print("Welcome to the simple Roulette game!")

    # Store total winnings
    total_winnings = 0

    # Main game loop
    while True:
        name = input('Your name: ')
        print(f"Hello, {name}! Let's start the game.")

        while True:  # Inner loop for repeating the game without resetting the name
            # Display number choices
            print("Choose a number between 1 and 5:")
            for number in range(1, 6):
                print(f"|{number}|", end=' ')
            print()

            # Input player's guessed number
            try:
                guess = int(input('Enter your number (1 to 5): '))
                if guess < 1 or guess > 5:
                    print("Please enter a number between 1 and 5.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            # Input betting amount
            try:
                bet = int(input('Enter your bet amount: '))
                if bet <= 0:
                    print("Bet amount must be greater than 0.")
                    continue
                if bet > total_winnings and total_winnings > 0:
                    print(f"Your bet exceeds your total winnings ({total_winnings}). Your bet has been adjusted.")
                    bet = total_winnings
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            # Confirm whether to play
            confirmation = input('Are you sure you want to play? [yes/no]: ').strip().lower()
            if confirmation == 'yes':
                # Spin the roulette
                roulette_result = random.randint(1, 5)
                print(f"The spin result: {roulette_result}")

                if roulette_result == guess:
                    print(f"Your guess is correct! The answer is {roulette_result}. Congratulations, you win!")
                    total_winnings += bet * 2
                    print(f"You won: {bet * 2}. Your total winnings are now: {total_winnings}")
                else:
                    print(f"Your guess is incorrect. The answer is {roulette_result}. You lost.")
                    total_winnings -= bet
                    # Ensure total winnings do not go negative
                    if total_winnings < 0:
                        total_winnings = 0
                    print(f"You lost: {bet}. Your total winnings are now: {total_winnings}")

            elif confirmation == 'no':
                print("Alright, see you next time!")
                break
            else:
                print("Invalid choice. Returning to the bet input.")
                continue

            # Ask if the player wants to play again
            play_again = input("Do you want to play again? [yes/no]: ").strip().lower()
            if play_again != 'yes':
                print(f"Thank you for playing! Your total winnings: {total_winnings}")
                return  # Exit the program
            else:
                print("Restarting the game...")

# Run the game
if __name__ == "__main__":
    main()
