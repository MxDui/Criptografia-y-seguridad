from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
import base64

def cifrar_des_ecb(mensaje_str, clave_str):
    # La clave para DES debe de ser exactamente de 8 bytes
    clave = clave_str.encode('utf-8')
    cipher = DES.new(clave, DES.MODE_ECB)

    # Aplicar padding PKCS7 para que el bloque sea multiplo de 8
    mensaje_padded = pad(mensaje_str.encode('utf-8'), DES.block_size)
    cifrado = cipher.encrypt(mensaje_padded)

    return base64.b64encode(cifrado).decode('utf-8')

m = "mensaje"
k = "data7Qa="
print(cifrar_des_ecb(m, k))
