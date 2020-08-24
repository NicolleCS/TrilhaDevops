import forca
import advinhacao

def escolha_jogo():
    print(
        '********************************\n'
        '****** Escolha o seu jogo ******\n'
        '********************************\n'
    )

    print("(1) Forca (2) Advinhação")

    jogo = int(input("Qual jogo?"))

    if (jogo == 1):
        print("Jogando forca..")
        forca.jogar_forca
    elif(jogo == 2):
        print("Jogando Advinhação")
        advinhacao.jogar_advinhacao()

if(__name__ == "__main__"):
    escolha_jogo()