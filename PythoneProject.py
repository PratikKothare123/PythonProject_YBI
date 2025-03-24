import tkinter as tk
import random

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Scores
user_score = 0
computer_score = 0

# Function to handle user choice
def play(choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)
    result = determine_winner(choice, computer_choice)

    # Update the result label
    result_label.config(text=f"Your Choice: {choice}\nComputer's Choice: {computer_choice}\nYour Score: {user_score}\nComputer Score: {computer_score}")

# Function to determine winner
def determine_winner(user_choice, computer_choice):
    global user_score, computer_score

    if user_choice == computer_choice:
        return "Tie"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        user_score += 1
        return "You win"
    else:
        computer_score += 1
        return "Computer wins"

# Creating the GUI window
root = tk.Tk()
root.title("Rock Paper Scissors Game")

# Buttons for Rock, Paper, Scissors
rock_button = tk.Button(root, text="Rock", command=lambda: play("Rock"), bg="lightblue", width=10)
rock_button.pack()

paper_button = tk.Button(root, text="Paper", command=lambda: play("Paper"), bg="lightgray", width=10)
paper_button.pack()

scissors_button = tk.Button(root, text="Scissors", command=lambda: play("Scissors"), bg="lightgreen", width=10)
scissors_button.pack()

# Label for displaying results
result_label = tk.Label(root, text="Your Choice: \nComputer's Choice: \nYour Score: 0\nComputer Score: 0", bg="yellow", width=40, height=5)
result_label.pack()

# Run the GUI application
root.mainloop()
