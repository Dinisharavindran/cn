def hamming(data):
    data = list(data[::-1])
    r = 0
    while (2**r) < (len(data) + r + 1):
        r += 1
    j = 0
    k = 0
    code = ''
    for i in range(1, len(data) + r + 1):
        if i == 2**j:
            code += '0'; j += 1
        else:
            code += data[k]; k += 1
    code = list(code[::-1])
    for i in range(r):
        x = 0
        for j in range(1, len(code) + 1):
            if j & (2**i) == (2**i):
                x ^= int(code[-j])
        code[-(2**i)] = str(x)
    return ''.join(code)

def check(code):
    n = len(code); r = 0
    while (2**r) < n: r += 1
    err = 0
    for i in range(r):
        x = 0
        for j in range(1, n + 1):
            if j & (2**i) == (2**i):
                x ^= int(code[-j])
        err += x * (2**i)
    return err

d = input("Data bits: ")
c = hamming(d)
print("Hamming code:", c)
p = int(input("Error position (0 for none): "))
if p:
    c = list(c); c[-p] = '1' if c[-p] == '0' else '0'; c = ''.join(c)
    print("Erroneous code:", c)
e = check(c)
if e == 0: print("No error.")
else:
    print("Error at position:", e)
    c = list(c); c[-e] = '1' if c[-e] == '0' else '0'
    print("Corrected code:", ''.join(c))
