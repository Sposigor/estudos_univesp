"""
Problema Prático 3.2

Traduza estas instruções condicionais em instruções if do Python:

(a) Se idade é maior que 62, exiba "Você pode obter benefícios de pensão".

(b) Se o nome está na lista ["Musial", "Aaraon", "Williams", "Gehrig", "Ruth"], exiba "Um dos 5 maiores jogadores de beisebol de todos os tempos!".

(c) Se golpes é maior que 10 e defesas é 0, exiba "Você está morto…".

(d) Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste for True, exiba "Posso escapar.".
"""


# a
idade = 63
if idade > 62:
    print("Você pode obter benefícios de pensão")
else:
    print("Ainda não atingiu a idade para obter o benefício de pensão")

# b
lista = ["Musial", "Aaraon", "Williams", "Gehrig", "Ruth"]
nome = "Ruth"

if nome in lista:
    print("Um dos 5 maiores jogadores de beisebol de todos os tempos!")
else:
    print("Não é um dos 5 maiores jogadores de beisebol de todos os tempos!")

# c
golpes = 11
defesas = 0
if golpes > 10 and defesas == 0:
    print("Você está morto…")
else:
    print("Você ainda está vivo")

# d
norte = False
sul = True
leste = False
oeste = True

if norte or sul or leste or oeste:
    print("Posso escapar")
else:
    print("Não posso escapar")


"""
Problema Prático 3.3

Traduza estas declarações em instruções if/else do Python:

(a) Se ano é divisível por 4, exiba 'Pode ser um ano bissexto.'; caso contrário, exiba 'Definitivamente não é um ano bissexto.'

(b) Se a lista bilhete é igual à lista loteria, exiba 'Você ganhou!'; se não, exiba 'Melhor sorte da próxima vez…'.
"""

# a
ano = 2020
if ano % 4 == 0:
    print("Pode ser um ano bissexto")
else:
    print("Definitivamente não é um ano bissexto")

# b
bilhete = [1, 40, 3, 85, 94, 6]
loteria = [1, 42, 3, 85, 94, 6]
if bilhete == loteria:
    print("Você ganhou!")
else:
    print("Mais sorte da próxima vez…")

"""
Problema Prático 3.4

Implemente um programa que comece pedindo ao usuário para digitar uma identificação de login (ou seja, uma string).
O programa, então, verifica se a identificação informada pelo usuário está na lista ['joe', 'sue', ' hani', 'sophie' ] de usuários válidos.
Dependendo do resultado, uma mensagem apropriada deverá ser impressa.
Não importando o resultado, sua função deverá exibir 'Fim.' antes de terminar.
Aqui está um exemplo de um login bem-sucedido:

>>>

Login: joe

Você entrou!

Fim.

E aqui está um que não tem sucesso:

>>>

Login: john

Usuário desconhecido.

Fim.
"""

# problema 3.4

usuarios = ['joe', 'sue', 'hani', 'sophie']

login = str(input("Login: "))

if login in usuarios:
    print("Você entrou!")
    print("Fim.")
else:
    print("Usuário desconhecido.")
    print("Fim.")


"""
Problema Prático 5.1

Implemente a função meuIMC(), que aceita como entrada a altura de uma pessoa (em metros) e o peso (em quilos)
e calcula o Índice de Massa Corporal (IMC) dessa pessoa. A fórmula do IMC é:

Illustration

Sua função deverá exibir a string 'Abaixo do peso' se o imc < 18.5, 'Normal' se 18,5 <= imc < 25, e 'Sobrepeso' se imc >= 25.

>>> meuIMC *86, 1.90)

Normal

>>> meuIMC (63, 1.90)

Abaixo do peso
"""

# problema 5.1
def meuIMC(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        print("Abaixo do peso")
    elif 18.5 <= imc < 25:
        print("Normal")
    else:
        print("Sobrepeso")

meuIMC(63, 1.90)
meuIMC(86, 1.90)
meuIMC(120, 1.90)