DNA_PARA_AMINOACIDO = {
    'TTT': 'F',
    'TTC': 'F',
    'TTA': 'L',
    'TTG': 'L',
    'TCT': 'S',
    'TCC': 'S',
    'TCA': 'S',
    'TCG': 'S',
    'TAT': 'Y',
    'TAC': 'Y',
    'TGT': 'C',
    'TGC': 'C',
    'TGG': 'W',
    'CTT': 'L',
    'CTC': 'L',
    'CTA': 'L',
    'CTG': 'L',
    'CCT': 'P',
    'CCC': 'P',
    'CCA': 'P',
    'CCG': 'P',
    'CAT': 'H',
    'CAC': 'H',
    'CAA': 'Q',
    'CAG': 'Q',
    'CGT': 'R',
    'CGC': 'R',
    'CGA': 'R',
    'CGG': 'R',
    'ATT': 'I',
    'ATC': 'I',
    'ATA': 'I',
    'ATG': 'M',
    'ACT': 'T',
    'ACC': 'T',
    'ACA': 'T',
    'ACG': 'T',
    'AAT': 'N',
    'AAC': 'N',
    'AAA': 'K',
    'AAG': 'K',
    'AGT': 'S',
    'AGC': 'S',
    'AGA': 'R',
    'AGG': 'R',
    'GTT': 'V',
    'GTC': 'V',
    'GTA': 'V',
    'GTG': 'V',
    'GCT': 'A',
    'GCC': 'A',
    'GCA': 'A',
    'GCG': 'A',
    'GAT': 'D',
    'GAC': 'D',
    'GAA': 'E',
    'GAG': 'E',
    'GGT': 'G',
    'GGC': 'G',
    'GGA': 'G',
    'GGG': 'G'
}

DNA_STOP_CODONS = ['TAA', 'TAG', 'TGA']

# Tabela de complemento de bases, incluindo os códigos IUPAC de ambiguidade.
#
# As 4 bases "normais" seguem o pareamento do DNA: A-T e C-G.
#
# Já os códigos de ambiguidade (quando não sabemos ao certo qual é a base,
# e por isso usamos uma letra que representa um GRUPO de bases possíveis)
# têm como complemento o código que representa o grupo das bases
# complementares. Ou seja: pegue cada base do grupo, ache o complemento
# dela (A<->T, C<->G) e veja qual letra representa esse novo grupo.
#
# Exemplo: M = A ou C (amino). O complemento de A é T, o complemento de C
# é G. Logo o complemento de M é o código que representa {T, G} -> K.
CONVERSOR_DE_BASE = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C',
    'R': 'Y',  # R = A ou G (purina)     -> complemento = T ou C = Y (pirimidina)
    'Y': 'R',  # Y = C ou T (pirimidina) -> complemento = G ou A = R (purina)
    'S': 'S',  # S = G ou C (forte)      -> complemento = C ou G = S (não muda)
    'W': 'W',  # W = A ou T (fraca)      -> complemento = T ou A = W (não muda)
    'K': 'M',  # K = G ou T (keto)       -> complemento = C ou A = M (amino)
    'M': 'K',  # M = A ou C (amino)      -> complemento = T ou G = K (keto)
    'B': 'V',  # B = C, G ou T (não A)   -> complemento = G, C ou A = V (não T)
    'V': 'B',  # V = A, C ou G (não T)   -> complemento = T, G ou C = B (não A)
    'D': 'H',  # D = A, G ou T (não C)   -> complemento = T, C ou A = H (não G)
    'H': 'D',  # H = A, C ou T (não G)   -> complemento = T, G ou A = D (não C)
    'N': 'N',  # N = qualquer base       -> complemento = qualquer base
}
