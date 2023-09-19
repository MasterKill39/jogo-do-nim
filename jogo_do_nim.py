import random

def computador_escolhe_jogada(n, m):
    if n <= m:
        return n
    else:
        k = n % (m+1)
        if k == 0:
            return m
        else:
            return k

def usuario_escolhe_jogada(n, m):
    jogada = int(input("Quantas peças você vai tirar? "))
    while jogada > m or jogada <= 0 or jogada > n:
        print("Oops! Jogada inválida! Tente de novo.")
        jogada = int(input("Quantas peças você vai tirar? "))
    return jogada

def partida():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    tipo_jogo = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))
    while tipo_jogo != 1 and tipo_jogo != 2:
        print("Oops! Opção inválida! Tente de novo.")
        tipo_jogo = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))
    if tipo_jogo == 2:
        num_partida = 1
        usuario = 0
        computador = 0
        while num_partida <= 3:
            print("**** Rodada", num_partida, "****")
            vencedor = partida_individual()
            if vencedor == "computador":
                computador += 1
            else:
                usuario += 1
            num_partida += 1
        print("**** Final do campeonato! ****")
        print("Placar: Você", usuario, "X", computador, "Computador")
    else:
        partida_individual()

def partida_individual():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if n % (m+1) == 0:
        print("Você começa!")
        vez_do_usuario = True
    else:
        print("Computador começa!")
        vez_do_usuario = False
    while n > 0:
        if vez_do_usuario:
            jogada = usuario_escolhe_jogada(n, m)
            n -= jogada
            print("Você tirou", jogada, "peça(s).")
            vez_do_usuario = False
        else:
            jogada = computador_escolhe_jogada(n, m)
            n -= jogada
            print("O computador tirou", jogada, "peça(s).")
            vez_do_usuario = True
        print("Restam", n, "peças no tabuleiro.")
    if vez_do_usuario:
        print("Fim do jogo! O computador ganhou!")
        return "computador"
    else:
        print("Fim do jogo! Você ganhou!")
        return "usuario"

partida()