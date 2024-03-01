import tkinter as tk

class POSSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("POS System")

        # Product data (product_id: (product_name, price))
        self.products = {
            1: ("Item 1", 10.99),
            2: ("Item 2", 5.99),
            3: ("Item 3", 7.49),
            # Add more products as needed
        }

        # Initialize variables
        self.selected_items = {}
        self.total_price = tk.DoubleVar()
        self.total_price.set(0.0)

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Product listbox
        self.product_listbox = tk.Listbox(self.master, selectmode=tk.MULTIPLE)
        for product_id, (product_name, _) in self.products.items():
            self.product_listbox.insert(tk.END, f"{product_id}: {product_name}")
            self.product_listbox.pack(padx=10, pady=10)

        # Add to cart button
        add_button = tk.Button(self.master, text="Add to Cart", command=self.add_to_cart)
        add_button.pack(pady=5)

        # Total label
        total_label = tk.Label(self.master, text="Total Price:")
        total_label.pack()

        # Display total
        total_display = tk.Label(self.master, textvariable=self.total_price)
        total_display.pack()

    def add_to_cart(self):
        selected_indices = self.product_listbox.curselection()

        for index in selected_indices:
            product_id = index + 1  # Assuming product IDs start from 1
            if product_id in self.products:
                product_name, price = self.products[product_id]
                if product_id not in self.selected_items:
                    self.selected_items[product_id] = {"name": product_name, "price": price}
                    self.total_price.set(self.total_price.get() + price)

if __name__ == "__main__":
    root = tk.Tk()
    pos_system = POSSystem(root)
    root.mainloop()