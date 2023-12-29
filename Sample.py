import tkinter as tk
import random

def rock_paper_scissors(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    result = ""

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
    else:
        result = "Computer wins!"

    lbl_result.config(text=f"Computer chose: {computer_choice}\n{result}")

# Creating the GUI
root = tk.Tk()
root.title("Rock Paper Scissors Game")

lbl_instructions = tk.Label(root, text="Choose Rock, Paper, or Scissors")
lbl_instructions.pack()

btn_rock = tk.Button(root, text="Rock", command=lambda: rock_paper_scissors("Rock"))
btn_rock.pack()

btn_paper = tk.Button(root, text="Paper", command=lambda: rock_paper_scissors("Paper"))
btn_paper.pack()

btn_scissors = tk.Button(root, text="Scissors", command=lambda: rock_paper_scissors("Scissors"))
btn_scissors.pack()

lbl_result = tk.Label(root, text="")
lbl_result.pack()

root.mainloop()
