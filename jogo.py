# personagem: classe mãe
# heroi: controlado pelo usuário
# inimigo: adversário do heroi
import random

class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome

    def get_vida(self):
        return self.__vida

    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        print(f"Nome: {self.get_nome()}")
        print(f"Vida: {self.get_vida()}")
        print(f"Nível: {self.get_nivel()}")

    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0
        print(f"{self.get_nome()} recebeu {dano} de dano! Vida restante: {self.get_vida()}")

    def atacar(self, alvo):
        dano = self.__nivel * random.randint(0, 10)
        alvo.receber_ataque(dano)

    
class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f"Habilidade: {self.get_habilidade()}")
    
class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f"Tipo: {self.get_tipo()}")
    
class Jogo:
    """ classe orquestradora do jogo, responsável por criar personagens e iniciar o jogo """
    def __init__(self):
        self.heroi = Heroi("Arthur", 100, random.randint(1, 10), "Espadachim")
        self.inimigo = Inimigo("Goblin", 50, random.randint(1, 10), "Monstro")

    def iniciar_jogo(self):
        """ fazer a gestão da batalha em turnos entre herói e inimigo """
        print("Iniciando a batalha!")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhe dos Personagens:")
            self.heroi.exibir_detalhes()
            print()
            self.inimigo.exibir_detalhes()

            input("\nPressione Enter para o herói atacar...")
            escolha = input("Escolha (1- Atacaque Normal, 2- Ataque Especial): ")

            if escolha == "1":
                self.heroi.atacar(self.inimigo)
            elif escolha == "2":
                dano_extra = self.heroi.get_nivel() * random.randint(5, 15)
                print(f"{self.heroi.get_nome()} usou um ataque especial causando {dano_extra} de dano!")
                self.inimigo.receber_ataque(dano_extra)
            else:
                print("Escolha inválida! O herói perdeu a vez.")

# criar instância do jogo e iniciar
jogo = Jogo()
jogo.iniciar_jogo()