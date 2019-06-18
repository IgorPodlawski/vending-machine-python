from VendingMachine import VendingMachine

def loop():
  print('press CTRL+C or CTLR+D to exit')
  vm = VendingMachine('hospital', initialCash = 130)
  vm.fill(32)

  while True:
    try:
      data = input('MACHINE> ')
      if (data == 'PRODUCTS'):
        vm.productsList()
    except (KeyboardInterrupt, EOFError):
      print('goodbye!')
      break


if __name__ == "__main__":
  loop()

