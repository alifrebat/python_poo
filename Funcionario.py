"""
    CLASSE FUNCIONÁRIO PARA HERDAR DE PESSOA
"""
#importação da pessoa do arquivo Pessoa.py
from Pessoa import Pessoa

#Herança da classe Pessoa
class Funcionario(Pessoa):
    #construtor
    def __init__(self, objFuncionario):
        #construtor da classe Mãe
        super().__init__(objFuncionario)
    
        self.cargo = objFuncionario["cargo"]
        self.salario = objFuncionario["salario"]

    def reajuste_Salario(self, valor):
        novo_salario = valor + (valor * 0.10)

        return novo_salario
    
    def reajuste_salario(self):
        self.salario += self.salario * 0.10