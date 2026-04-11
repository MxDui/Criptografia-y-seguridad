alfabeto = "abcdefghijklmnñopqrstuvwxyz"

def vigenere_enc(pt, key):
    ct = ""
    pt_clean = pt.replace(" ", "").replace("ó", "o")
    key_idx = 0
    for c in pt_clean:
        if c in alfabeto:
            p = alfabeto.index(c)
            k = alfabeto.index(key[key_idx % len(key)])
            ct += alfabeto[(p + k) % 27]
            key_idx += 1
        else:
            ct += c
    return ct

def vigenere_dec(ct, key):
    pt = ""
    ct_clean = ct.replace(" ", "")
    key_idx = 0
    for c in ct_clean:
        if c in alfabeto:
            cc = alfabeto.index(c)
            kk = alfabeto.index(key[key_idx % len(key)])
            pt += alfabeto[(cc - kk) % 27]
            key_idx += 1
        else:
            pt += c
    return pt

print("=== P6 a ===")
pt1 = "pertenecio a una gran señor algo feudal y algo bruto"
print("Cifrado:", vigenere_enc(pt1, "poema"))

print("\n=== P6 b ===")
ct2 = "isowabofmsxhinujdceuthtaspzianeg"
print("Descifrado:", vigenere_dec(ct2, "poema"))

def vigenere_dec_26(ct, key):
    alfabeto_26 = "abcdefghijklmnopqrstuvwxyz"
    pt = ""
    ct_clean = ct.replace(" ", "")
    key_idx = 0
    for c in ct_clean:
        if c in alfabeto_26:
            cc = alfabeto_26.index(c)
            kk = alfabeto_26.index(key[key_idx % len(key)])
            pt += alfabeto_26[(cc - kk) % 26]
            key_idx += 1
        else:
            pt += c
    return pt

print("\n=== P6 c ===")
ct3 = "tuumrtsmpbyefzapchlnarrtvhcyrfudvsllofkqqmky"
print("Desc 27:", vigenere_dec(ct3, "zhuangzi"))
print("Desc 26:", vigenere_dec_26(ct3, "zhuangzi"))
