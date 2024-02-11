# No need to install, tkinter is part of python
import tkinter as tk

# Creating a window
window = tk.Tk()

# Size of the window
window.geometry("800x500")
window.title("Feltz Bakery - Order Management System")

# WIDGETS
#label
label = tk.Label(window, text="System Controls", font=("Arial", 18))
label.pack(padx=20, pady=20) # total of 40
# Textbox (With multiline features)
textbox = tk.Text(window, height=3, font=("Arial", 18)) # three lines
textbox.pack(padx=15)
# Entry field (no multiline features)
entry = tk.Entry(window, text="Default text")
entry.pack(pady=10)
# Button
button = tk.Button(window, text="Press me!", command=lambda: print("Button clicked!"))
button.pack()

# FRAME
button_frame = tk.Frame(window)
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)

button1 = tk.Button(button_frame, text="1", font=("Arial", 18))
button1.grid(row=0, column=0, sticky=tk.W+tk.E, padx=20) # west and east sticky
button2 = tk.Button(button_frame, text="2", font=("Arial", 18))
button2.grid(row=0, column=1, sticky=tk.W+tk.E, padx=20) # west and east sticky
button3 = tk.Button(button_frame, text="3", font=("Arial", 18))
button3.grid(row=0, column=2, sticky=tk.W+tk.E, padx=20) # west and east sticky
button4 = tk.Button(button_frame, text="1", font=("Arial", 18))
button4.grid(row=1, column=0, sticky=tk.W+tk.E, padx=20) # west and east sticky
button5 = tk.Button(button_frame, text="2", font=("Arial", 18))
button5.grid(row=1, column=1, sticky=tk.W+tk.E, padx=20) # west and east sticky
button6 = tk.Button(button_frame, text="3", font=("Arial", 18))
button6.grid(row=1, column=2, sticky=tk.W+tk.E, padx=20) # west and east sticky

button_frame.pack(fill="x",padx=150, pady=50)

# Placing manually
another_button = tk.Button(window, text="Hello")
another_button.place(x=100, y=100, height=100, width=100)



# Running the window
window.mainloop()