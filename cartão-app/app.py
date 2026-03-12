class CartaoDeCredito:
    def __init__(self, titular, limite_total, limite_disponivel, valor_fatura):
        self.titular = titular
        self.limite_total = limite_total
        self.limite_disponivel = limite_disponivel
        self.valor_fatura = valor_fatura