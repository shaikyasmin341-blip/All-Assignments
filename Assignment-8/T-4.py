#Task Description#4
#• Let AI fix it Prompt AI to generate test cases for a ShoppingCart class (add_item,remove_item, total_cost).
#Methods:
#Add_item(name,orice)
#Remove_item(name)
#Total_cost()
#Expected Output#4
#• Full class with tested functionalities
#want the print of all test cases passed at the end.

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        if price < 0:
            return "Invalid price"
        if name in self.items:
            self.items[name] += price
        else:
            self.items[name] = price

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
        else:
            return "Item not found"

    def total_cost(self):
        return sum(self.items.values())
    
# Test cases for ShoppingCart class
def test_shopping_cart():
    cart = ShoppingCart()
    
    # Test adding items
    cart.add_item("apple", 1.0)
    cart.add_item("banana", 2.0)
    assert cart.total_cost() == 3.0, f"Expected total cost 3.0, got {cart.total_cost()}"
    
    # Test adding the same item again
    cart.add_item("apple", 1.5)
    assert cart.total_cost() == 4.5, f"Expected total cost 4.5, got {cart.total_cost()}"
    
    # Test removing an item
    cart.remove_item("banana")
    assert cart.total_cost() == 2.5, f"Expected total cost 2.5, got {cart.total_cost()}"
    
    # Test removing an item that doesn't exist
    result = cart.remove_item("orange")
    assert result == "Item not found", f"Expected 'Item not found', got {result}"
    
    # Test adding an item with invalid price
    result = cart.add_item("grape", -1.0)
    assert result == "Invalid price", f"Expected 'Invalid price', got {result}"
    
    # Test total cost with no items
    cart.remove_item("apple")
    assert cart.total_cost() == 0.0, f"Expected total cost 0.0, got {cart.total_cost()}"
    
    print("All test cases passed!")
if __name__ == "__main__":
    test_shopping_cart()
