import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("Maze Generator v0.1")

# Set variables

gridWidth=8
gridHeight=8

# Generate a random row using the random.randint function
def generateRow():
    return format(random.randint(0,255),'08b') #Return the binary for a random number

# Create a 3x3 grid of labels
for i in range(gridHeight):
    randomRow=generateRow() #Call the random int function
    for j in range(gridWidth):
        # Create a label for each cell
        print(randomRow[j])
        if((randomRow[j]=='0') or (i==0 and j==0) or (i==gridHeight-1 and j==gridWidth-1)): #Make the pixel black or white depending on the bit, also set the first and last pixel to white
            label = tk.Label(root, text="", width=10, height=5, borderwidth=2, relief="groove",background="white")
        else:
            label = tk.Label(root, text="", width=10, height=5, borderwidth=2, relief="groove",background="black")
        # Place the label in the grid
        label.grid(row=i, column=j)

# Run the application
root.mainloop()