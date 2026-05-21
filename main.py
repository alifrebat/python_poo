"""
    CLASSE INICIAL DO PROJETO
"""
from Pessoa import Pessoa
from Funcionario import Funcionario
funcionarios = []
op = 'S'
while op.upper() == 'S':
    nome = input("DIGITE O NOME \n")
    idade = int(input("DIGITE A IDADE \n"))
    cargo = input("DIGITE O CARGO \n")
    salario = float(input("DIGITE O SALÁRIO \n"))
    objFuncionario = {
        "nome" : nome,
        "idade" : idade,
        "renda": 0.0,
        "cargo" : cargo,
        "salario": salario
    }

    funcionarios.append(Funcionario(objFuncionario))
       
    op = input("DESEJA ADICIONAR OUTRO FUNCIONÁRIO? S/N \n")

for f in funcionarios:
    print(f"{f.nome} - {f.idade} - {f.cargo} - R$ {f.salario} - R$ {Funcionario(objFuncionario).reajuste_Salario(f.salario)}")

"""
pessoas = []

while op.upper() == 'S':
    nome = input("DIGITE O NOME \n")
    idade = int(input("DIGITE A IDADE \n"))
    renda = float(input("DIGITE A RENDA \n"))

    objPessoa = {
        "nome" : nome,
        "idade" : idade,
        "renda" : renda
    }

    novaIdade = Pessoa.calculoIdade(idade)

    print(novaIdade)

    pessoas.append(Pessoa(objPessoa))

    op = input("DESEJA ADICIONAR OUTRA PESSOA? S/N \n")

for p in pessoas:
    print(f"{p.nome} - {p.idade} - R$ {p.renda}")

pessoa = Pessoa(objPessoa)
"""