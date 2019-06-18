from Product import Product
from Coin import Coin
from VendingMachine import VendingMachine

def test_foo():
  assert 2 + 2

def test_product_incease():
  product = Product('Snickers', 0, 1.00)
  product.increase()
  assert 1 == product.quantity

def test_coin_defitinion():
  dollar = Coin('DOLLAR', 1.00)
  assert dollar.symbol == 'DOLLAR' and dollar.value == 1.00

def test_vending_machine_init():
  vm = VendingMachine('hospital', initialCash = 130)
  assert vm.cash == 130 and vm.name == 'hospital'

def test_vending_machine_fill():
  vm = VendingMachine('hospital', initialCash = 130)
  vm.fill(32)
  vm.productsList()
  assert len(vm.slots) == 32

def test_insert_coin():
  vm = VendingMachine('hospital', initialCash = 130)
  dollar = Coin('DOLLAR', 1.00)
  vm.insertCoin(dollar)
  insertedCoin = vm.insertedCoins[0]
  assert insertedCoin.symbol == 'DOLLAR' and insertedCoin.value == 1.00

def test_sum_inserted_coins():
  vm = VendingMachine('hospital', initialCash = 130)

  dollar = Coin('DOLLAR', 1.00)
  quarter = Coin('Q', 0.25)

  vm.insertCoin(dollar)
  vm.insertCoin(dollar)
  vm.insertCoin(quarter)

  vm.sumInsertedCoins()
  assert vm.insertedCoinsSum == 2.25
  
def test_product_bought():
  vm = VendingMachine('hospital', initialCash = 130)
  vm.fill(32)

  dollar = Coin('DOLLAR', 1.00)
  quarter = Coin('Q', 0.25)

  vm.insertCoin(dollar)
  vm.insertCoin(dollar)
  vm.insertCoin(dollar)
  vm.insertCoin(quarter)

  vm.sumInsertedCoins()

  product = vm.slots[5]

  boughtProduct = vm.buyProduct(5)

  assert boughtProduct != False

def test_product_not_bought():
  vm = VendingMachine('hospital', initialCash = 130)
  vm.fill(32)

  quarter = Coin('Q', 0.25)
  vm.insertCoin(quarter)
  vm.sumInsertedCoins()

  product = vm.slots[5]
  boughtProduct = vm.buyProduct(5)

  assert boughtProduct == False

def test_rest():
  vm = VendingMachine('hospital', initialCash = 130)
  vm.fill(32)

  dollar = Coin('DOLLAR', 1.00)
  quarter = Coin('Q', 0.25)

  vm.insertCoin(dollar)
  vm.insertCoin(dollar)
  vm.insertCoin(dollar)
  vm.insertCoin(quarter)

  vm.sumInsertedCoins()
  initialSum = vm.insertedCoinsSum

  product = vm.slots[5]

  boughtProduct = vm.buyProduct(5)

  assert vm.insertedCoinsSum != initialSum