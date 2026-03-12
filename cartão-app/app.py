class CartaoDeCredito:
    def __init__(self, titular, limite_total, limite_disponivel, valor_fatura):
        self.titular = titular
        self.limite_total = limite_total
        self.limite_disponivel = limite_disponivel
        self.valor_fatura = valor_fatura

    def comprar(self, valor):
      if valor > self.limite_disponivel:
          print("Erro: Saldo insuficiente")
          return False
      self.limite_disponivel -= valor
      self.valor_fatura += valor
      return True
