class CartaoDeCredito:
    def __init__(self, titular):
        self.titular = titular
        self._limite_total = 2500
        self._limite_disponivel = 2500
        self.valor_fatura = 0

    def __str__(self):
      return f"Cartão de Crédito de {self.titular}"
    
    @property
    def ver_limite_disponivel(self):
      return f'Limite disponível: {self._limite_disponivel}'

    def comprar(self, valor):
      if valor > self._limite_disponivel:
          print("Erro: Saldo insuficiente")
          return False
      print(f"Compra realizada com sucesso, no valor de {valor}\n")
      self._limite_disponivel -= valor
      self.valor_fatura += valor
      return True

    def pagar_fatura(self, valor):
      if valor > self.valor_fatura:
          print("Erro: Valor maior que o da fatura")
          return False
      self.valor_fatura -= valor
      self._limite_disponivel += valor
      return True

    @property
    def ver_fatura(self):
      return f'Fatura atual: {self.valor_fatura}'

    @property
    def ver_limite_total(self):
      return f'Limite total: {self._limite_total}'

    def aumentar_limite(self, valor):
      if valor > self._limite_total:
          print("Erro: Valor maior que o limite total")
          return False
      self._limite_total += valor
      self._limite_disponivel += valor
      return True

cartao1 = CartaoDeCredito("Kaike")
print(cartao1.ver_limite_disponivel)
print(cartao1.ver_limite_total)
cartao1.comprar(100)
print(cartao1.ver_fatura)
print(cartao1.ver_limite_disponivel)