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
      return f'Limite disponível: R$ {self._limite_disponivel:.2f}'

    def comprar(self, valor):
      if valor > self._limite_disponivel:
          print(f"[ERRO] Saldo insuficiente para compra de R$ {valor:.2f}")
          return False
      print(f"[COMPRA] R$ {valor:.2f} aprovada com sucesso!")
      self._limite_disponivel -= valor
      self.valor_fatura += valor
      return True

    def pagar_fatura(self, valor):
      if valor > self.valor_fatura:
          print(f"[ERRO] Pagamento de R$ {valor:.2f} é maior que a fatura (R$ {self.valor_fatura:.2f})")
          return False
      print(f"[PAGAMENTO] R$ {valor:.2f} realizado com sucesso!")
      self.valor_fatura -= valor
      self._limite_disponivel += valor
      return True

    @property
    def ver_fatura(self):
      return f'Fatura atual: R$ {self.valor_fatura:.2f}'

    @property
    def ver_limite_total(self):
      return f'Limite total: R$ {self._limite_total:.2f}'

    def aumentar_limite(self, valor):
      if valor > self._limite_total * 0.3:
          print(f"\n[ERRO] Valor de R$ {valor:.2f} excede 30% do limite total.")
          return False
      self._limite_total += valor
      self._limite_disponivel += valor
      print(f"[SUCESSO] Limite aumentado em R$ {valor:.2f}\n")
      return True

    def exibir_status(self):
        print("-" * 30)
        print(f"RESUMO DO CARTÃO: {self.titular.upper()}")
        print("-" * 30)
        print(f"• Limite Total:      R$ {self._limite_total:>8.2f}")
        print(f"• Limite Disponível: R$ {self._limite_disponivel:>8.2f}")
        print(f"• Fatura Atual:      R$ {self.valor_fatura:>8.2f}")
        print("-" * 30 + "\n")

# --- Testando o Sistema ---
cartao = CartaoDeCredito("Kaike")

cartao.exibir_status()

# Realizando compras
cartao.comprar(100)
cartao.comprar(250)

# Aumentando limite
cartao.aumentar_limite(500)

cartao.exibir_status()
