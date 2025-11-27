import random

class heroi:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
    def turnos (self):
        print("Qual habilidade você quer usar?")
        print("\n 1) Golpe Flamejante/ 2) Investida Rápida")
        
        p = input(">")
        
        if p.lower() == "1":
            print("Você terá que esperar 2 turnos para utilizar o ataque novamente")
            atk = random.randint(1, 2)
            
            if atk == 1:
                print("Você teve sorte e o inimigo nao atacou")
            elif atk == 2:
                print("O inimigo atacou um ataque mais que especial")
                self.vida -= 7 * 2
        else:
            print("Você ja pode atacar novamente")


Heroi = heroi("dany", 80)
print(f"{Heroi.nome}")
Heroi.turnos()
print(f"no final o heroi terminou com {Heroi.vida}")
    