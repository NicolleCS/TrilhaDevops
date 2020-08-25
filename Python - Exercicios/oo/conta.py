class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto..")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo R${} do titular {}.".format(self.saldo, self.titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor):
        valor_disponivel_sacar = self.__saldo + self.__limite
        return valor <= valor_disponivel_sacar

    def saca(self, valor):
        if(self.pode_sacar()):
            self.__saldo -= valor
        else:
            print("O valor {} passou do limite".format(valor))

    def transfere(self, valor, conta_destino):
        conta_origem = self

        conta_origem.saca(valor)
        conta_destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'123', 'MeuBanco':'6565'}
