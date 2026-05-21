"""
    Documentar classe é descrição da classe
    Dizer que ela faz
    Classe Pojo: É uma classe que contem atributos e os métodos setts e getts
"""

class Pessoa:
    """
       Em Python existem várias formas de “simular” construtores diferentes,
       já que a linguagem não possui sobrecarga real de métodos como Java ou C#.
    """
    
    #Muito usado em APIs e JSON
    def __init__(self, objPessoa):
        self.nome = objPessoa["nome"]
        self.idade = objPessoa["idade"]
        self.renda = objPessoa["renda"]
        
    def exibe_dados(self):
       return print(f"{self.nome} - {self.idade} R$ {self.renda:.2f}")

    #PASSANDO VALOR PARA A FORMA API E JSON  
    """
        objPessoa = {
            "nome" : nome,
            "idade" : idade,
            "renda" : renda
        }
    
    #construtor vazio
    def __init__(self):
        pass

    #PASSANDO VALOR PARA CONTRUTOR VAZIO

        p = Pessoa()

        p.nome = "Fulano"
        p.idade = 20
        p.renda = 5000.00

        print(p.nome)

    #Forma mais comum
    def __init__(self, nome, idade, renda):
        self.nome = nome
        self.idade = idade
        self.renda = renda
    
    #PASSANDO VALOR PARA A FORMA COMUM ----> p = Pessoa("fulano", 20, 5000.00)


    

    #Recebe quantidade variável de parâmetros posicionais:
    def __init__(self, *args):
        self.nome = args[0]
        self.idade = args[1]
        self.renda = args[2]
    
    #PASSANDO VALOR PARA A FORMA PARÂMETRO POSICIONAIS ----> p = Pessoa("fulano", 20, 5000.00)

    #Muito flexível. Recebe parâmetros nomeados:
    def __init__(self, **kwargs):
        self.nome = kwargs.get("nome")
        self.idade = kwargs.get("idade")

    #p = Pessoa(nome="fulano",idade=20, renda=5000.00)
    
    #POO Python.
    def __init__(self, nome, idade, renda):
        self.nome = nome
        self.idade = idade
        self.renda = renda

    @classmethod
    def from_dict(cls, dados):
        return cls(
            dados["nome"],
            dados["idade"]
        )

    #PASSANDO VALOR PARA A FORMA Muito profissional em POO Python.
        objPessoa = {
            "nome" : nome,
            "idade" : idade,
            "renda" : renda
        }

        p = Pessoa.from_dict(objPessoa)
    """