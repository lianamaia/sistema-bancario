# coding: UTF-8
class SistemaBancario:
    def __init__(self):
        self.saldo = 0
        self.transacoes = []
        self.saques_diarios = 0

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.transacoes.append(f"Depósito: +{self.formatar_valor(valor)}")
            print(f"Depósito de {self.formatar_valor(valor)} realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def saque(self, valor):
        if valor > 0 and valor <= self.saldo and self.saques_diarios < 3 and valor <= 500:
            self.saldo -= valor
            self.transacoes.append(f"Saque: -{self.formatar_valor(valor)}")
            self.saques_diarios += 1
            print(f"Saque de {self.formatar_valor(valor)} realizado com sucesso.")
        elif self.saques_diarios >= 3:
            print("Limite de saques diários atingido.")
        else:
            print("Saldo insuficiente para saque ou valor excede o limite de R$ 500,00.")

    def extrato(self):
        print("\n================ EXTRATO ================")
        if len(self.transacoes) == 0:
            print("Não foram realizadas movimentações.")
        else:
            for transacao in self.transacoes:
                print(transacao)
        print(f"\nSaldo atual: {self.formatar_valor(self.saldo)}")
        print("==========================================")
    @staticmethod
    def formatar_valor(valor):
        return f"R$ {valor:.2f}"
    
# Criar uma instância do sistema bancário
sistema = SistemaBancario()

# Realizar operações
sistema.deposito(1000)
sistema.saque(3000)
sistema.saque(200)
sistema.saque(100)
sistema.saque(1000)
sistema.deposito(10000)
sistema.extrato()