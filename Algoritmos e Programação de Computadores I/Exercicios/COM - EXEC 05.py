"""

Exercício 3.5

Implemente um programa que solicite do usuário uma lista de palavras (ou seja, strings) e depois exiba na tela, 
uma por linha, todas as strings de quatro letras nessa lista. 

>>> 
Digite a lista de palavras: ['pare', 'desktop', 'tio', 'pote'] 
pare pote 

Exercício 3.6

Escreva o laço for que exibirá as sequências de números a seguir, um por linha, no shell interativo do Python. 
 
(a)Inteiros de 0 a 9 (isto é, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9). 
 
(b)Inteiros de 0 a 1 (isto é, 0, 1). 

Exercício 3.7

Escreva um laço for que exiba a seguinte sequência de números, um por linha. 
 
(a)Inteiros de 3 até 12, inclusive este. 
 
(b)Inteiros de 0 até (mas não incluindo) 9, com um passo de 2 em vez do padrão 1 (isto é, 0, 2, 4, 6, 8). 
 
(c)Inteiros de 0 até (mas não incluindo) 24, com um passo de 3. 
 
(d)Inteiros de 3 até (mas não incluindo) 12, com um passo de 5. 

"""

# Exercicio 3.5
palavras = []

def palavras_com_4_letras(palavras):
    x = str(input("Digite uma lista de palavras separadas por espaço: "))

    for i in x.split():
        if len(i) == 4:
            palavras.append(i)
    
    for i in palavras:
        print(i)

palavras_com_4_letras(palavras)


# Exercicio 3.6
def numeros_0_a_9():
    for i in range(10):
        print(i)

def numeros_0_a_1():
    for i in range(2):
        print(i)

numeros_0_a_9()
numeros_0_a_1()

# Exercicio 3.7
def numeros_3_a_12():
    for i in range(3, 13):
        print(i)

def numeros_0_a_9_2():
    for i in range(0, 10, 2):
        print(i)

def numeros_0_a_24_3():
    for i in range(0, 25, 3):
        print(i)

def numeros_3_a_12_5():
    for i in range(3, 13, 5):
        print(i)

numeros_3_a_12()
numeros_0_a_9_2()
numeros_0_a_24_3()
numeros_3_a_12_5()
