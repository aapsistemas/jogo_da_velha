# Função para imprimir o tabuleiro

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 9)

# Função para verificar se algum jogador venceu

def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas
    for linha in tabuleiro:
        if all(posicao == jogador for posicao in linha):
            return True

    # Verificar colunas
    for coluna in range(3):
        if all(tabuleiro[i][coluna] == jogador for i in range(3)):
            return True

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True

    return False

# Função para realizar a jogada de um jogador
def fazer_jogada(tabuleiro, jogador):
    nome = jogador["nome"]
    print(f"{nome}, faça a sua jogada.")

    while True:
        linha = int(input("Digite o número da linha (0, 1 ou 2): "))
        coluna = int(input("Digite o número da coluna (0, 1 ou 2): "))

        if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
            print("Posição inválida! Tente novamente.")
        elif tabuleiro[linha][coluna] != " ":
            print("Essa posição já está ocupada! Tente novamente.")
        else:
            tabuleiro[linha][coluna] = jogador["simbolo"]
            break

# Função principal
def jogar_jogo_da_velha():
    jogador1 = {"nome": input("Jogador 1, digite seu nome: "), "simbolo": "X"}
    jogador2 = {"nome": input("Jogador 2, digite seu nome: "), "simbolo": "O"}

    tabuleiro = [[" ", " ", " "],
                 [" ", " ", " "],
                 [" ", " ", " "]]

    jogador_atual = jogador1
    jogo_acabou = False

    while not jogo_acabou:
        imprimir_tabuleiro(tabuleiro)
        fazer_jogada(tabuleiro, jogador_atual)

        if verificar_vitoria(tabuleiro, jogador_atual["simbolo"]):
            imprimir_tabuleiro(tabuleiro)
            print(f"Parabéns, {jogador_atual['nome']}! Você venceu!")
            jogo_acabou = True
        elif all(posicao != " " for linha in tabuleiro for posicao in linha):
            imprimir_tabuleiro(tabuleiro)
            print("O jogo terminou em empate!")
            jogo_acabou = True
        else:
            jogador_atual = jogador2 if jogador_atual == jogador1 else jogador1

# Iniciar o jogo
jogar_jogo_da_velha()
