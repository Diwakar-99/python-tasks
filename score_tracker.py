# Global variable to keep track of the player's total score
total_score = 0

def play_round():
    global total_score  # Use the global keyword to modify the global variable

    # Local variable to store the score for this round
    round_score = int(input("Enter the score for this round: "))

    # Update the total score
    total_score += round_score

# Simulate multiple rounds
num_rounds = int(input("Enter the number of rounds to play: "))
for _ in range(num_rounds):
    play_round()

# Display the total score at the end
print(f"\nTotal Score after {num_rounds} rounds: {total_score}")
 
