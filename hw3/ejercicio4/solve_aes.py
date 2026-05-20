from pathlib import Path
import hashlib
import math
import re
import unicodedata

try:
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
except ImportError:
    AESGCM = None


def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def primeros_primos(cantidad):
    primos = []
    n = 2
    while len(primos) < cantidad:
        if es_primo(n):
            primos.append(n)
        n += 1
    return primos


def buscar_archivo(nombre):
    for path in [Path.cwd() / nombre, Path(__file__).parent / nombre, Path(__file__).parent.parent / nombre]:
        if path.exists():
            return path
    return Path.cwd() / nombre


texto = buscar_archivo("file.txt").read_text(encoding="utf-8")
normalizado = unicodedata.normalize("NFD", texto)
normalizado = "".join(c for c in normalizado if unicodedata.category(c) != "Mn")
letras = "".join(re.findall(r"[A-Za-z]", normalizado)).lower()

base = "kevinmitnick"
extraido = "".join(letras[(p - 2) % len(letras)] for p in primeros_primos(25))
clave = "".join(a + b for a, b in zip(extraido, (base * 10)[:25]))
sha256 = hashlib.sha256(clave.encode()).hexdigest()
hashes = set(buscar_archivo("hashes.txt").read_text().splitlines())

print("letras normalizadas:", len(letras))
print("texto extraido:", extraido)
print("clave:", clave)
print("sha256:", sha256)
print("hash encontrado en hashes.txt:", sha256 in hashes)

if AESGCM is None:
    print("cryptography no esta instalado; se omite prueba AES-GCM")
else:
    # Derivar los bytes de la clave AES usando el hash hexadecimal (doble hash)
    key_bytes = hashlib.sha256(sha256.encode()).digest()
    
    # Concatenar todas las lineas de cipher.txt
    cipher_lines = buscar_archivo("cipher.txt").read_text().splitlines()
    cipher_hex = "".join(line.strip() for line in cipher_lines)
    data = bytes.fromhex(cipher_hex)
    
    nonce, ciphertext = data[:12], data[12:]
    try:
        plaintext = AESGCM(key_bytes).decrypt(nonce, ciphertext, None)
        print("descifrado exitoso:", plaintext.decode())
    except Exception as exc:
        print(f"error al descifrar: {type(exc).__name__}: {exc}")
