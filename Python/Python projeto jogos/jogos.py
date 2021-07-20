import jogo_forca
import jogo_adivinhacao

def escolhe_jogo():

    print ("********************************")
    print ("Bem vindo ao jogo de adivinhação")
    print ("********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual Jogo? "))

    if(jogo ==1):
        print("jogando foca")
        jogo_forca.jogar()
    elif(jogo == 2):
        print("jogando adivinhação")
        jogo_adivinhacao.jogar()

if (__name__ == "__main__"):
    escolhe_jogo() 