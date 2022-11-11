class Pessoa:
    rins = 2

    def __init__(self, *filhos, nome=None, idade = 35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    italo = Pessoa(nome='Ítalo')
    carlos = Pessoa(italo,nome ='Carlos', idade =51)

    print(Pessoa.cumprimentar(carlos))
    print(id(carlos))
    print(carlos.cumprimentar())
    print(carlos.nome)
    print(carlos.idade)
    for filho in carlos.filhos:
        print(filho.nome)
    carlos.sobrenome = 'Gomes'
    print(carlos.nome, carlos.sobrenome)
    print(carlos.__dict__)
    print(italo.__dict__)
    del carlos.filhos
    print(carlos.__dict__)
    print(Pessoa.rins)
    print(italo.rins)
    carlos.rins = 1
    print(carlos.__dict__)
    Pessoa.rins = 5
    print(carlos.__dict__)
    del carlos.rins
    print(carlos.__dict__)


