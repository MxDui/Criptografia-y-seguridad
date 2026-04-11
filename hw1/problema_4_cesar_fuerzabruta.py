def caesar_decrypt(ciphertext, k):
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    plaintext = ""
    for char in ciphertext.lower():
        if char in alfabeto:
            idx = alfabeto.index(char)
            idx = (idx - k) % 27
            plaintext += alfabeto[idx]
        else:
            plaintext += char
    return plaintext

print("=== Problema 4 ===")
ct1 = "dqiqo"
print(f"Criptograma: {ct1}")
for k in range(27):
    print(f"k={k}: {caesar_decrypt(ct1, k)}")

ct2 = "btvtvshz"
print(f"\nCriptograma: {ct2}")
for k in range(27):
    print(f"k={k}: {caesar_decrypt(ct2, k)}")
