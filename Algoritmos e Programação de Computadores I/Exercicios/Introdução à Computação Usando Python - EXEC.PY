"""
Introdução à Computação Usando Python - Um Foco no Desenvolvimento de Aplicações

Exercícios - Capitulo 2 - Pagina 48

Não irei realizar todos os exercicios propostos no capitulo, porém o mais divertidos irei.
"""
import statistics

"""
Exercício 2.1
Escreva expressões algébricas Python correspondentes aos seguintes comandos:
(a) A soma dos 5 primeiros inteiros positivos.
(b) A idade média de Sara (idade 23), Mark (idade 19) e Fátima (idade 31).
(c) O número de vezes que 73 cabe em 403.
(d) O resto de quando 403 é dividido por 73.
(e) 2 à 10ª potência.
(f) O valor absoluto da distância entre a altura de Sara (54 polegadas) e a altura de Mark (57 polegadas).
(g) O menor preço entre os seguintes preços: R$ 34,99, R$ 29,95 e R$ 31,50.

"""

## 2.12
# A
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"{sum(lista[0:5])}")

# for x in range(0, 7, 1):
#     print(x)


# B
idade_pessoas_2 = {"Sara": 23, "Mark": 19, "Fatima": 31}
idades_pessoas = [23, 19, 31]
print(f"Idade Média: {statistics.mean(idades_pessoas)}")

# C
print(f"Quantas vezes 73 cabe em 403: {403 // 73}")

# D
print(f"O resto da divisão de 403 por 73 é: {403 % 73}")

# E
print(f"2 elevado a 20 é: {2**20}")

# F
print(f"A diferença entre a altura de Sara (54 polegadas) e a altura de Mark (57 polegadas) é: {abs(54 - 57)}")

# G
print(f"O menor preço entre os seguintes preços: {min([34.99, 29.95, 31.50])}")


"""
Exercício 2.2
Traduza os comandos a seguir para expressões Booleanas em Python e avalie-as:
(a) A soma de 2 e 2 é menor que 4.
(b) O valor de 7 // 3 é igual a 1 + 1.
(c) A soma de 3 ao quadrado e 4 ao quadrado é igual a 25.
(d) A soma de 2, 4 e 6 é maior que 12.
(e) 1387 é divisível por 19.
(f) 31 é par. (Dica: o que o resto lhe diz quando você divide por 2?)
(g) O preço mais baixo dentre R$ 34,99, R$ 29,95 e R$ 31,50 é menor que R$ 30,00.*

"""

# A 
print(f"A soma de 2 e 2 é menor que 4: {2 + 2 < 4}")

# B
print(f"O valor de 7 // 3 é igual a 1 + 1: {7 // 3 == 1 + 1}")

# C
print(f"A soma de 3 ao quadrado e 4 ao quadrado é igual a 25: {3**2 + 4**2 == 25}")

# D
print(f"A soma de 2, 4 e 6 é maior que 12: {2 + 4 + 6 > 12}")

# E
print(f"1387 é divisível por 19: {1387 % 19 == 0}")

# F
print(f"31 é par: {31 % 2 == 0}")

# G
print(f"O preço mais baixo dentre R$ 34,99, R$ 29,95 e R$ 31,50 é menor que R$ 30,00: {min([34.99, 29.95, 31.50]) < 30}")

"""
Exercício 2.3
Escreva instruções Python que correspondem às ações a seguir e execute-as:
(a) Atribua o valor inteiro 3 à variável a.
(b) Atribua 4 à variável b.
(c) Atribua à variável c o valor da expressão a * a + b * b.
"""

# A
a = 3

# B
b = 4

# C
c = a * a + b * b

"""
Exercício 2.4
Comece executando as instruções de atribuição:
>>> s1 = 'ant'
>>> s2 = 'bat'
>>> s3 = 'cod'
Escreva expressões Python usando s1, s2 e s3 e os operadores + e * a fim de avaliar para:
(a) 'ant bat cod'
(b) ant ant ant ant ant ant ant ant ant ant'
(c) 'ant bat bat cod cod cod'
(d) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
(e) 'batbatcod batbatcod batbatcod batbatcod batbatcod'
"""

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

# A
print(f"{s1} {s2} {s3}")

# B
print(f"{s1 * 10}")

# C
print(f"{s1 } {((s2 + ' ') * 2)}{((s3 + ' ') * 3)}")

# D
print(f"{(s1 + ' ' + s2 + ' ') * 7}")

# E
print(f"{(s2+s2+s3 + ' ') * 7}")

"""
Exercício 2.5
Comece executando a atribuição:
s = '0123456789'
Agora, escreva expressões usando a string s e o operador de indexação que é avaliado como:
(a) '0'
(b) '1'
(c) '6'
(d) '8'
(e) '9'
"""
s = '0123456789'

# A
print(f"{s[0]}")

# B
print(f"{s[1]}")

# C
print(f"{s[6]}")

# D
print(f"{s[8]}")

# E
print(f"{s[9]}")
