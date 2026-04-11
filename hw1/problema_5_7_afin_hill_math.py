import numpy as np
from sympy import Matrix

# ===== PROBLEMA 5: CIFRADO HILL =====
alfabeto5 = "abcdefghijklmnñopqrstuvwxyzAEN "
def char_to_idx(c):
    if c in alfabeto5: return alfabeto5.index(c)
    return -1

key_str = "Elliot Alderson fsocietys"
key_nums = [char_to_idx(c) for c in key_str]
print("Key indices:", key_nums)
K = np.array(key_nums).reshape((5, 5))
print("K =")
print(K)

K_sym = Matrix(K)
det_K = K_sym.det() % 31
print(f"det(K) mod 31 = {det_K}")
K_inv = K_sym.inv_mod(31)
print("K_inv =")
print(np.array(K_inv))

# El texto cifrado base extraído de la imagen del PDF: "xqacAzwNxscuevA"
# Pero verificamos variantes por posibles ambigüedades en la transcripción:
for hill_ct in ["xqacAzwNxscuevA", "xqacAvlxscucvA "]:
    print(f"\n--- trying: '{hill_ct}' (len={len(hill_ct)}) ---")
    if len(hill_ct) % 5 != 0:
        hill_ct = hill_ct + " " * (5 - len(hill_ct) % 5)
    blocks = [hill_ct[i:i+5] for i in range(0, len(hill_ct), 5)]
    pt = ""
    K_inv_np = np.array(K_inv).astype(int)
    for block in blocks:
        vec = np.array([char_to_idx(c) for c in block])
        dec_vec = np.dot(K_inv_np, vec) % 31
        for num in dec_vec:
            pt += alfabeto5[num]
    print(f"P = K^-1 * C: {pt}")

# ===== PROBLEMA 7: DESCIFRADO AFÍN =====
print("\n===== P7 descifrado =====")
alfabeto = "abcdefghijklmnñopqrstuvwxyz"
N = 27
A_inv = 20
B = 10
# Texto cifrado original transcrito del PDF (presentaba 'ñn' en vez de la 'ñ' normal)
ct_correct = "ua hcelqrñnquqñn ft ua seqñn efmfuqhqoñn gf ua frqtlfñnhqñn"
pt = ""
for c in ct_correct:
    if c in alfabeto:
        C = alfabeto.index(c)
        m = (A_inv * (C - B)) % N
        pt += alfabeto[m]
    else:
        pt += c
print(f"Descifrado P7 (con ñn): {pt}")

# También intentamos con la versión asumiendo que el original venía sin la doble letra extra:
ct_orig = "ua hcelqrñquqñ ft ua seqñ efmfuqhqoñ gf ua frqtlfñhqñ"
pt2 = ""
for c in ct_orig:
    if c in alfabeto:
        C = alfabeto.index(c)
        m = (A_inv * (C - B)) % N
        pt2 += alfabeto[m]
    else:
        pt2 += c
print(f"Descifrado P7 (sin n): {pt2}")

# ===== PROBLEMA 6c: VIGENÈRE CON ZHUANGZI =====
print("\n===== P6c =====")
# El criptograma transcrito tiene un carácter "á" acentuado visiblemente: "tuu mrtsm pby efzá pchlna rr tvhcyrfu dvsllo fk qqmky"
# Usamos Zhuangzi como clave:
ct6c = "tuumrtsmpbyefzapchlnarrtvhcyrfudvsllofkqqmky"
key6c = "zhuangzi"

# Evaluar descifrado con módulo 27 (alfabeto español con 'ñ')
pt_27 = ""
ki = 0
for c in ct6c:
    if c in alfabeto:
        cc = alfabeto.index(c)
        kk = alfabeto.index(key6c[ki % len(key6c)])
        pt_27 += alfabeto[(cc - kk) % 27]
        ki += 1
print(f"P6c (mod 27): {pt_27}")

# Evaluar descifrado con módulo 26 (alfabeto estándar inglés sin 'ñ')
alfa26 = "abcdefghijklmnopqrstuvwxyz"
pt_26 = ""
ki = 0
for c in ct6c:
    if c in alfa26:
        cc = alfa26.index(c)
        kk = alfa26.index(key6c[ki % len(key6c)])
        pt_26 += alfa26[(cc - kk) % 26]
        ki += 1
print(f"P6c (mod 26): {pt_26}")

