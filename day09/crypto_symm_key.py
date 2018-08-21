def KSA(key):
    s = []
    # ord(char) change the char to the ascii code of the char
    key = [ord(k) for k in key]
    j = 0
    s = list(range(256))
    # for i in range(256):
    #     s.append( key[i % len(key)])

    for i in range(256):
        j = (j + s[i] + key[i%len(key)]) % 256
        s[i], s[j] = s[j], s[i]
    return s

def PRGA(key,s):
    i, j = 0, 0
    xorkey = []

    for k in range(256):
        i = (i+1) % 256
        j = (i+s[i]) % 256
        s[i], s[j] = s[j], s[i]
        tmp = (s[i] + s[j]) % 256
        xorkey.append(s[tmp])
    return xorkey

def xor(xorkey, target):
    ret = ''
    for i in range(len(target)):
        ret += chr(xorkey[i%256] ^ ord(target[i]))
    return ret

def rc4(text, key):
    s = KSA(key)
    xorkey = PRGA(key,s)
    return xor(xorkey, text)

key = 'hello'
text = 'This is plain text'
encrypt_msg = rc4(text, key)
print(encrypt_msg)
decrypt_msg = rc4(encrypt_msg, key)
print(decrypt_msg)
