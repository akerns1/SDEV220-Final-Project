# WHP2024
class Item:
    def __init__(self, item_name: str, price: float, quantity: int):
        self.item_name: str = item_name
        self.price: float = price
        self.quantity: int = quantity

    # Getters
    def get_name(self) -> str:
        return self.item_name
    
    def get_price(self) -> float:
        return self.price
    
    def get_quantity(self) -> int:
        return self.quantity
    
    # Setters
    def set_name(self, item_name) -> str:
        self.item_name = item_name
    
    def set_price(self, price) -> float:
        self.price = price
    
    def set_quantity(self, quantity) -> int:
        self.quantity = quantity