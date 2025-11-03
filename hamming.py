def calc_redundant_bits(m):
    r = 0
    while (2 ** r) < (m + r + 1):
        r += 1
    return r

def pos_redundant_bits(data, r):
    j = 0
    k = 1
    m = len(data)
    res = ''
    for i in range(1, m + r + 1):
        if i == 2 ** j:
            res = res + '0'
            j += 1
        else:
            res = res + data[-1 * k]
            k += 1
    return res[::-1]

def calc_parity_bits(arr, r):
    n = len(arr)
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if j & (2 ** i) == (2 ** i):
                val ^= int(arr[-1 * j])
        arr = arr[:n - (2 ** i)] + str(val) + arr[n - (2 ** i) + 1:]
    return arr

def detect_error(arr, r):
    n = len(arr)
    res = 0
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if j & (2 ** i) == (2 ** i):
                val ^= int(arr[-1 * j])
        res = res + val * (10 ** i)
    return int(str(res), 2)

data = input("Enter the data bits: ")

r = calc_redundant_bits(len(data))
arr = pos_redundant_bits(data, r)
arr = calc_parity_bits(arr, r)

print("\nData transferred is:", arr)

error_data = input("Enter the received data: ")
print("Error Data is:", error_data)

correction = detect_error(error_data, r)

if correction == 0:
    print("There is no error in the received message.")
else:
    print(f"Error detected at bit position: {correction}")
    error_data = list(error_data)
    pos = len(error_data) - correction
    error_data[pos] = '0' if error_data[pos] == '1' else '1'
    corrected = ''.join(error_data)
    print("Corrected Data is:", corrected)
