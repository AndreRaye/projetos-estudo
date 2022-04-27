"""
Este programa gera um numero qualquer entre 1 e 1000 e o usuário deverá dizer ao programa se esse foi o número que ele pensou
caso não seja o usuário responde ao programa se o número que ele pensou está acima ou abaixo do que o programa gerou.
Caso esteja correto, o programa mostra qual era o número que o usuário pensou e o número de tentativas necessárias para encontrá-lo.
"""
from random import randint

n1 = 1
n2 = 1000
tentativas = 1
numero_random = randint(n1,n2)

print("Bem-vindos!\nNesse programa você deverá pensar em um número inteiro qualquer entre 1 e 1000. \nO computador tentará adivinhar em qual número você pensou.\n")
print("O número que o computador pensou é: {}".format(numero_random))
print("O número que o computador pensou está abaixo, acima ou correto em relação ao seu.")
resposta = str(input("(abaixo/acima/correto): ").lower())

while resposta != 'correto':
    if resposta == 'acima':
        tentativas += 1
        n1 = numero_random
        numero_random = randint(n1,n2)
        print("\nO novo número que o computador pensou é: {}".format(numero_random))
        print("O número que o computador pensou está abaixo, acima ou correto em relação ao seu.")
        resposta = str(input("(abaixo/acima/correto): ").lower())
    elif resposta == 'abaixo':
        tentativas += 1
        n2 = numero_random
        numero_random = randint(n1,n2)
        print("\nO novo número que o computador pensou é: {}".format(numero_random))
        print("O número que o computador pensou está abaixo, acima ou correto em relação ao seu.")
        resposta = str(input("(abaixo/acima/correto): ").lower())
    else:
        print("O número que o computador pensou está abaixo, acima ou correto em relação ao seu.")
        resposta = str(input("(abaixo/acima/correto): ").lower())
        
print("\nO número que você pensou é: {}!".format(numero_random))
print("O computador precisou de {} tentativa(s) para acertar!".format(tentativas))