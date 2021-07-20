import random

def jogar():

    print ("********************************")
    print ("Bem vindo ao jogo de adivinhação")
    print ("********************************")

    #Variaveis
    numero_secreto = random.randrange(1,101)
    tentativas = 0
    pontos = 1000

    #inicio do jogo

    nivel = int(input ("Escolha seu nível (1 para facil, 2 para médio e 3 para dificil): " ))

    if(nivel == 2):
        tentativas = 10
        print("Voce escolheu o nivel medio")
    elif (nivel == 3):
        tentativas = 5
        print("Voce escolheu o nivel dificil")
    elif (nivel ==1):
        tentativas= 20
        print("Voce escolheu o nivel facil")

    for rodada in range (1, tentativas +1):
        print("Tentativa {} de {}".format(rodada,tentativas))
        chute_str = input("Digite o seu número de 1 a 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if(chute <1 or chute > 100):
            print("Você deve digitar um valor entre 1 e 100!")
            ("Escolha seu nível (1 para facil, 2 para médio ee 3 para dificil): " )
            continue       

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou! e fez {} pontos!".format(pontos))
            break
        else:
            pontos_perdidos = abs(numero_secreto-chute)
            pontos = pontos - pontos_perdidos
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            if (rodada == tentativas):
                print("O numero secreto era {}. você fez {}".format(numero_secreto, pontos))
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
            if (rodada == tentativas):
                print("O numero secreto era {}. você fez {}".format(numero_secreto, pontos))
        
    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar() 