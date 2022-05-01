"""
Esse é um programa no qual você joga uma batalha como num jogo RPG baseado em turno tradicional.
Você escolhe qual habilidade gostaria de usar, o programa calcula o dano do acerto e se é um acerto crítico.
O programa escolhe automaticamente qual habilidade o inimigo usará e o dado do acerto dele.
O programa acaba quando a sua vida a ou do inimigo chegarem a zero.
"""
from random import *

h2 = ['chidori', 'amaterasu', 'goukakyuu no jutsu']

pv1 = 1000
pv2 = 1000

rodada = 1

print("-"*80)
print("Bem-vindos!\nEste é um programa é um jogo de luta no estilo RPG baseado em turnos.\nO jogo acaba quando seu PV (pontos de vida) chegar a zero.")

while pv1 >= 0 and pv2 >= 0:
    for i in range(1):
        print()
        print("-"*80)
        print(f"Rodada {rodada}!")
        rodada += 1
        print(f"Seu PV: {pv1}")
        print(f"PV do inimigo: {pv2}")
        habilidade = input("Qual habilidade você gostaria de usar?\n1: Kage bunshin no jutsu\n2: Rasengan\n3: Rasenshuriken\nDigite: ")
        while habilidade not in "123" or habilidade == "":
            habilidade = input("\nQual habilidade você gostaria de usar?\n1: Kage bunshin no jutsu\n2: Rasengan\n3: Rasenshuriken\nDigite: ")
        if habilidade == '1':
            dado = randint(1,20)
            dano = 10 * dado
            dano2 = dano * 2
            if dado == 20:
                print(f"\nACERTO CRÍTICO!\nVocê usou o kage bunshin no jutsu, tirando um total de {dano2} PV do inimigo.")
                pv2 = pv2 - dano2
                print(f"PV do inimigo: {pv2}")
            else:
                print(f"\nVocê usou o kage bunshin no jutsu, tirando um total de {dano} PV do inimigo.")
                pv2 = pv2 - dano
                print(f"PV do inimigo: {pv2}")
        
        elif habilidade == '2':
            dado = randint(1,20)
            dano = 15 * dado
            dano2 = dano * 2
            if dado == 20:
                print(f"\nACERTO CRÍTICO!\nVocê acertou o inimigo com um rasengan, tirando um total de {dano2} PV do inimigo.")
                pv2 = pv2 - dano2
                print(f"PV do inimigo: {pv2}")
            else:
                print(f"\nVocê acertou o inimigo com um rasengan, tirando um total de {dano} PV do inimigo.")
                pv2 = pv2 - dano
                print(f"PV do inimigo: {pv2}")
        
        elif habilidade == '3':
            dado = randint(1,20)
            dano = 20 * dado
            dano2 = dano * 2
            if dado == 20:
                print(f"\nACERTO CRÍTICO!\nVocê acertou o inimigo com um rasenshuriken, tirando um total de {dano2} PV.")
                pv2 = pv2 - dano2
                print(f"PV do inimigo: {pv2}")
            else:
                print(f"\nVocê acertou o inimigo com um rasenshuriken, tirando um total de {dano} PV.")
                pv2 = pv2 - dano
                print(f"PV do inimigo: {pv2}")
    
    for i in range(1):
        habilidade2 = choice(h2)
        if habilidade2 == 'goukakyuu no jutsu':
            dado = randint(1,20)
            dano = 10 * dado
            dano2 = dano * 2
            if dado == 20:
                print(f"\nACERTO CRÍTICO!\nO inimigo te acertou com um goukakyuu no jutsu, tirando um total de {dano2} PV.")
                pv1 = pv1 - dano2
                print(f"Seu PV: {pv1}")
            else:
                print(f"\nO inimigo te acertou com um goukakyuu no jutsu, tirando um total de {dano} PV.")
                pv1 = pv1 - dano
                print(f"Seu PV: {pv1}")
        
        elif habilidade2 == 'chidori':
            dado = randint(1,20)
            dano = 15 * dado
            dano2 = dano * 2
            if dado == 20:
                print(f"\nACERTO CRÍTICO!\nO inimigo te acertou com um chidori, tirando um total de {dano2} PV.")
                pv1 = pv1 - dano2
                print(f"Seu PV: {pv1}")
            else:
                print(f"\nO inimigo te acertou com um chidori, tirando um total de {dano} PV.")
                pv1 = pv1 - dano
                print(f"Seu PV: {pv1}")
        
        elif habilidade2 == 'amaterasu':
            dado = randint(1,20)
            dano = 20 * dado
            dano2 = dano * 2
            if dado == 20:
                print(f"\nACERTO CRÍTICO!\nO inimigo usou o amaterasu em você, tirando um total de {dano2} PV.")
                pv1 = pv1 - dano2
                print(f"Seu PV: {pv1}")
            else:
                print(f"\nO inimigo usou o amaterasu em você, tirando um total de {dano} PV.")
                pv1 = pv1 - dano
                print(f"Seu PV: {pv1}")
else:
    if pv1 <= 0 and pv2 <=0:
        print()
        print("*"*40)
        print("A batalha terminou em empate.\nDescansem e lutem novamente mais tarde.")
        print("*"*40)
    elif pv1 <= 0:
        print()
        print("*"*20)
        print("Você perdeu.")
        print("*"*20)
    elif pv2 <= 0:
        print()
        print("*"*20)
        print("Você venceu!!!")
        print("*"*20)