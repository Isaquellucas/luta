import random

class assassino:
    def __init__(self, nome, dano, vida):
        self.nome = nome
        self.dano = dano
        self.vida = vida
    def turnos(self):
        print("1) ataca; 2) defende")
        i = input(">")
        if i == "1":
            print(f"Você ataca o {Humano.nome}")
        else:
            defesa = self.dano // 2
            self.vida -= defesa
            print("ataque defendido")
            return defesa

class humano:
    def __init__(self, nome, dano, vida):
        self.nome = nome
        self.dano = dano
        self.vida = vida
    def acao_do_humano(self):
        i = random.randint(1, 3)
        if i == 1:
            print("Humano atacou")
        elif i == 2:
            print("Humano defende")
        else: 
            print("o humano nao faz nada")

Humano = humano("dany", 10, 20)
Assassino = assassino("babil", 20, 30)

print("\n -------------- que a luta começe --------------")


print("\n \t a luta é entre ", Assassino.nome, "e", Humano.nome)
Assassino.turnos()
Humano.acao_do_humano()