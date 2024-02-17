class Item:
    def __init__(self, item_name: str, price: float, quantity: int):
        self.item_name: str = item_name
        self.price: float = price
        self.quantity: int = quantity