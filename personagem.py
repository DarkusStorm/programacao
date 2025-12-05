import random

class Personagem:
    lista_personagens = []  # Atributo que pertence à CLASSE.
    # "self" diz respeito ao próprio OBJETO.
    # "cls" diz respeito à CLASSE.

    def __init__(self, nome, nivel, hp):
        self.nome = nome
        self.nivel = nivel
        self.hp = hp
        self.hp_total = self.hp
        # Atributos que pertencem ao OBJETO.
        Personagem.lista_personagens.append(self)

    @classmethod  # Decorator, mas não decoração.
    def atualizar_hp(cls, nome, novo_hp):
        for personagem in cls.lista_personagens:
            if personagem.nome == nome:
                personagem.hp = novo_hp
                print(personagem)
                if personagem.hp > personagem.hp_total / 2:
                    print(f"{personagem.nome} ainda pode lutar!")
                elif personagem.hp <= personagem.hp_total / 2 and personagem.hp > (personagem.hp_total / 2) / 2:
                    print(f"{personagem.nome} está começando a se cansar...")
                elif personagem.hp <= (personagem.hp_total / 2) / 2 and personagem.hp > 0:
                    print(f"{personagem.nome} está gravemente ferido!")
                elif personagem.hp <= 0:
                        personagem.derrota()

    def atacar(self, target, dano):
        if target.hp > 0:
            print(f"{self.nome} ataca {target.nome}, causando {dano} Pontos de Dano!")
            Personagem.atualizar_hp(target.nome, novo_hp=target.hp-dano)
        else:
            print(f'{self.nome} não pôde atacar, pois {target.nome} já está caído!')

    def derrota(self):
        if self.hp <= 0:
            roll = random.randint(1, 6)
            if roll == 6:
                self.hp = 1
                print(f'{self.nome} não sucumbiu.')
            else:
                print(f'{self.nome} foi derrotado!')
                return
            
    def __str__(self):
        return f'{self.nome}, de Nível {self.nivel}, possui {self.hp} Pontos de Vida.'

class Mago(Personagem):

    def __init__(self, nome, nivel, hp, mp):
        super().__init__(nome, nivel, hp) # Chama o __init__ da superclasse
        self.mp = mp

    def atacar(self, target, dano): # Override (Sobrescrita do método)
        if target.hp > 0:
            if self.mp >= 10:
                print(f'{self.nome} lançou uma magia em {target.nome}, causando {dano} Pontos de Dano!')
                self.mp -= 10
                Personagem.atualizar_hp(target.nome, novo_hp=target.hp-dano)
            else:
                print(f'{self.nome} está sem mana...')
        else:
            print(f'{self.nome} não pôde atacar, pois {target.nome} já está caído!')

    def __str__(self):
        return f'{self.nome}, de Nível {self.nivel}, possui {self.hp} Pontos de Vida (HP) e {self.mp} Pontos de Mana (MP).'
            
class Bardo(Personagem):

    def __init__(self, nome, nivel, hp):
        super().__init__(nome, nivel, hp) # Chama o __init__ da superclasse
    
    def atacar(self, target, dano): # Override (Sobrescrita do método)
        if target.hp > 0:
            print(f'{self.nome} tocou uma música triste para {target.nome}, causando {dano} Pontos de Dano!')
            Personagem.atualizar_hp(target.nome, novo_hp=target.hp - dano)
        else:
            print(f'{self.nome} não pôde atacar, pois {target.nome} já está caído!')

### AÇÃO ###

# Criando os objetos com base na classe Personagem.
super_edgard = Mago("Super Edgard", 40, 10000, 50)
joao = Bardo("João Roccella", 30, 10000)
batman = Personagem("Batman", 20, 200)

# Imprimindo a situação inicial dos personagens (objetos).
print(super_edgard)
print(joao)
print(batman)

# Ataque do Batman e atualização de HP do alvo (Super Edgard).
batman.atacar(super_edgard, 1)

# Ataque do Super Edgard e atualização de HP do alvo (Batman).
super_edgard.atacar(batman, 203)

# Ataque de João ao cadáver de Batman.

joao.atacar(batman, 100)