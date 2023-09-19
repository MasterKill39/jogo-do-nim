def computador_escolhe_jogada(n, m):
    if n <= m:
        return n
    else:
        quantia = n % (m+1)
        if quantia > 0:
            return quantia
        else:
            return m

def usuario_escolhe_jogada(n, m):
    jogada = 0
    while jogada == 0:
        jogada = int(input("Quantas peças você vai tirar? "))
        if jogada > n or jogada < 1 or jogada > m:
            print("\nOops! Jogada inválida! Tente de novo.")
            jogada = 0
    return jogada

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if n % (m+1) == 0:
        print("\nVocê começa!")
        vez_do_usuario = True
    else:
        print("\nComputador começa!")
        vez_do_usuario = False
    while n > 0:
        if vez_do_usuario:
            jogada = usuario_escolhe_jogada(n, m)
            n = n - jogada
            print("\nVocê tirou", jogada, "peça(s).")
            vez_do_usuario = False
        else:
            jogada = computador_escolhe_jogada(n, m)
            n = n - jogada
            print("\nO computador tirou", jogada, "peça(s).")
            vez_do_usuario = True
        print("Agora restam", n, "peça(s) no tabuleiro.\n")
    if vez_do_usuario:
        print("Fim do jogo! O computador ganhou!")
        return 0
    else:
        print("Fim do jogo! Você ganhou!")
        return 1

def campeonato():
    placar_usuario = 0
    placar_computador = 0
    for i in range(1, 4):
        print("\n**** Rodada", i, "****\n")
        vencedor = partida()
        if vencedor == 0:
            placar_computador += 1
        else:
            placar_usuario += 1
    print("\nPlacar: Você", placar_usuario, "X", placar_computador, "Computador")

print("Bem-vindo ao jogo do NIM!")
print("Escolha:\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato ")
escolha = int(input())
if escolha == 1:
    print("\nVocê escolheu uma partida isolada!\n")
    partida()
elif escolha == 2:
    print("\nVocê escolheu um campeonato!\n")
campeonato()