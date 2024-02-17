import tkinter as tk

# Create window
root = tk.Tk()
root.geometry("1200x650")
root.title("Foltz Bakery - Order Management System")
root.config(bg="white")
root.resizable(0,0)

# FRAMES
ItemListFrame = tk.Frame(root, bd=5, width=400, relief=tk.RIDGE, bg="skyblue")
ItemListFrame.pack(side=tk.RIGHT, fill=tk.Y)

ButtonFrame = tk.Frame(root, bd=5, width=800, padx=4, pady=4, relief=tk.RIDGE, bg="crimson")
ButtonFrame.pack(side=tk.LEFT, fill=tk.Y)

"""
# LABELS
Food = tk.Label(ButtonFrame, font=('Arial', 14, 'bold'), text="Food", bd=5)
Food.grid(row=0, column=0, padx=5)
"""

# Run window
root.mainloop()