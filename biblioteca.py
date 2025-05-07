class Pessoa():
    def __init__(self, nome, peso, idade, comendo, falando, dormindo):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        self.dormindo = dormindo

    def comer(self):
        if self.comendo:
            print(f'{self.nome}, já está comendo')
        elif self.dormindo:
            print(f'{self.nome}, não pode comer porque está comendo')
        elif self.falando:
           print(f'{self.nome},não pode comer porque está falando')

    def falar(self):
        if self.falando:
            print(f'{self.nome},já está falando')
        elif self.dormindo:
            print(f'{self.nome},não pode falar porque está dormindo')
        elif self.comendo:
            print(f'{self.nome},não pode comer porque está comendo')

    def dormir(self):
        if self.dormindo:
            print(f'{self.nome},já está dormindo')
        elif self.falando:
            print(f'{self.nome},não pode dormir porque esta falando')
        elif self.comendo:
            print(f'{self.nome},não pode dormir porque esta comendo ')

        else:
            print(f'{self.nome} dormindo')
            jhhfjjfj

