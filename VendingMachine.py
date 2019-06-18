from Product import Product
from Coin import Coin
import random

class VendingMachine:
  name = ''
    
  def __init__(self, name: str, **qwargs: dict):
    self.name = name
    self.insertedCoinsSum = 0.00
    self.insertedCoins = []
    self.slots = []

    if qwargs.get('initialCash'):
      self.cash = qwargs.get('initialCash')
    else:
      self.cash = 100.00

  def fill(self, productsQuantity: int):
    randomProductsNames = ['Mars', 'Snickers', 'Coffee', 'Coca-Cola', 'Pepsi 😂', 'iPhone']
    for i in range(0, productsQuantity):
      product = Product(random.choice(randomProductsNames), random.randint(1, 9), random.choice([1.00, 1.50, 2.00, 3.00]))
      self.slots.append(product)

  def productsList(self):
    for product in self.slots:
      print('NAME:', product.name, 'QUANTITY:', product.quantity, 'PRICE:', product.price)

  def insertCoin(self, coin: Coin):
    self.insertedCoins.append(coin)

  def sumInsertedCoins(self):
    for coin in self.insertedCoins:
      self.insertedCoinsSum = self.insertedCoinsSum + coin.value

  def buyProduct(self, number: int):
    product = self.slots[number]
    if (product.price <= self.insertedCoinsSum and product.quantity > 0):
      product.decrease()
      self.insertedCoinsSum = self.insertedCoinsSum - product.price
      return product
    else:
      return None