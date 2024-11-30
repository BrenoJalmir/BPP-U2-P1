import logging as logger

logger.basicConfig(filename='log.log', level=logger.DEBUG, encoding='utf-8', filemode='w', format='%(asctime)s - %(levelname)s || %(message)s')

class Produto:
  def __init__(self, id:int, nome:str, preco:float):
    self.id = id
    self.nome = nome
    self.preco = preco

  def __str__(self):
    return f'({self.id:^4}) | {self.nome:^32} - R$ {self.preco:^5.2f}'


class Catalogo:
  def __init__(self):
    self.registered_products = {}

  def adicionar_produto(self, id, produto:Produto):
    logger.info(f'Adicionando produto {produto} ao catálogo.')
    self.registered_products[id] = produto

  def listar_produtos(self):
    print_products(self.registered_products.values())

  def buscar_produto_por_id(self, id):
    if id in self.registered_products:
      return self.registered_products[id]
    else:
      return None


class Pedido:
  def __init__(self, cliente:str):
    self.produtos = []
    self.cliente = cliente
    logger.info(f'Criação de novo pedido do cliente {cliente}.')

  def adicionar_produto(self, product:Produto):
    self.produtos.append(product)
    return product

  def calcular_total(self):
    total = 0
    discount = 0
    for product in self.produtos:
      total += product.preco
    if total > 100.0:
      discount = round(total * 0.1, 2)
      logger.info(f'Desconto de R$ {discount} dado no pedido de R$ {total} do cliente {self.cliente}')
      total = round(total * 0.9, 2)
    return total, discount


def receive_id():
  try:
    id = int(input('ID: '))
    return id
  except ValueError as e:
    logger.debug('Valor inválido para ID.\n')
    return e
  except Exception as e:
    logger.error(f'Erro inesperado ao tentar receber um ID.\n {e}')
    return e


def receive_preco():
  try:
    preco = round(float(input('Preço: ')), 2)
    return preco
  except ValueError as e:
    logger.debug('Valor inválido para preço.\n')
    return e
  except Exception as e:
    logger.error(f'Erro inesperado ao tentar receber um preço.\n {e}')
    return e


def print_products(products:list, mode:int = 1):
  if len(products) == 0:
    print('Não existem produtos no catálogo!' if mode == 1 else 'Não há nenhum produto no carrinho!')
    return
  print('Produtos cadastrados:' if mode == 1 else 'Produtos no carrinho:\n')
  print(f'{"ID":^6} | {"NOME":^32} - {"PREÇO":^8} ')
  for product in products:
    print(product)


def print_menu(menu:int):
  if menu == '0':
    print('1 - Catálogo de Produtos')
    print('2 - Pedidos')
    print('3 - Sair\n')
  elif menu == '1':
    print('1 - Cadastrar produto')
    print('2 - Listar produtos')
    print('3 - Buscar produto por ID')
    print('4 - Voltar\n')
  elif menu == '2':
    print('1 - Adicionar produto ao carrinho')
    print('2 - Calcular valor atual do carrinho')
    print('3 - Finalizar pedido\n')


def main():
  catalog = Catalogo()

  menu = 0
  action = 0

  while menu != 3:
    print_menu('0')
    menu = input('Menu: ')

    print('\n=======================================================================================================================\n')

    if menu == '1':
      while action != 4:
        print_menu(menu)
        action = input('Opção: ')

        print('')

        if action == '1':
          id = receive_id()
          if type(id) == ValueError:
            continue
          nome = input('Nome: ')
          preco = receive_preco()
          if type(preco) == ValueError:
            continue
          if type(catalog.buscar_produto_por_id(id)) == Produto:
              print('Já existe um produto com esse ID!')
              continue
          catalog.adicionar_produto(id, Produto(id, nome, preco))
          logger.info('Produto cadastrado com sucesso!')
        elif action == '2':
          catalog.listar_produtos()
        elif action == '3':
          id = receive_id()
          if type(id) == ValueError:
            continue
          product = catalog.buscar_produto_por_id(id)
          print(product if product else 'Não existe produto com esse ID.')
        elif action == '4':
          break
        else:
          print('Opção inválida')
        print('')
    elif menu == '2':
      customer = input("Nome do cliente: ")
      order = Pedido(customer)
      while action != 3:
        print_menu(menu)
        action = input("Opção: ")

        print('')

        if action == '1':
          print_products(catalog.registered_products.values())
          id = receive_id()
          if type(id) == ValueError:
            continue
          product = catalog.buscar_produto_por_id(id)
          if product:
            order.adicionar_produto(product)
            print('Produto adicionado ao pedido.')
          else: 
            print('Não existe produto com esse ID.')
        elif action == '2':
          print_products(order.produtos, 2)
          total, discount = order.calcular_total()        
          print(f'Total: {total:.2f}; Desconto: {discount:.2f}')
        elif action == '3':
          total, discount = order.calcular_total()              
          print(f'Cliente: {order["customer"]}\nTotal: {total:.2f}; Desconto: {discount:.2f}')
          break
        else:
          print('Opção inválida.')
        print('')
    elif menu == '3':
      return 0
    else:
      print('Opção inválida.')
    
    print('\n=======================================================================================================================\n')

if __name__ == '__main__':
  main()