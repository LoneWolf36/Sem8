plain = '10010111'  # 8
key = '1001011101'  # 10

# Defining tuples
P10table = (3, 5, 2, 7, 4, 10, 1, 9, 8, 6)
P8table = (6, 3, 7, 4, 8, 5, 10, 9)
P4table = (2, 4, 3, 1)
InputPerm = (2, 6, 3, 1, 4, 8, 5, 7)  # Data encryption Initial permutation
FinalPerm = (4, 1, 3, 5, 7, 2, 8, 6)  # Data encryption Final permutation
EPtable = (4, 1, 2, 3, 2, 3, 4, 1)  # Expand and permute

S0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]
S1 = [
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
]


def permute(PX, bits):
    r = ''
    for p in PX:
        r += bits[p-1]
    return r


def rotL(bits, c):
    return bits[c:]+bits[:c]


def keygen(key):
    """
    1. Take key and permute according to P10 table
    2. Then split into 2 parts and rotate each part left by 1
    3. Then join them and permute accoring to P8 table
    4. Then split into 2 parts and rotate each part left by 2
    """
    sk = []
    # Apply P10 table
    temp = permute(P10table, key)
    l, r = temp[:5], temp[5:]

    # Rotate left by 1
    l1, r1 = rotL(l, 1), rotL(r, 1)

    # Apply P8 table
    sk.append(permute(P8table, l1+r1))

    # Rotate left by 2
    l2, r2 = rotL(l, 2), rotL(r, 2)
    sk.append(permute(P8table, l2+r2))

    return sk


def s_table(b, table):
    # Convert 1st and 4th values to binary for row position
    row = int(b[0]+b[3], 2)
    # Convert 2nd and 3r values to binary for column position
    col = int(b[1]+b[2], 2)
    return bin(table[row][col])[2:].zfill(4)


def F(r, k):
    e = permute(EPtable, r)
    l = s_table(e[:4], S0)
    r = s_table(e[4:], S1)
    mask = bin(int(l+r, 2) ^ int(k, 2))[2:].zfill(8)

    return permute(P4table, mask)


def f(l, r, k):
    mask = F(r, k)
    l = bin(int(l, 2) ^ int(mask, 2))[2:].zfill(4)
    r = r

    return l, r


def encrypt(pt, k):
    print("Plain:", pt, int(pt, 2))
    temp = permute(InputPerm, pt)
    l, r = temp[:4], temp[4:]
    # Printing binary
    print('Checking binary equivalent:', int(temp, 2))
    # r1
    l, r = f(l, r, k[0])
    print('Checking binary equivalent:', int(r+l, 2))
    # r2
    l, r = f(r, l, k[1])
    print('Checking binary equivalent:', int(l+r, 2))
    temp = permute(FinalPerm, l+r)
    print("Cipher:", temp, int(temp, 2))
    return temp


def decrypt(cipher, k):
    print('\n\n\nCipher', cipher, int(cipher, 2))
    temp = permute(InputPerm, cipher)
    print('Checking binary equivalent:', int(temp, 2))
    l, r = temp[:4], temp[4:]
    # r1
    l, r = f(l, r, k[1])
    print('Checking binary equivalent:', int(r+l, 2))
    # r2
    l, r = f(r, l, k[0])
    print('Checking binary equivalent:', int(l+r, 2))
    temp = permute(FinalPerm, l+r)
    print("Plain:", temp, int(temp, 2))
    return temp


def main():
    sk = keygen(key)
    print("The generated keys are:", sk)
    cip = encrypt(plain, sk)
    pl = decrypt(cip, sk)


if __name__ == '__main__':
    main()

"""
Key Differences Between DES and AES

    The basic difference between DES and AES is that the block in DES is divided into two halves before further processing whereas, in AES entire block is processed to obtain ciphertext.
    The DES algorithm works on the Feistel Cipher principle, and the AES algorithm works on substitution and permutation principle.
    The key size of DES is 56 bit which is comparatively smaller than AES which has 128,192, or 256-bit secret key.
    The rounds in DES include Expansion Permutation, Xor, S-box, P-box, Xor and Swap. On the other hands, rounds in AES include Subbytes, Shiftrows, Mix columns, Addroundkeys.
    DES is less secure than AES because of the small key size.
    AES is comparatively faster than DES.

"""