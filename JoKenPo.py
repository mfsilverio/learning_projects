# o jogo tem que estar em loop até mandar parar
# while e uma variável para continuar?

# passo a passo:
# definir jogadas
# definir contadores
# perguntar nome dos jogadores
# pedir jogada 1
# pedir jogada 2
# comparar as jogadas
# dar resultado
# perguntar se quer jogar novamente
# -----------------------------
jogadas = [0, 1, 2]
# jogadas = []
# jogadas.append(str("pedra"))
# jogadas.append(str("papel"))
# jogadas.append(str("tesoura"))

win_jogador1 = 0
win_jogador2 = 0
empate = 0

continuar = "S"

print("Vamos jogar?")
print("-" * 31)

jogador1 = input("Jogador 1: ")
print("-" * 31)

jogador2 = input("Jogador 2: ")

while continuar == "S":

    print("-" * 31)
    print("Escolha uma das jogadas abaixo: \n [0] Pedra \n [1] Papel \n [2] Tesoura")
    print("-" * 31)

    print(jogador1, ", escolha uma jogada: ")
    jogada1 = int(input("Qual a sua jogada?"))
    print("-" * 31)

    print(jogador2, ", escolha uma jogada: ")
    jogada2 = int(input("Qual a sua jogada?"))
    print("-" * 31)

    if jogada1 == jogadas[0] and jogada2 == jogadas[0]:
        print("Empate!")
        empate += 1

    elif jogada1 == jogadas[0] and jogada2 == jogadas[1]:
        print("Papel envolve a pedra! {} venceu.".format(jogador2))
        win_jogador2 += 1

    elif jogada1 == jogadas[0] and jogada2 == jogadas[2]:
        print("Pedra quebra tesoura! {} venceu.".format(jogador1))
        win_jogador1 += 1

    if jogada1 == jogadas[1] and jogada2 == jogadas[0]:
        print("Papel envolve a pedra! {} venceu.".format(jogador1))
        win_jogador1 += 1

    elif jogada1 == jogadas[1] and jogada2 == jogadas[1]:
        print("Empate!")
        empate += 1

    elif jogada1 == jogadas[1] and jogada2 == jogadas[2]:
        print("Tesoura corta papel! {} venceu.".format(jogador2))
        win_jogador2 += 1

    if jogada1 == jogadas[2] and jogada2 == jogadas[0]:
        print("Pedra quebra tesoura! {} venceu.".format(jogador2))
        win_jogador2 += 1

    elif jogada1 == jogadas[2] and jogada2 == jogadas[1]:
        print("Tesoura corta papel! {} venceu.".format(jogador1))
        win_jogador1 += 1

    elif jogada1 == jogadas[2] and jogada2 == jogadas[2]:
        print("Empate!")
        empate += 1

    continuar = input("Continuar jogando? (S/N): ").upper().strip()

    if continuar == "N":
        print("Vitórias de {}: {}.".format(jogador1, win_jogador1))
        print("Vitórias de {}: {}.".format(jogador2, win_jogador2))
        print("Empates: {}.".format(empate))


