"""
Madlibs em python é um jogo onde dado os 'prompts' de input sem o contexto geral ao usuário
ele define strings que serão usadas no texto final.
"""

#mostrar o nome do projeto e linguagem
print("Madlibs em Python")
#mostrar uma linha vazia
print()

#definindo as variáveis que estarão no texto final
dia_da_semana = input("Digite um dia da semana: ")
sentimento = input("Digite um sentimento no singular: ")
data_especial = input("Digite uma data especial: ")
verbo1 = input("Digite um verbo: ")
verbo2 = input("Digite outro verbo: ")
adjetivo_diminutivo = input("Digite um adjetivo no diminutivo: ")
local = input("Digite um local: ")
verbo3 = input("Digite mais um verbo: ")
substantivo_comum = input("Digite um substantivo comum: ")

#mostrar uma linha vazia
print()

#mostrar que esse é o texto feito pelo usuário
print("Esse é o seu texto!")

#mostrar o texto final
print(f"Hoje é {dia_da_semana.lower()} e eu estou muito {sentimento}. Na verdade eu gostaria que fosse {data_especial} para que eu pudesse {verbo1} e {verbo2}. Tenho um amigo famoso, o {adjetivo_diminutivo} e nós sempre vamos ao {local}. Quando estamos lá, nós gostamos de {verbo3} no {substantivo_comum}.")
