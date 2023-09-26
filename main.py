import tkinter as tk
import pygame

# Initialize Pygame
pygame.init()

# Create a Pygame window (it won't be visible)
pygame.display.set_mode((1, 1))

# Create a Tkinter window
window = tk.Tk()
window.title("Tkinter and Pygame Demo")
window.geometry("400x400")

# Create a label in the Tkinter window
label = tk.Label(window, text="Welcome to the Tkinter and Pygame Demo!")
label.pack()

# Function to play a sound using Pygame
def play_sound():
    pygame.mixer.Sound("sound.wav").play()

# Create a button to play a sound
sound_button = tk.Button(window, text="Play Sound", command=play_sound)
sound_button.pack()

# Run the Tkinter main loop
window.mainloop()
