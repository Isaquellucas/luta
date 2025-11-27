import random

class Inimigo:
    def __init__(self, nome, dano, vida):
        self.nome = nome
        self.vida = vida
        self.dano = dano
        
    # métodos da class

    def atacar_jogador(self, jogador):
        jogador.vida -= self.dano
        return f"{self.nome} atacou! O jogador agora tem {jogador.vida} de vida."
            

    def estar_vivo(self):
        if self.vida > 0:
            return True
        else: 
            return False
        
            

     # @classmethod'S (monstros)
        
    @classmethod
    def slime(cls):
        return cls("Slime", 15, 3)
    @classmethod
    def goblin(cls):
        return cls("Goblin", 25, 6)
    @classmethod
    def ogro(cls):
        return cls("Ogro", 60, 12)

        # GERAR INIMIGO ALEATÓRIO
    def gerar_inimigo():
        inimigos = [Inimigo.goblin, Inimigo.slime, Inimigo.ogro]
        aleatorio = random.choice(inimigos)
        return aleatorio()
            


    #class jogador 
class Jogador:
    def __init__(self, nome, dano, vida):
        self.nome = nome
        self.dano = dano
        self.vida = vida
    
    def atacar_inimigo (self, alvo):
        alvo.vida -= self.dano
        return f"{self.nome} atacou {alvo.nome}! O inimigo agora tem {alvo.vida} de vida."


# Criando objetos
inimigo = Inimigo.gerar_inimigo()   # agora funciona
jogador = Jogador("dan", 50, 60)

print(jogador.atacar_inimigo(inimigo))

