"""
    CLASSE INICIAL DO PROJETO
"""
from Pessoa import Pessoa

pessoas = []

op = 'S'

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
