

class Grocery:

    def __init__(self, catagory, item,  unit, quantity, price, date):
        self.catagory = catagory
        self.item = item
        self.unit = unit
        self.quantity = quantity
        self.price = price
        self.date = date
    
    def get_dict(self):
        x = {"Catagory":self.catagory,"Item":self.item,
            "Quantity":f"{self.quantity} {self.unit}",
            "Price":self.price,"Date":self.date
        }
        return x
