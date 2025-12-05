personagens = []

def criar_personagem(nome, nivel, hp):
    personagem = {
        'nome': nome,
        'nivel': nivel,
        'hp': hp
    }
    personagens.append(personagem)

def alterar_hp(nome, novo_hp):
    for personagem in personagens:
        if personagem['nome'] == nome:
            personagem['hp'] = novo_hp

def listar_personagens():
    for personagem in personagens:
        print(f'Nome: {personagem['nome']}, de Nível {personagem['nivel']}, possui {personagem['hp']} Pontos de Vida.')

# criar_personagem('Bob Esponja', 10, 100)
# criar_personagem('Super Choque', 30, 350)
# criar_personagem('Arsène "Raoul" Lupin', 99, '?')
# criar_personagem('Sans, o Esqueleto', '?', 1)
# criar_personagem('Shadow The Hedgehog', 50, 1000)
# criar_personagem('Receptáculo Puro', 99, 8000)
# criar_personagem('Capt. Spaceboy', 20, 275)
# criar_personagem('Aile', 10, 75)

criar_personagem('Superman', 20, 1000)
criar_personagem('Lex Luthor', 20, 100)
print(*personagens, sep='\n')
listar_personagens()
print("Lex Luthor usou uma Kryptonita para enfraquecer Superman!")
alterar_hp('Superman', 100)
listar_personagens()

# A função e o append são guardados na memória, mas não de fato executados, fazendo com que o programa não seja executado linha por linha na prática.