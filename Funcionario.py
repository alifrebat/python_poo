"""
    CLASSE FUNCIONÁRIO PARA HERDAR DE PESSOA
"""
from Pessoa import Pessoa

class Funcionario(Pessoa):
    #construtor
    def __init__(self, objFuncionario)
        super().__init__(objFuncionario)
    
        self.cargo = objFuncionario["salario"]
        self.salario = objFuncionario["salario"]
