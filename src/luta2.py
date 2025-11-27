import random

class heroi:
    def __init__(self, nome, vida, dano):
        self.nome = nome
        self.vida = vida
        self.dano = dano

    def ataque(self, alvo):
        i = random.randint(1, 6)

        if i in [1, 2, 3, 4]:
            print(f"{self.nome} atacou mas a defesa foi mal feita!")
            alvo.vida -= self.dano * 1.5

        elif i == 5:
            print(f"{self.nome} acertou um crítico!")
            alvo.vida -= self.dano * 2

        else:
            print(f"{self.nome} errou o ataque :(")


class slime:
    def __init__(self, nome, vida, dano):
        self.nome = nome
        self.vida = vida
        self.dano = dano

    def ataque(self, alvo):
        i = random.randint(1, 6)

        if i in [1, 2, 3, 4]:
            print(f"{self.nome} atacou mas a defesa foi mal feita!")
            alvo.vida -= self.dano * 1.5

        elif i == 5:
            print(f"{self.nome} acertou um crítico!")
            alvo.vida -= self.dano * 2

        else:
            print(f"{self.nome} errou o ataque :(")




# declaração das classes
Slime = slime("slime", 40, 20)
Heroi = heroi("dany", 50, 10)


Slime.ataque(Heroi)
Heroi.ataque(Slime)

print(f"A luta será entre {Slime.nome} e {Heroi.nome}")
print(f"Os resultados da luta foi {Slime.vida} de vida do {Slime.nome} e {Heroi.vida} de vida do {Heroi.nome}")