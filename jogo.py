# personagem: classe mãe
# heroi: controlado pelo usuário
# inimigo: adversário do heroi

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
    
heroi = Heroi("Arthur", 100, 5, "Espadachim")
print("Detalhes do Herói:")
heroi.exibir_detalhes()

inimigo = Inimigo("Goblin", 50, 2, "Monstro")
print("\nDetalhes do Inimigo:")
inimigo.exibir_detalhes()