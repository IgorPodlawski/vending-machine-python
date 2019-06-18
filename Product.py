class Product:
  name = ''
  quantity = 0
  price = 0.00
    
  def __init__(self, name: str, quantity: int, price: float): 
    self.name = name
    self.quantity = quantity
    self.price = price

  def increase(self):
    self.quantity = self.quantity + 1

  def decrease(self):
    self.quantity = self.quantity - 1