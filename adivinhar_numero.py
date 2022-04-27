"""
Esse é um programa feito em python que usa a função de número aleatório(randint)
estrutura de repetição while, print e tipos booleanos para criar um jogo de adivinhação.
Nesse jogo o objetivo é adivinhar qual é o número que a função randint com range 1 a 30 escolheu antes que as chances acabem.
Caso as chances acabem, o usuário tem a escolha de recomeçar o jogo ou parar o programa.
"""

#importando a função randint que será usada no programa
from random import randint

#usando a função randint e decidindo em qual range o programa trabalhará
ns = randint(1,30)
#decidindo a quantidade de tentativas que o usuário tem
limite_tentativas = 10
#criando a variável tentativas que será usada no programa
tentativas = 0
#criando variável que ajudará a decidir se o usuário ainda tem tentativas
sem_tentativas = False

#mostrando instruções ao usuário sobre o funcionamento do programa
print("Bem-vindos ao programa de adivinhação!")
print("Nesse programa você terá que adivinhar um número aleatório entre 1 e 30.")
print("Você tem {} tentativas para fazer isso.".format(limite_tentativas))
print("\nVamos começar!")
#pedindo o número que o usuário acredita ser o número aleatório, n
n = int(input("Chute um número: "))

#criando a estrutura de repetição que se repetirá sempre que o usuário enviar um número diferente do número aleatório	
while n != ns:
    #checando se o input do usuário é maior que o número aleatório e se ele ainda tem tentativas restantes
    if n > ns and limite_tentativas > tentativas:
        #contando como uma tentativa a mais caso o usuário tenha errado o número aleatório
        tentativas += 1
        #mostrando ao usuário que o número é menor que o dele e quantas tentativas restam
        print("\nÉ um número menor que {}!".format(n))
        print("Tentativas restantes: {}".format(int(limite_tentativas - tentativas)))
        #pedindo novo input do usuário, n
        n = int(input("Tente outro número: "))
    #checando se o input do usuário é menor que o número aleatório e se ele ainda tem tentativas restantes
    elif n < ns and limite_tentativas > tentativas:
        #contando como uma tentativa a mais caso o usuário tenha errado o número aleatório
        tentativas += 1
        #mostrando ao usuário que o número é maior que o dele e quantas tentativas restam
        print("\nÉ um número maior que {}!".format(n))
        print("Tentativas restantes: {}".format(int(limite_tentativas - tentativas)))
        #pedindo novo input do usuário, n
        n = int(input("Tente outro número: "))
    #caso as tentativas do usuário acabem
    else:
        #atualizar a variável para mostrar que o usuário não tem mais tentativas
        sem_tentativas = True
    
    #o que fazer se o usuário não tiver mais tentativas    
    if sem_tentativas == True:
        #mostrar ao usuário que acabaram as chances
        print("\nAcabaram as suas chances.")
        #perguntando ao usuário se ele quer recomeçar o jogo
        resposta = str(input("Você quer tentar novamente novamente? \nS/N: ").upper())
        #checando se a resposta é sim
        if resposta == 'S':
            #resetando as variáveis do jogo e começando novamente
            ns = randint(1,30)
            limite_tentativas = 11
            tentativas = 0
            sem_tentativas = False
            n = int(input("\nTente outro número: "))
            continue
        #checando se a resposta é não
        elif resposta == 'N':
            #mostrando ao usuário que acabou o jogo e parando o programa
            print("\nFim de jogo.")
            break
    
#caso o usuário tenha acertado o número
if n == ns:
    #mostrar ao usuário que acertou e qual era o número
    print("\nVocê acertou! O número secreto é {}!".format(ns))