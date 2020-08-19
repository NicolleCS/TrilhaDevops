print(
    '********************************\n'
    'Bem vindo ao jogo de advinhação!\n'
    '********************************\n'
)

numero_secreto = 42

chute = input('Digite o seu número:')

acertou = int(chute) == numero_secreto

chute_maior = chute > numero_secreto

chute_menor = chute < numero_secreto

print("Você digitou", chute)

if acertou:
    print("Você acertoou!! Parabéns!")
else:
    if(chute_maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif(chute_menor):
        print("Você errou! O seu chute foi menor que o número secreto.")

# numero1 = 10
# numero2 = 10
#
# if numero1 == numero2:
#     print("Os números são iguais")


