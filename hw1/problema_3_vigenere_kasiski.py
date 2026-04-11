print("\n=== Problema 3: Vigenère Kasiski ===")
p3_ct = """ECISCRVSWVLGDDWUEFHFNGESXUVTICOKQOTA.JPHWAKFBNA
EUONOJFHONCPHRZNSCOKEWLSUFPFEEUWOMHPQFAEEDOLDB
QROKFZLNQBSXVMFZZNMQQSACESDDVMONHBROUEBGMOCVI
SLZAOXDGTJDAQVZLDRTOVAKDDWOKJTFEJBBFNHBGLCRJRLS
KVEVUDBXOPVDVZADBGSLCPOKUWSSJCRQWCOLFOKUC"""

# Limpiamos el criptograma de caracteres no alfabéticos
p3_ct = "".join(c for c in p3_ct if c.isalpha())

# Buscar secuencias repetidas de longitud > 2
from math import gcd
from functools import reduce

def find_repeats(text, min_len=3):
    repeats = {}
    for l in range(min_len, 6): # buscar palabras de hasta longitud 5
        for i in range(len(text) - l):
            seq = text[i:i+l]
            for j in range(i + l, len(text) - l):
                if text[j:j+l] == seq:
                    dist = j - i
                    if seq not in repeats:
                        repeats[seq] = []
                    repeats[seq].append(dist)
    return repeats

reps = find_repeats(p3_ct)
distances = []
for seq, dists in reps.items():
    if len(dists) > 0:
        print(f"Secuencia '{seq}' distancias: {dists}")
        distances.extend(dists)

def find_gcd_list(lst):
    return reduce(gcd, lst)

if distances:
    print(f"Posibles divisores comunes de las distancias: {[i for i in range(2, 20) if all(d % i == 0 for d in distances)]}")
    # A veces es mejor encontrar los factores de la moda o simplemente listar factores comunes
    factors = {}
    for d in distances:
        for i in range(2, d+1):
            if d % i == 0:
                factors[i] = factors.get(i, 0) + 1
    # Mostramos los factores resultantes
    print(f"Factores más comunes: {sorted(factors.items(), key=lambda x: x[1], reverse=True)[:5]}")

