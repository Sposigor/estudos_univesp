"""
Exercicio proposto Algoritmos e Programação de Computadores I - Semana 1 - COM EXEC 02

Exercicio: Modifique o exemplo anterior para calcular a média de notas para 100 alunos

Exemplo dado:

Inicio:
Leia N1
Leia N2
Leia N3
M = (N1 + N2 + N3) / 3
SE M > 5 ENTÃO:
    Escreva("O aluno passou")
Senão
    Escreva("O aluno não Passou)


Desenvolva o Algoritmo e o Fluxograma

Para isso vamos usar um arquivo csv com quatro colunas:

- Numero: Que vai ser a numeração do aluno
- N1: Nota N1
- N2: Nota N2
- N3: Nota N3

Após o calculo de cada média, o aluno vai recer uma média e um status que vão ser inclusos no txt

- Média: Vai ser o calculo (N1 + N2 + N3) / 3
- Status: Se ele foi aprovado ou não

"""
import pandas as pd
import numpy as np


def calcular_média_aluno_e_criando_um_novo_csv():

    """Algoritmo simples para obter a média do aluno"""

    # Leitura dos dados usando o pandas para facilitar a manipulação
    dados = pd.read_csv(r"COM - EXEC 02 - DADOS.csv", ",", encoding="utf-8")

    # Criando a média proposta pelo exercicio
    media = (dados["N1"] + dados["N2"] + dados["N3"])/3

    # Incluido a média no objeto dataframe e aredondado ela para 1 casa decimal
    dados["Média"] = round(media, 1)

    # Incluido o status com a condição usando o numpy
    dados["Status"] = np.where(dados["Média"] > 5, "Aprovado", "Reprovado")

    # Vamos trasnforma o objeto dataframe em csv
    dados.to_csv("COM - EXEC 02 - RESULTADO.csv", sep=",", encoding="utf-8", index=False)


def main() -> None:
    """Função Main"""
    calcular_media = calcular_média_aluno_e_criando_um_novo_csv()


if __name__ == '__main__':
    main()
