import tkinter as tk
from tkinter import messagebox

class MyGUI:
    
    def __init__(self):
        # Create window 
        self.window = tk.Tk()
        self.window.geometry("800x500")
        self.window.title("Foltz Bakery - Order Management System")

        # MENU BAR
        self.menu_bar = tk.Menu(self.window)
        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Close", command=self.on_close)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Force Close", command=exit)
        # Action menu
        self.action_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.action_menu.add_command(label="Show Message", command=self.show_message)

        
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.menu_bar.add_cascade(label="Action", menu=self.action_menu)
        self.window.config(menu=self.menu_bar)

        # GUI
        self.title_label = tk.Label(self.window, text="Enter a message", font=("Arial", 18))
        self.title_label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.window, font=("Arial", 16), height=5)
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.window, text="Show messagebox", font=("Arial", 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.window, text="Show message", font=("Arial", 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        # Run window
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.window.mainloop()
    
    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END)) # this gets everything
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))

    def shortcut(self, event):
        if event.state == 4 and event.keycode == 13:
            self.show_message()
    
    def on_close(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.window.destroy()

MyGUI()