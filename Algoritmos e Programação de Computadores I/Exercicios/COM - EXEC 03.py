"""
Exercício de apoio - Semana 4
Pratique o conteúdo da semana fazendo os exercícios do livro Introdução a Computação Usando Python que seguem abaixo:

Exercício 3.1

Implemente um programa que solicita a temperatura atual em graus Fahrenheit do usuário e exibe a temperatura em graus Celsius usando a fórmula 
texto  celsius  fim do texto igual a 5 sobre 9 parêntese esquerdo texto  fahrenheit  fim do texto menos 32 parêntese direito Clique para obter mais opções
Seu programa deverá ser executado da seguinte forma: 
>>> Digite a temperatura em graus Fahrenheit: 50 
>>> A temperatura em graus Celsius é 10.0 

Exercício 3.8

Defina, diretamente no shell interativo, a função média(), que aceita dois números como entrada e retorna a média dos números. Um exemplo de uso é: 
>>> average(2, 3.5) 
>>> 2.75 

Exercício 3.9

Implemente a função perímetro(), que aceita, como entrada, o raio de um círculo (um número não negativo) e retorna o perímetro do círculo. Você deverá escrever sua implementação em um módulo chamado perímetro.py. Um exemplo de uso é: 
>>> perimeter(1) 
>>> 6.283185307179586 

Exercício 3.10

Escreva a função negativos(), que aceita uma lista como entrada e exibe, um por linha, os valores negativos na lista. A função não deverá retornar nada. 
>>> negatives([4, 0, -1, -3, 6, -9]) 
>>> -1 
>>> -3 
>>> -9 

Exercício 3.11

Acrescente a docstring retorna a média de x e y à função média() e a docstring exibe os números negativos contidos na lista lst à função negativos() dos Problemas Práticos 3.8 e 3.10. Verifique seu trabalho usando a ferramenta de documentação help(). Você deverá receber, por exemplo: 
>>> help(média) 
Ajuda sobre a função média no módulo __main__: 
média(x, y)
    retorna a média de x e y 

Exercício 3.12

Desenhe um diagrama representando o estado dos nomes e objetos após esta execução: 
>>> a = [5, 6, 7] 
>>> b = a 
>>> a = 3 

Exercício 3.13

Suponha que uma lista não vazia time foi atribuída. Escreva uma instrução Python ou instruções que mapeiam o primeiro e último valor da lista. Assim, se a lista original for: 
>>> time = ['Ava', 'Eleanor', 'Clare', 'Sarah'] 
então a lista resultante deverá ser: 
>>> time 
>>> ['Sarah', 'Eleanor', 'Clare', 'Ava'] 

Exercício 3.14

Implemente a função trocaPU(), que aceita uma lista como entrada e troca o primeiro e último elementos da lista. Você pode considerar que a lista não estará vazia. A função não deverá retornar nada. 
>>> ingredientes = ['farinha', 'açúcar', 'manteiga', 'maçãs'] 
>>> trocaPU(ingredientes) 
>>> ingredientes 
>>> ['maçãs', 'açúcar', 'manteiga', 'farinha'] 

"""


# Exercício 3.1

fah = float(input("Digite a temperatura em graus Fahrenheit: "))
cel = 5 * (fah - 32) / 9
print("A temperatura em graus Celsius é", cel)

# Exercício 3.8
def average(x, y):
    return (x + y) / 2
print(average(2, 3.5))

# Exercício 3.9
def perimetro(x):
    import math
    r = x
    return 2 * math.pi * r
print(perimetro(1))

# Exercício 3.10
def negatives(lst):
    for x in lst:
        if x < 0:
            print(x)

negatives([4, 0, -1, -3, 6, -9])

# Exercício 3.11
time = ['Ava', 'Eleanor', 'Clare', 'Sarah']
time.sort(reverse=True)
print(time)

# Exercício 3.14
ingredientes = ['farinha', 'açúcar', 'manteiga', 'maçãs']

def trocaPU(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    print(lst)

trocaPU(ingredientes)