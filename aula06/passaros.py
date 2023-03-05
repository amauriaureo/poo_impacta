class Passaro:
    def __init__(self, vida, ataque, defesa):
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa


def atacar(self, alvo):
    pass


def fugir(self, destino):
    pass


class PassaroAereo(Passaro):
    def voar(self):
        pass


class PassaroAquatico(Passaro):
    def nadar(self):
        pass


class PassaroDeCompanhia(PassaroAereo):
    def __init__(self, vida, ataque, defesa, companheiro):
        self.companheiro = companheiro
        super().__init__(vida, ataque, defesa)


class Pinguim(PassaroAquatico):
    def __init__(self, vida, ataque, defesa, peso):
        self.peso = peso
        super().__init__(vida, ataque, defesa)


aguia = PassaroDeCompanhia(100, 300, 250, 'Rafael')
pinguim = Pinguim(140, 80, 400, 5)

p_ar = PassaroAereo(100, 300, 250)
p_agua = PassaroAquatico(140, 80, 400)

print('fim')

# Nesta situação estamos atribuindo na classe mais específica
# os atributos que são pertinentes à ela, e em seguida,
# delegamos ao Python o trabalho de procurar nas classes
# que estão acima na hierarquia de heranças o inicializador
# que deverá ser executado para atribuição dos demais atributos.
# (Linhas 26  35)
