"""
Introdução à Computação Usando Python - Um Foco no Desenvolvimento de Aplicações

Exercícios - Capitulo 2 - Pagina 48
"""
import statistics


## 2.12
# A
for x in range(0, 7, 1):
    x = x + 1
    print(x)

# B
idades_pessoas = [64, 56, 45]
print(f"Idade Média: {statistics.mean(idades_pessoas)}")

# C
print(f"2 elevado a 20 é: {2**20}")

# D
print(f"Quantas vezes 61 cabe em 4356: {4656 // 61}")

# E
print(f"Quantas vezes 61 cabe em 4356: {61 // 4656}")

## 2.13
S1 = "-"
S2 = "+"


# A '-+'

print(f"A {S1 + S2}")

# B '+-'

print(f"B {S2 + S1}")

# C '+––'

print(f"C {S2 + (S1*2)}")

# D '+––+––'

print(f"D {(S2 + (S1*2)) * 2}")

# E '+––+––+––+––+––+––+––+––+––+––+'

print(f"E {(S2 + (S1*2)) * 10 + S2}")

# F '+–+++––+–+++––+–+++––+–+++––+–+++––'

print(f"F {(((S2+S1) + (S2*3) + (S1*2)) * 5)}")


## 2.14
#  s = 'abcdefghijklmnopqrstuvwxyz' indexa 'a', 'c', 'z', 'y' e 'q'

s = 'abcdefghijklmnopqrstuvwxyz'
print(f"{s[0]}, {s[2]}, {s[-1]}. {s[-2]}, {s[-10]}")


#@ 2.15

# s = 'goodbye'

s = 'goodbye'

# A

print(f"A {s[0] == 'g'}")

# B