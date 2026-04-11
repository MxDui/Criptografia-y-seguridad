def caesar_decrypt(ciphertext, k):
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    plaintext = ""
    ciphertext = ciphertext.upper()
    for char in ciphertext:
        if char in alfabeto:
            idx = alfabeto.index(char)
            idx = (idx - k) % 27
            plaintext += alfabeto[idx]
        else:
            plaintext += char
    return plaintext

print("=== Problema 1: Cifrado César ===")

# a) Fuerza bruta
print("\n--- a) Fuerza bruta ---")
ct1 = "Nc xkfc gu dgnnc"
for k in range(27):
    print(f"K={k}: {caesar_decrypt(ct1, k)}")

# b) Última letra es O sin rotar
print("\n--- b) Última letra O ---")
ct2 = "Zo qgweidugotío sh jb hsqgsid"
# La última letra es 'D', sabemos descifrada es 'O' (sin rotar)
# Entonces D (index 3) viene de O (index 15) ? No. 
# "La última letra está relacionada con la O sin rotar"
# D en el alfabeto (A=0.. Z=26)
alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
d_idx = alfabeto.index("D")
o_idx = alfabeto.index("O")
k2 = (d_idx - o_idx) % 27
print(f"La K sería {k2}")
print(f"Mensaje: {caesar_decrypt(ct2, k2)}")

# c) Frecuencias
print("\n--- c) Frecuencias ---")
ct3 = "Jx qzd kfhnp mjwnw f ptx ijqfx xnr ifwxj hzjryf xtgwj ytit hzfrit jwjx ñtajr"
# Vamos a contar letras
ct3_upper = ct3.upper()
counts = {}
for c in ct3_upper:
    if c in alfabeto:
        counts[c] = counts.get(c, 0) + 1
print(f"Frecuencias: {counts}")
# La letra más frecuente suele ser la E
max_char = max(counts, key=counts.get)
print(f"Letra más frecuente: {max_char}")
e_idx = alfabeto.index("E")
max_idx = alfabeto.index(max_char)
k3 = (max_idx - e_idx) % 27
print(f"Posible K: {k3}")
print(f"Mensaje: {caesar_decrypt(ct3, k3)}")

print("\n=== Problema 2: Cuadrado de Polibio ===")
polybius_alphabet = "ABCDEFGHIKLMNOPQRSTUVWXY" # Para el Cuadrado de Polibio, descartamos la Ñ y Z. Consideramos I y J independientes.
# El alfabeto español normalmente tiene 27 letras (A-Z + Ñ).
# Si descartamos Ñ y Z, nos quedan exactamente 25 letras.
# En una matriz de 5x5 caben exactamente 25 letras. Perfecto.
polybius_grid = [
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'I', 'J'],
    ['K', 'L', 'M', 'N', 'O'],
    ['P', 'Q', 'R', 'S', 'T'],
    ['U', 'V', 'W', 'X', 'Y']
]
# Crear mapeo de coordenadas
enc_map = {}
dec_map = {}
for r in range(5):
    for c in range(5):
        char = polybius_grid[r][c]
        coord = str(r+1) + str(c+1)
        enc_map[char] = coord
        dec_map[coord] = char

p2_ciphertext = "15 32 45 24 15 33 41 35 34 35 15 44 41 15 43 11 11 34 11 14 24 15"
p2_plaintext = ""
for pair in p2_ciphertext.split():
    p2_plaintext += dec_map[pair]
print("a) Descifrado:")
print(p2_plaintext)

p2_todecrypt = "Si la felicidad tuviera una forma, tendría forma de cristal, porque puede estar a tu alrededor sin que la notes. Pero si cambias de perspectiva, puede reflejar una luz capaz de iluminarlo todo."
import unicodedata
def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

p2_clean = strip_accents(p2_todecrypt).upper()
p2_encrypted = ""
for char in p2_clean:
    if char == 'Z': char = 'S' # La 'Z' se descarta y se intercambia fonéticamente por la 'S' para las palabras "luz" y "capaz"
    if char in enc_map:
        p2_encrypted += enc_map[char] + " "
    else:
        p2_encrypted += char
print("b) Cifrado:")
print(p2_encrypted)


