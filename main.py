import tkinter as tk
from tkinter import font
from functools import partial
from item import Item
from order import Order

class BakerySystem():
    def __init__(self, root):
        self.root = root
        self.root.title("Foltz Bakery - Order Management System")
        root.resizable(width=False, height=False)

        # Single order for testing
        self.test_order: Order = Order()

        # AK2024 - List of available items
        self.item_types: list = [
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

        # AK2024 - Creation of two frames and the items
        self.items_frame = tk.Frame(self.root, bg='lightblue', padx=10, pady=10)
        self.items_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.order_frame = tk.Frame(self.root, bg='gray', padx=10, pady=10, width=150)
        self.order_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=False)

        # AK2024 - Add widgets to Items Frame 
        self.label_items = tk.Label(self.items_frame, text="Item Menu", font=('Helvetica 16 bold'), bg='lightblue')
        self.label_items.grid(row=0)

        # AK2024 - Add widgets to Current Order Frame
        self.label_order = tk.Label(self.order_frame, text="Current Order", font=('Helvetica 16 bold'), bg='lightgray')
        self.label_order.pack(pady=10)

        self.listbox = tk.Listbox(self.order_frame, font=("Times", 20), selectmode=tk.EXTENDED)
        self.listbox.pack(padx=10,pady=10,fill=tk.BOTH, expand=True)

        # AK2024 - Delete button
        self.delete_button = tk.Button(self.order_frame, text="Delete", command=self.delete_item)
        self.delete_button.pack()

        # WHP2024 - Loop through item list
        #for item_name, item_price in self.item_types:
        #    self.create_button(self.items_frame, item_name, item_price)

        num_columns = 3
        num_rows = 4

        for cols in range(num_columns):
            for rows in range(num_rows):
                # Calculate index
                index = rows * num_columns + cols
                item = self.item_types[index]

                # Make button
                button = self.create_button(self.items_frame, f"{self.item_types[index][0]}", self.item_types[index][1])
                button.grid(sticky="ew", pady=3, row=rows+1, column=cols+1)

    # Creating buttons
    def create_button(self, root: tk.Frame, name: str, price: float) -> None:
        button = tk.Button(
            root, bg="#f0f0f0", 
            font=("Times", 15), 
            fg="#000000", 
            justify="center", 
            text=f"{name}: ${price}", 
            command=partial(self.add_item, name, price)
        )
        return button
                
    # WHP2024 - Adding items
    def add_item(self, name: str, price: float) -> None:
        item: Item = Item(name, price, 1)
        self.test_order.items.append(item)
        
        self.update_listbox()

    # Delete button
    def delete_item(self):
        # Reverse the order of selected indices to avoid index changes affecting subsequent deletions
        selected_indices = sorted(self.listbox.curselection())

        for index in reversed(selected_indices):
            deleted_item = self.test_order.items[index]
            self.test_order.items.pop(index)
        
        # Update display
        self.update_listbox()
    
    def update_listbox(self):
        # Clear listbox
        self.listbox.delete(0, tk.END)

        # Add items back
        for item in self.test_order.items:
            self.listbox.insert(tk.END, item.get_name())

if __name__ == "__main__":
    root = tk.Tk()
    app = BakerySystem(root)
    root.geometry("1200x600")
    root.mainloop()
    
    """
        def create_button(self, root, text, row, column):
        button = tk.Button(root, text=text, command=lambda: self.button_command(text))
        button.grid(row=4, column=4, padx=5, pady=5)
    """