class Pessoa:
    bracos = 2

    def __init__(self, nome, sobrenome, idade, *filhos, pernas=2):
        self.pernas = pernas
        self.filhos = filhos
        self.sobrenome = sobrenome
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Ola {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 55

    @classmethod
    def nome_atributos(cls):
        return f'{cls} - olhos {cls.bracos} '

class Homem(Pessoa):
    pass

class Mutante(Pessoa):
    bracos = 5
    pernas = 9
    def cumprimentar(self):
        print(f'Eae Doidao')
        cumprimentar_da_classe = super().cumprimentar()
        print(f"{cumprimentar_da_classe}, Eae Doidao")

if __name__ == '__main__':
    Renata = Pessoa('Renata', 'Barbosa', 25)
    Richarlisson = Pessoa('Richarlisson', 'Gomes Barbosa', 3)
    Italo = Homem('Ítalo', 'Gomes', 27, Richarlisson.nome)
    print(Pessoa.cumprimentar(Renata))
    print(Renata.cumprimentar())
    print(f'{Renata.nome} {Renata.sobrenome} possui {Renata.idade} anos. '
          f'\nFilhos? {Renata.filhos}. \n'
          f'Quantidade de Pernas = {Renata.pernas}')

    print()

    print(f'{Italo.nome} {Italo.sobrenome} possui {Italo.idade} anos. '
          f'\nFilhos? {Italo.filhos} '
          f'\nQuantidade de Pernas = {Italo.pernas}')

    Italo.olhos = 2
    print(Italo.olhos)
    print(Italo.__dict__)
    print(Renata.__dict__)
    del Italo.filhos
    print(Italo.__dict__)
    print(Italo.bracos)
    Italo.bracos=1
    print(Italo.__dict__)

    print(Pessoa.metodo_estatico())
    print(Italo.metodo_estatico())
    print(Pessoa.nome_atributos())
    print(Italo.nome_atributos())
    print()
    anonima = Homem('anonimus', 'nao', 25)
    print(isinstance(anonima, Pessoa))
    print(Italo.cumprimentar())

    Hulk = Mutante('Hulk', 'José', 157894, pernas = 56)
    print(Hulk.__dict__)
    Hulk.cumprimentar()

print([_ for _ in range(10)])
print([letras for letras in range(50)])