# O Projeto: um panorama da família Flaviviridae
#
# Leia o enunciado completo no README (seção "O Projeto")
#
# A ideia é construir UMA tabela (pandas) descrevendo os vírus e, a partir dela,
# tirar duas conclusões:
#   - o conteúdo GC é aleatório? (Parte 2)
#   - quão grande é a proteína de cada vírus? (Parte 3)
#
# Vá preenchendo as partes abaixo, uma de cada vez.
# Obs: Se preferir fazer esse processo num jupyter notebook, sem problemas!! Fica a critério do grupo

import pandas as pd

pd.set_option('display.max_columns', None)   # mostra todas as colunas
pd.set_option('display.width', None)         # não quebra linha por largura do terminal
pd.set_option('display.max_colwidth', 30)

from bio.ler_fasta import ler_fasta
from bio.sequencia import (
    traduzir,
    calcular_percentual_gc,
    encontrar_inicio,
)


# ------------------------------------------------------------------
# Parte 1 — Monte a tabela
# ------------------------------------------------------------------
organismos = ler_fasta("arquivos/Flaviviridae-genomes.fasta")
df = pd.DataFrame(organismos)
df["tamanho"] = df["sequencia"].apply(len)
print(df.head())

# ------------------------------------------------------------------
# Parte 2 — O conteúdo GC é aleatório?
# ------------------------------------------------------------------
# 1) crie a coluna "gc" com df["sequencia"].apply(calcular_percentual_gc)
# 2) mostre os 10 maiores e os 10 menores GC (com o nome!) -> usar função sort_values do pandas
# 3) escreva sua conclusão sobre o padrão que observou

# Cria a coluna "gc"
df["gc"] = df["sequencia"].apply(calcular_percentual_gc)

# Ordena a tabela do maior GC para o menor
df = df.sort_values("gc", ascending=False)

# Mostra os 10 vírus com maior GC
print("\n10 vírus com maior conteúdo GC:")
print(df[["nome", "gc"]].head(10))

# Mostra os 10 vírus com menor GC
print("\n10 vírus com menor conteúdo GC:")
print(df[["nome", "gc"]].tail(10))

# Conclusão:
# O conteúdo GC não parece ser aleatório. Os vírus com maior GC são,
# em sua maioria, Pegivirus e Hepatitis C virus, enquanto os de menor
# GC pertencem principalmente ao grupo Pestivirus. Isso sugere que vírus
# evolutivamente aparentados apresentam composição de bases semelhante.


# ------------------------------------------------------------------
# Parte 3 — Encontre a proteína (a poliproteína viral)
# ------------------------------------------------------------------
# 1) coluna "proteina": traduzir(encontrar_inicio(seq), parar=True)
# 2) coluna "tamanho_proteina": len da proteína
# 3) coluna "cobertura": (tamanho_proteina * 3) / tamanho
# 4) escreva sua conclusão (qual a cobertura típica? faz sentido ser 1 poliproteína?)


# Modifica a sequência para começar no primeiro códon ATG
df["sequencia"] = df["sequencia"].apply(encontrar_inicio)

# Traduz a sequência e para no primeiro stop codon
df["proteina"] = df["sequencia"].apply(
    lambda sequencia: traduzir(sequencia, parar=True)
)

# Calcula o número de aminoácidos da proteína
df["tamanho_proteina"] = df["proteina"].apply(len)

# Calcula a fração do genoma ocupada pela proteína
df["cobertura"] = (
    df["tamanho_proteina"] * 3
) / df["tamanho"]

# Mostra algumas linhas para conferência
print("\nProteínas encontradas:")
print(
    df[
        [
            "nome",
            "tamanho",
            "tamanho_proteina",
            "cobertura",
        ]
    ].head(10)
)

# Calcula a cobertura típica
cobertura_mediana = df["cobertura"].median()

print("\nCobertura mediana:")
print(cobertura_mediana)

# Conclusão:
# A cobertura mediana foi de aproximadamente 0.93 (93% do genoma).
# Isso indica que, para a maioria dos vírus, a poliproteína ocupa quase
# todo o genoma. Alguns vírus apresentaram cobertura baixa, provavelmente
# porque o primeiro códon ATG encontrado não corresponde ao início real do gene.

# ------------------------------------------------------------------
# Parte 4 — Salve o resultado
# ------------------------------------------------------------------
# 1) filtre os vírus com gc > 0.5 (quantos são?)
# 2) df.to_csv("resultado.csv", index=False)

# Filtra os vírus com conteúdo GC maior que 50%
virus_gc_alto = df[df["gc"] > 0.5]

print("\nQuantidade de vírus com GC acima de 50%:")
print(len(virus_gc_alto))

# Salva a tabela completa em um arquivo CSV
df.to_csv("resultado.csv", index=False)
#Salva a tabela completa em um arquivo Excel xlsx
df.to_excel("resultado.xlsx", index=False)

print("\nArquivos salvos com sucesso!")

