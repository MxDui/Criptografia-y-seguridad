from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64


def descifrar_des_ecb(cifrado_b64, clave_str):
    clave = clave_str.encode('utf-8')
    cipher = DES.new(clave, DES.MODE_ECB)
    cifrado = base64.b64decode(cifrado_b64)
    descifrado = unpad(cipher.decrypt(cifrado), DES.block_size)
    return descifrado.decode('utf-8')


def generar_matriz_playfair(clave):
    clave = clave.upper().replace("J", "I")
    vista = []
    for c in clave:
        if c not in vista and c.isalpha():
            vista.append(c)
    for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c not in vista:
            vista.append(c)
    return [vista[i:i+5] for i in range(0, 25, 5)]


def encontrar_posicion(matriz, letra):
    for i, fila in enumerate(matriz):
        for j, c in enumerate(fila):
            if c == letra:
                return i, j
    return None


def descifrar_playfair(texto, matriz):
    texto = texto.upper().replace("J", "I")
    pares = [texto[i:i+2] for i in range(0, len(texto), 2)]
    resultado = []
    for par in pares:
        r1, c1 = encontrar_posicion(matriz, par[0])
        r2, c2 = encontrar_posicion(matriz, par[1])
        if r1 == r2:
            resultado.append(matriz[r1][(c1 - 1) % 5])
            resultado.append(matriz[r2][(c2 - 1) % 5])
        elif c1 == c2:
            resultado.append(matriz[(r1 - 1) % 5][c1])
            resultado.append(matriz[(r2 - 1) % 5][c2])
        else:
            resultado.append(matriz[r1][c2])
            resultado.append(matriz[r2][c1])
    return ''.join(resultado)


# lista de palabras candidatas para clave DES
with open("words.txt", "r") as f:
    palabras = [line.strip() for line in f if len(line.strip()) == 8]

cifrado_b64 = "h+F7XMoHpF0="

clave_correcta = None
for palabra in palabras:
    try:
        resultado = descifrar_des_ecb(cifrado_b64, palabra)
        print(f"Clave: {palabra} -> {resultado}")
        clave_correcta = palabra
        break
    except Exception:
        continue

if clave_correcta:
    print(f"\nClave DES encontrada: {clave_correcta}")

# PlayFair
texto_cifrado = (
    "SHPETXSQZNSPLBMBWFFKCEBRBQMVQSEGOLRBLGXPPSUXHWLGXPDL"
    "SZSNAZINELFTEQRGTSRIFWKBRGZVNPWKBQPGPBMZOMGEQMXPHGUF"
    "DIKBSCMGQMSHVZXTQMFXFOGPSHBWIOSNOQNPWKKCOQMFAVSHS M"
    "FOSNDKHGMVSZSHQPIYSQAVPNEGCERZQBQOKSSCOFOHPYQSBKQOZSHP"
    "FKEGKCRLSNQOIKOQOWPSTDPSBRAVGMVZQZKGFRZVVPZVSHPG"
    "VAOHRBGEZVEQHGWMKSNSZSRZPHZVPSZSIRDLSNAZINDLOBFWSKGPZS"
    "MZQZOWMCAVSHGRMPXGNSPGFPKFHBMGSQSGPEKGQSFSSNOW"
    "BLPYSQKBSQBRQSEFSGKSKSUXHWLGXPZSZSNSZKRGFZQPOQDYSXTFRZQ"
    "MPQRGXECNZPCEGLBQNQPCMESNOWBLPYSCGSOHQPFSRIFWKBQB"
    "DTQOQNDOZVMIZPUFDIKBSCNGRYCYBLQGBQOQZAMRZPBRPESNGRQEPE"
    "SNVPVZBKZVVPPSKSSPQBKGBKQOBKWHKDZVYMMGMQZLKEIOEQGLBR"
    "WHUXFOSPZSGPGFQOGKAV"
).replace("-", "").replace(" ", "").replace("\n", "")

# Clave deducida: PEGASUZ
clave_playfair = "PEGASUZ"
matriz = generar_matriz_playfair(clave_playfair)

print("\nMatriz PlayFair:")
for fila in matriz:
    print(fila)

texto_plano = descifrar_playfair(texto_cifrado, matriz)
print(f"\nTexto descifrado:\n{texto_plano}")
