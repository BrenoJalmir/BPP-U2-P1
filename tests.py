import unittest as ut
from main import Produto, Catalogo, Pedido

def are_products_equal(p1, p2):
    return p1.id == p2.id and p1.nome == p2.nome and p1.preco == p2.preco

class TestCatalogoMethods(ut.TestCase):

  def setUp(self):
    self.catalogo = Catalogo()
    self.catalogo.adicionar_produto(1, Produto(1, 'Água', 3))

  def test_buscar_produto_por_id(self):
    produto = Produto(1, 'Água', 3)
    self.assertTrue(are_products_equal(self.catalogo.buscar_produto_por_id(produto.id), produto))

  def test_adicionar_produto(self):
    produto = Produto(2, 'Sorvete Flocos 1kg', 15.5)
    self.catalogo.adicionar_produto(produto.id, produto)

    self.assertEqual(len(self.catalogo.registered_products), 2)
    self.assertTrue(are_products_equal(self.catalogo.buscar_produto_por_id(2), produto))

class TestPedidoMethods(ut.TestCase):

  def setUp(self):
    self.catalogo = Catalogo()
    self.catalogo.adicionar_produto(1, Produto(1, 'Água', 3))
    self.catalogo.adicionar_produto(2, Produto(2, 'Leite', 5.3))
    self.catalogo.adicionar_produto(3, Produto(3, 'Feijão 1kg', 9.99))
    self.catalogo.adicionar_produto(4, Produto(4, 'Arroz 1kg', 12.67))
    self.catalogo.adicionar_produto(5, Produto(5, 'Caixa de Chocolate Lollo', 63.43))
    self.catalogo.adicionar_produto(6, Produto(6, 'Caixa de Chocolate Garoto', 15.30))
    self.pedido = Pedido('Teste')

  def teste_adicionar_produto(self):
    produtos = []

    produtos.append(self.pedido.adicionar_produto(Produto(1, 'Caixa de Chocolate Lollo', 63.43)))
    produtos.append(self.pedido.adicionar_produto(Produto(2, 'Caixa de Chocolate Garoto', 15.30)))
    produtos.append(self.pedido.adicionar_produto(Produto(3, 'Batom Garoto Unidade', 1.26)))

    for i in range(0, 2):
      self.assertTrue(are_products_equal(self.pedido.produtos[i], produtos[i]))

  def teste_calcular_total_sem_desconto(self):
    self.pedido.adicionar_produto(self.catalogo.buscar_produto_por_id(1))
    self.pedido.adicionar_produto(self.catalogo.buscar_produto_por_id(2))
    self.pedido.adicionar_produto(self.catalogo.buscar_produto_por_id(3))
    self.pedido.adicionar_produto(self.catalogo.buscar_produto_por_id(4))

    self.assertEqual((self.pedido.calcular_total()), (30.96, 0.0))

  def teste_calcular_total_com_desconto(self):
    self.pedido.adicionar_produto(self.catalogo.buscar_produto_por_id(1))
    self.pedido.adicionar_produto(self.catalogo.buscar_produto_por_id(2))
    self.pedido.adicionar_produto(self.catalogo.buscar_produto_por_id(3))
    self.pedido.adicionar_produto(self.catalogo.buscar_produto_por_id(4))
    self.pedido.adicionar_produto(self.catalogo.buscar_produto_por_id(5))
    self.pedido.adicionar_produto(self.catalogo.buscar_produto_por_id(6))

    self.assertEqual((self.pedido.calcular_total()), (98.72, 10.97))


if __name__ == '__main__':
  ut.main()