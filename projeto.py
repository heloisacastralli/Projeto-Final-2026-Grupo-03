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
print(df.head())

# Criando a coluna "tamanho"
df['tamanho'] = df.apply(lambda linha: len(linha['sequencia']), axis=1)

# ------------------------------------------------------------------
# Parte 2 — O conteúdo GC é aleatório?
# ------------------------------------------------------------------
# 1) crie a coluna "gc" com df["sequencia"].apply(calcular_percentual_gc)

df['gc'] = df['sequencia'].apply(calcular_percentual_gc)

# 2) mostre os 10 maiores e os 10 menores GC (com o nome!) -> usar função sort_values do pandas

# 10 maiores conteúdos GC
print('\n10 maiores conteúdos GC')
print(df.sort_values(by='gc', ascending=False)[['nome', 'gc']].head(10))

# 10 menores conteúdos GC
print('\n10 menores conteúdos GC')
print(df.sort_values(by='gc', ascending=True)[['nome', 'gc']].head(10))

# 3) escreva sua conclusão sobre o padrão que observou

# Os pegivirus e hepatites apresentam os maiores conteúdos GC. Os pestivirus apresentam os menores conteúdos GC.

# ------------------------------------------------------------------
# Parte 3 — Encontre a proteína (a poliproteína viral)
# ------------------------------------------------------------------
# 1) coluna "proteina": traduzir(encontrar_inicio(seq), parar=True)

df['proteina'] = df['sequencia'].apply(lambda seq: traduzir(encontrar_inicio(seq), parar=True))

# 2) coluna "tamanho_proteina": len da proteína

df['tamanho_proteina'] = df['proteina'].apply(len)

# 3) coluna "cobertura": (tamanho_proteina * 3) / tamanho

df['cobertura'] = df.apply(lambda linha: (linha['tamanho_proteina']*3) / linha['tamanho'], axis = 1)

# 4) escreva sua conclusão (qual a cobertura típica? faz sentido ser 1 poliproteína?)


# ------------------------------------------------------------------
# Parte 4 — Salve o resultado
# ------------------------------------------------------------------
# 1) filtre os vírus com gc > 0.5 (quantos são?)

filtro_gc = df['gc'] > 0.5

df_filtro_gc = df[filtro_gc]

# 2) df.to_csv("resultado.csv", index=False)

df_filtro_gc.to_csv('resultado.csv', index=False)
