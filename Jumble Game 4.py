import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Constants
MAX_TURNS = 10  # Set the maximum number of turns

# Function to choose a random word from the list
def choose():
    words = [
        "Snowflake", "Glacier", "Challenging", "Swaddling", "Emmanuel",
        "Ornament", "Reindeer", "Versatile", "frosty", "Implement",
        "Enhance", "Substantial", "Consistent", "Subtle", "ScrupuLous",
        "Rainbow", "Brutality", "Apparent", "Straightforward", "Moderate",
        "Methodology", "Component", "Accelerate", "Interpret", "Establish", "Perspective",
        "Troublesome", "Insightful", "Laborious","Burdensome"
    ]
    return random.choice(words)

# Function to jumble the chosen word
def jumble(word):
    return "".join(random.sample(word, len(word)))

# Check the answer
def check_answer():
    global turn
    global pp1, pp2, picked_word
    
    answer = answer_entry.get()
    
    if turn % 2 == 0:
        if answer.lower() == picked_word.lower():
            pp1 += 1
            score1_label.config(text=f"{p1name.get()} Score: {pp1}")
            messagebox.showinfo("Correct!", f"{p1name.get()}, that's correct!")
        else:
            messagebox.showinfo("Incorrect", f"Wrong answer. The correct word was {picked_word}.")
    else:
        if answer.lower() == picked_word.lower():
            pp2 += 1
            score2_label.config(text=f"{p2name.get()} Score: {pp2}")
            messagebox.showinfo("Correct!", f"{p2name.get()}, that's correct!")
        else:
            messagebox.showinfo("Incorrect", f"Wrong answer. The correct word was {picked_word}.")
    
    next_turn()

# Handle the next turn
def next_turn():
    global turn
    turn += 1
    if turn >= MAX_TURNS:
        end_game()  # Automatically end the game if max turns reached
    else:
        start_game()

# Start the game
def start_game():
    global picked_word
    picked_word = choose()
    jumbled_word = jumble(picked_word)
    
    word_label.config(text=jumbled_word)
    answer_entry.delete(0, tk.END)

    if turn % 2 == 0:
        player_turn_label.config(text=f"{p1name.get()}'s Turn")
    else:
        player_turn_label.config(text=f"{p2name.get()}'s Turn")

# End the game and declare the winner
def end_game():
    if pp1 > pp2:
        winner = p1name.get()
    elif pp2 > pp1:
        winner = p2name.get()
    else:
        winner = "It's a Draw"
    
    messagebox.showinfo("Game Over", f"Winner is: {winner}\n\nFinal Scores:\n{p1name.get()}: {pp1}\n{p2name.get()}: {pp2}")
    root.quit()

# Center the window on the screen
def center_window(root, width=800, height=600):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    
    root.geometry(f"{width}x{height}+{x}+{y}")

# Load and resize the background image to fit window dimensions dynamically
def load_background_image():
    global background_photo
    
    # Get window dimensions
    width, height = root.winfo_width(), root.winfo_height()
    
    background_image = Image.open("background.jpg")  # Ensure this file is in the same directory
    
    # Resize image to fill the window while maintaining aspect ratio
    background_image = background_image.resize((width, height), Image.LANCZOS)
    background_photo = ImageTk.PhotoImage(background_image)
    
    # Create a Label for the background image
    background_label.config(image=background_photo)
    background_label.image = background_photo

# Initialize the tkinter window
root = tk.Tk()
root.title("Jumble Words Game")

# Create a Label for the background image and set it to fill the entire window
background_label = tk.Label(root)
background_label.place(relwidth=1, relheight=1)

# Dynamically resize the background when window resizes
root.bind('<Configure>', lambda event: load_background_image())

# Center the window with larger size
center_window(root, 800, 600)

# Global variables
turn = 0
pp1 = 0
pp2 = 0
picked_word = ""

# Player names
p1name = tk.StringVar()
p2name = tk.StringVar()

# Frame for the game layout
game_frame = tk.Frame(root)
game_frame.pack(expand=True)

# Game title
title_label = tk.Label(game_frame, text="JUMBLE WORDS", font=("Helvetica", 32, "bold"), fg="black")
title_label.grid(row=0, column=0, columnspan=2, pady=20)

# Instructions
instructions_label = tk.Label(game_frame, text="Instructions:\nGuess the jumbled word.\nPlayers take turns.\nCorrect answers score a point.", font=("Helvetica", 14), justify="center")
instructions_label.grid(row=1, column=0, columnspan=2, pady=10)

# Widgets for player names and starting the game
tk.Label(game_frame, text="Player 1 Name:", font=("Helvetica", 14)).grid(row=2, column=0, padx=20, pady=10)
tk.Entry(game_frame, textvariable=p1name, font=("Helvetica", 14)).grid(row=2, column=1, padx=20, pady=10)

tk.Label(game_frame, text="Player 2 Name:", font=("Helvetica", 14)).grid(row=3, column=0, padx=20, pady=10)
tk.Entry(game_frame, textvariable=p2name, font=("Helvetica", 14)).grid(row=3, column=1, padx=20, pady=10)

start_button = tk.Button(game_frame, text="Start Game", font=("Helvetica", 14), command=start_game)
start_button.grid(row=4, column=0, columnspan=2, pady=20)

# Display jumbled word
word_label = tk.Label(game_frame, text="", font=("Helvetica", 28))
word_label.grid(row=5, column=0, columnspan=2, pady=20)

# Input for answer
tk.Label(game_frame, text="Your Answer:", font=("Helvetica", 14)).grid(row=6, column=0, padx=20, pady=10)
answer_entry = tk.Entry(game_frame, font=("Helvetica", 14))
answer_entry.grid(row=6, column=1, padx=20, pady=10)

# Submit button for the answer
submit_button = tk.Button(game_frame, text="Submit Answer", font=("Helvetica", 14), command=check_answer)
submit_button.grid(row=7, column=0, columnspan=2, pady=20)

# Score labels
score1_label = tk.Label(game_frame, text="Player 1 Score: 0", font=("Helvetica", 14))
score1_label.grid(row=8, column=0, padx=20, pady=10)

score2_label = tk.Label(game_frame, text="Player 2 Score: 0", font=("Helvetica", 14))
score2_label.grid(row=8, column=1, padx=20, pady=10)

# Label to show which player's turn it is
player_turn_label = tk.Label(game_frame, text="", font=("Helvetica", 18))
player_turn_label.grid(row=9, column=0, columnspan=2, pady=20)

# Button to end the game
end_button = tk.Button(game_frame, text="End Game", font=("Helvetica", 14), command=end_game)
end_button.grid(row=10, column=0, columnspan=2, pady=20)

# Run the tkinter loop
root.mainloop()
