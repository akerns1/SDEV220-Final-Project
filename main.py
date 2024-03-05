import tkinter as tk
from tkinter import font
from functools import partial
from item import Item
from order import Order
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# AK2024 - List of available items
item_types: list = [
    ("Jalapeño Bread", 3.49), 
    ("Cinnamon Bread", 3.49), 
    ("Donut", 1.99), 
    ("Latte", 2.49), 
    ("Cinnamon Roll", 2.49),
    ("Cookie", 2.49),
    ("Danish", 1.99),
    ("Cream Cheese Cups", 2.75),
    ("Cupcake", 3.25),
    ("Mini Pie", 4.99),
    ("Coffee Cake", 3.99),
    ("Cake", 14.99)
]

# WHP2024 
class BakerySystem():
    def __init__(self, root):
        self.root = root
        self.root.title("Foltz Bakery - Order Management System")

        # Run window
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.create_menu()

        # Single order for testing
        self.test_order: Order = Order()

        # AK2024 - Creation of two frames and the items
        self.items_frame = tk.Frame(self.root, bg='gray', highlightbackground='black', highlightthickness=3, padx=10, pady=10)
        self.items_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

        self.order_frame = tk.Frame(self.root, bg='gray', highlightbackground='black', highlightthickness=3, padx=10, pady=10)
        self.order_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # AK2024 - Add widgets to Items Frame 
        self.label_items = tk.Label(self.items_frame, text="Item Menu", font=('Helvetica 16 bold'), bg='lightgray')
        self.label_items.grid(row=0, column=2, sticky="ew", pady=10)

        # AK2024 - Add widgets to Current Order Frame
        self.label_order = tk.Label(self.order_frame, text="Current Order", font=('Helvetica 16 bold'), bg='lightgray')
        self.label_order.pack(pady=10)

        # WHP2024 - Make a scrollbar object
        
        self.listbox = tk.Listbox(self.order_frame, font=("Times", 25), selectmode=tk.EXTENDED)
        self.scrollbar = tk.Scrollbar(self.listbox, orient=tk.VERTICAL)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.listbox.pack(padx=10,fill=tk.BOTH, expand=True)

        # WHP2024 Link it to the listbox.
        self.scrollbar.config(command=self.listbox.yview)

        # AK2024 - Delete button
        self.delete_button = tk.Button(self.order_frame, text="Delete", command=self.delete_item, font=('Helvetica 16'))
        self.delete_button.pack(pady=10)

        # AK2024 - Total Price display
        self.total_price = tk.DoubleVar()
        self.total_price.set(0.0)
        self.total_label = tk.Label(self.order_frame, text="Order Total:", font=('Helvetica 16 bold'))
        self.total_label.pack()
        
        self.total_display = tk.Label(self.order_frame, textvariable=self.total_price, font=('Helvetica 16 bold'))
        self.total_display.pack()

        # WHP2024 & AK2024 - Generate buttons from list of available items in a grid pattern
        num_items = len(item_types)
        num_columns = 3
        num_rows = -(-num_items // num_columns)

        for index, item in enumerate(item_types):
            # Calculate the position in the grid
            row = index // num_columns
            col = index % num_columns

            # WHP2024 Make images
            # Check if the file exists
            if os.path.exists(f"./images/{item[0]}.jpg"):
                print(f"./images/{item[0]}.jpg exists")

                # Load the image using Pillow
                image = Image.open(f"./images/{item[0]}.jpg")
                # Resize the image as needed
                image = image.resize((75, 75))  # Adjust the size as per your requirements

                # Convert the image to PhotoImage
                tk_image = ImageTk.PhotoImage(image)

                # Make button with the image
                button = self.create_button(self.items_frame, tk_image, item[0], item[1])
                button.image = tk_image  # Keep a reference to avoid garbage collection
                button.grid(sticky="nsew", pady=5, padx=5, row=row+1, column=col+1)
            else:
                print(f"./images/{item[0]}.jpg does not exist")

    # Creating buttons
    def create_button(self, root: tk.Frame, image: ImageTk.PhotoImage, name: str, price: float) -> None:
        button = tk.Button(
            self.items_frame, 
            image=image, 
            compound="top", 
            bg="#f0f0f0", 
            font=("Times", 18), 
            fg="#000000", 
            justify="center", 
            text=f"{name}: ${price}",
            command=partial(self.add_item, f"{name}", price)
        )
        
        return button
                
    # WHP2024 - Adding items
    def add_item(self, name: str, price: float) -> None:
        item: Item = Item(name, price, 1)
        self.test_order.items.append(item)
        
        # Update total price
        self.total_price.set(self.total_price.get() + item.get_price())
        rounded_value = round(self.total_price.get(), 2)
        self.total_price.set(rounded_value)

        self.update_listbox()

    # AK2024 Delete button
    def delete_item(self):
        # Reverse the order of selected indices to avoid index changes affecting subsequent deletions
        selected_indices = sorted(self.listbox.curselection())

        for index in reversed(selected_indices):
            deleted_item = self.test_order.items[index]
            self.test_order.items.pop(index)
            
            # Update total price
            self.total_price.set(self.total_price.get() - deleted_item.get_price())
            rounded_value = round(self.total_price.get(), 2)
            self.total_price.set(rounded_value)
        
        # Update display
        self.update_listbox()
    
    def update_listbox(self):
        # Clear listbox
        self.listbox.delete(0, tk.END)

        # Add items back
        for item in self.test_order.items:
            self.listbox.insert(tk.END, f"{item.get_name()}: {item.get_price()}")

    def create_menu(self):
        # WHP2024 Menu bar
        self.menu_bar = tk.Menu(self.root)
        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Close", command=self.on_close)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Force Close", command=exit)
        # Action menu
        self.action_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.action_menu.add_command(label="Clear order", command=self.clear_order)
        
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.menu_bar.add_cascade(label="Action", menu=self.action_menu)
        self.root.config(menu=self.menu_bar)

    def on_close(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()

    def clear_order(self):
        # Clear the list of items in the order
        self.test_order.items.clear()

        # Reset the total price to 0
        self.total_price.set(0.0)

        # Update the listbox to reflect the cleared order
        self.update_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = BakerySystem(root)
    root.geometry("1200x600")
    root.mainloop()