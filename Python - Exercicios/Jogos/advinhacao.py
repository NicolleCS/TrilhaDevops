import random

def jogar_advinhacao():
    print(
        '\n********************************\n'
        'Bem vindo ao jogo de advinhação!\n'
        '********************************\n'
    )

    numero_random = random.randrange(101)
    numero_random_arredondado = round(numero_random)
    total_de_tentativas = 5
    escolheu = False
    pontos = 1000

    while(escolheu == False):
        print(
            "Qual nível de difículade?\n"
            "(1) Fácil (2) Médio (3) Difícil"
        )

        nivel = int(input("Define o nível:"))

        if(nivel == 1):
            total_de_tentativas = 20
            break
        elif(nivel == 2):
            total_de_tentativas = 10
            break
        elif(nivel == 3):
            total_de_tentativas = 5
            break
        else:
            print("Número inválido!")


    for rodada in range (1,total_de_tentativas +1) :

        print("Tentativa {} de {}".format(rodada,total_de_tentativas))
        chute = input('Digite o seu número entre 1 e 100:')
        acertou = int(chute) == numero_random_arredondado
        chute_maior = int(chute) > numero_random_arredondado
        chute_menor = int(chute) < numero_random_arredondado

        print("Você digitou", chute)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        if acertou:
            print("Você acertoou!! Parabéns!")
            break
        else:
            if(chute_maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif(chute_menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = numero_random - chute
            pontos = pontos - pontos_perdidos
            print("Seus pontos são {}",pontos)

        rodada += 1


# numero1 = 10
# numero2 = 10
#
# if numero1 == numero2:
#     print("Os números são iguais")

if(__name__ == "__main__"):
    jogar_advinhacao()
