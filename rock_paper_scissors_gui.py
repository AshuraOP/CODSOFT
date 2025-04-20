import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        master.title("Rock, Paper, Scissors")

        self.user_score = 0
        self.computer_score = 0

        self.label = tk.Label(master, text="Choose Rock, Paper, or Scissors", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.score_label = tk.Label(master, text="Score - You: 0, Computer: 0", font=("Helvetica", 14))
        self.score_label.pack(pady=10)

        self.rock_button = tk.Button(master, text="Rock", command=lambda: self.play("rock"), width=10)
        self.rock_button.pack(side=tk.LEFT, padx=10)

        self.paper_button = tk.Button(master, text="Paper", command=lambda: self.play("paper"), width=10)
        self.paper_button.pack(side=tk.LEFT, padx=10)

        self.scissors_button = tk.Button(master, text="Scissors", command=lambda: self.play("scissors"), width=10)
        self.scissors_button.pack(side=tk.LEFT, padx=10)

        self.result_label = tk.Label(master, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=20)

        self.play_again_button = tk.Button(master, text="Play Again", command=self.reset_game, state=tk.DISABLED)
        self.play_again_button.pack(pady=10)

    def play(self, user_choice):
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        self.label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}")

        winner = self.determine_winner(user_choice, computer_choice)

        if winner == "tie":
            self.result_label.config(text="It's a tie!")
        elif winner == "user":
            self.result_label.config(text="You win!")
            self.user_score += 1
        else:
            self.result_label.config(text="You lose!")
            self.computer_score += 1

        self.update_score()
        self.play_again_button.config(state=tk.NORMAL)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            return "user"
        else:
            return "computer"

    def update_score(self):
        self.score_label.config(text=f"Score - You: {self.user_score}, Computer: {self.computer_score}")

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.update_score()
        self.result_label.config(text="")
        self.label.config(text="Choose Rock, Paper, or Scissors")
        self.play_again_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()