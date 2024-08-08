import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Maze Generator v0.0")

# Set the size of the window

# Create a 3x3 grid of labels
for i in range(10):
    for j in range(10):
        # Create a label for each cell
        label = tk.Label(root, text="", width=10, height=5, borderwidth=2, relief="groove",background="black")
        # Place the label in the grid
        label.grid(row=i, column=j)

# Run the application
root.mainloop()