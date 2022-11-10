class Pessoa:
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



