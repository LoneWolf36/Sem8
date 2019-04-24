key = "0010 0100 0111 0101"  # 16 bit
pt = '1001 0100 0010 0111'  # 16 bit
rc1 = '80'
rc2 = '30'

S = [['9', '4', 'A', 'B'],
     ['D', '1', '8', '5'],
     ['6', '2', '0', '3'],
     ['C', 'E', 'F', '7']]

Si = [['A', '5', '9', 'B'],
      ['1', '7', '8', 'F'],
      ['6', '0', '2', '3'],
      ['C', '4', 'D', 'E']]


def xor(h1, h2):
    return hex(int(h1, 16) ^ int(h2, 16))[2:]


def subNibble(nib, box):
    bits = bin(int(nib, 16))[2:].zfill(4)
    row = int(bits[0]+bits[1], 2)
    col = int(bits[2]+bits[3], 2)
    return box[row][col]


def genT(oddw, rc):
    t0 = subNibble(oddw[0], S)
    t1 = subNibble(oddw[1], S)
    t2 = t1+t0
    return xor(t2, rc)


def keygen(key):
    sk = []
    w = [0]*6

    k = hex(int(key.replace(' ', ''), 2))[2:]
    # print(k)
    w[0] = k[:2]
    w[1] = k[2:]
    sk.append(w[0]+w[1])

    t2 = genT(w[1], rc1)
    # print t2

    w[2] = xor(t2, w[0])
    w[3] = xor(w[2], w[1])
    sk.append(w[2]+w[3])

    t4 = genT(w[3], rc2)
    w[4] = xor(t4, w[2])
    w[5] = xor(w[4], w[3])
    sk.append(w[4]+w[5])
    return sk


def rot(state):
    return state[0]+state[3]+state[2]+state[1]


def sub(state, S):
    r = ''
    for s in state:
        r += subNibble(s, S)
    return r


#	1	4
#	4	1

def mult(num, h):
    h = int(h, 16)
    val = num * h

    if(num != 9):
        if val >= 64:
            val ^= 76
        if val >= 32:
            val ^= 38
        if val >= 16:
            val ^= 19

    else:
        val = 8 * h
        if val >= 64:
            val ^= 76
        if val >= 32:
            val ^= 38
        if val >= 16:
            val ^= 19
        val ^= h

    #print (h,"*",num,"=",hex(val))
    return hex(val)[2:]


def mix(state):
    s00 = xor(mult(1, state[0]), mult(4, state[1]))
    s10 = xor(mult(4, state[0]), mult(1, state[1]))
    s01 = xor(mult(1, state[2]), mult(4, state[3]))
    s11 = xor(mult(4, state[2]), mult(1, state[3]))
    return s00+s10+s01+s11


def mix_inv(state):
    s00 = xor(mult(9, state[0]), mult(2, state[1]))
    s10 = xor(mult(2, state[0]), mult(9, state[1]))
    s01 = xor(mult(9, state[2]), mult(2, state[3]))
    s11 = xor(mult(2, state[2]), mult(9, state[3]))
    return s00+s10+s01+s11


def encrypt(pt, k):

    pt = hex(int(pt.replace(' ', ''), 2))[2:]
    print("Plain", pt)
    # PreGame
    temp = xor(pt, k[0])
    print("Pre", temp)

    # R1
    temp = rot(temp)
    print("Rot", temp)
    temp = sub(temp, S)
    print("Sub", temp)
    temp = mix(temp)
    print("Mix", temp)
    temp = xor(temp, k[1])

    # R2
    temp = rot(temp)
    print("Rot", temp)
    temp = sub(temp, S)
    print("Sub", temp)
    temp = xor(temp, k[2])
    print("cipher", temp)
    return temp


def decrypt(cipher, k):
    print("\n\n\nCipher", cipher)
    # R2 i
    temp = xor(cipher, k[2])
    temp = sub(temp, Si)
    temp = rot(temp)

    print("R2 i", temp)

    # R1 i
    temp = xor(temp, k[1])

    temp = mix_inv(temp)
    temp = sub(temp, Si)
    #print ("R1 i",temp)
    temp = rot(temp)
    print("R1 i", temp)

    # pre
    temp = xor(temp, k[0])
    print("Plain", temp)

    return temp


def main():
    subk = keygen(key)
    print(subk)
    cipher = encrypt(pt, subk)
    #print (cipher)
    plain = decrypt(cipher, subk)


if __name__ == '__main__':
    main()
"""
Lets assume the inputs for the encryption are:•16-bit Plaintext,
 P: 1101 0111 0010 1000•16-bit
 Key, K: 0100 1010 1111 0101
 
 1.1
 Key GenerationThe first step is to generate the sub-keys. This is called Key Generation or Key Expansion:The input key, K, is split into 2 words, w0 and w1
 w0 = 0100 1010
 w1 = 1111 0101
 
 The first sub-key, Key0, is in fact just the input key: Key0 = w0w1 = K
 The other sub-keys are generated as follows:
 w2= w0 XOR 10000000 XOR SubNib(RotNib(w1))
 (Note: RotNib() is “rotate the nibbles”, which is equivalent to swapping the nibbles)= 0100 1010 XOR 10000000 XOR SubNib(0101 1111)
 
 (Note: SubNib() is “apply S-Box substitution on nibbles using encryption S-Box”)= 1100 1010 XOR SubNib(0101 1111)= 1100 1010 XOR 0001 0111= 1101 1101
 
 w3= w2 XOR w1= 1101 1101 XOR 1111 0101= 0010 1000
 
 w4= w2 XOR 0011 0000 XOR SubNib(RotNib(w3))= 1101 1101 XOR 0011 0000 XOR SubNib(1000 0010)= 1110 1101 XOR 0110 1010= 1000 0111

 w5= w4 XOR w3= 1000 0111 XOR 0010 1000= 1010 1111

Now the sub-keys are:
Key0= w0w1= 0100 1010 1111 0101
Key1= w2w3= 1101 1101 0010 1000
Key2= w4w5= 1000 0111 1010 1111

1.2 Encryption
Now let’s  do the encryption. There is an initial operation  (Add Round Key), followed by the main Round, followed by the final Round. (Note, the main difference in the real DES is that the main Round is repeated many times). Remember, the output of each operation is sed as the input to the next operation, always operating on 16-bits. The 16-bits can be viewed as a state matrix of nibbles.

1.2.1 Add Round 0 Key
Plaintext XOR Key1= 1101 0111 0010 1000 XOR 0100 1010 1111 0101=1001 1101 1101 1101

1.2.2 Round 1 Nibble Substitution (S-boxes).
Each nibble in the input is used in the Encryption S-Box togenerate an output nibble.
Input = 1001 1101 1101 1101
Output =0010 1110 1110 1110

Shift Row. 
Swap 2nd nibble and 4th nibble (note, in this example, its not so easy to see 
since 2nd and 4th nibbles are the same!)=0010 1110 1110 1110

Mix Columns. Apply the matrix multiplication with the constant matrix,  Me, using GF(24). For GF(24), the addition operation is simply an XOR, and for the multiplication operation you can usea lookup table. Me=1441S= 0010 1110=S00’S01’11101110S10’S11’

S’=Me x S
S00’=0010 XOR (4 x 1110)=0010 XOR (4 x E)=0010 XOR D=0010 XOR 1101=1111
S10’=(4 x 0010) XOR 1110=1000 XOR 1110=0110
S01’=1110 XOR (4 x 1110)=1110 XOR (4 x E)=1110 XOR 1101=0011
S11’=(4 x 1110) XOR 1110=1101 XOR 1110=0011
Output = S00’ S10’ S01’ S11’=1111 0110 0011 0011

Add Round 1 Key.=1111 0110 0011 0011 XOR1101 1101 0010 1000=0010 1011 0001 1011
1.2.3 Final RoundNibble Substitution (S-boxes)=1010 0011 0100 0011
Shift Row (2nd and 4th)=1010 0011 0100 0011
Add Round 2 Key
1010 0011 0100 0011 XOR 1000 0111 1010 1111=0010 0100 1110 1100
Now we have the final ciphertext.
Ciphertext = 0010 0100 1110 1100

1.3Decryption
Now lets decrypt. Note that we use the same keys generated during the encryption (that is, thedecryptor would generate the round sub-keys using the input key K, using the encryption S-Box). 
Add Round 2 Key
0010 0100 1110 1100 XOR1000 0111 1010 1111=1010 0011 0100 0011
Inverse Shift Row (same as normal)=1010 0011 0100 0011
Inverse Nibble Sub (use the inverse or decryption S-box)=0010 1011 0001 1011

Add Round 1 Key=0010 1011 0001 1011 XOR1101 1101 0010 1000=1111 0110 0011 0011

Inverse Mix Columns
S=S00S01S10S11=1111 00110110 0011S’=S00’S01’S10’

S11’=9 x S00 XOR 2 x S109 x S01 XOR 2 x S112 x S00 XOR 9 x S102 x S01 XOR 9 x S11
S00’=(9 x 1111) XOR (2 x 0110)=9 x F XOR 2 x 6=E XOR C=1110 XOR 1100=0010
S10’=2 x 1111 XOR 9 x 0110=2 x F XOR 9 x 6= D XOR 3=1101 XOR 0011=1110
S01’=9 x 0011 XOR 2 x 0011=9 x 3 XOR 2 x 3=8 XOR 6=1000 XOR 0110=1110
S11’=2 x 0011 XOR 9 x 0011=1110
Output=0010 1110 1110 1110
Inverse Shift Row=0010 1110 1110 1110
Inverse Nibble Sub=1001 1101 1101 1101

Add Round 0 
Key=1001 1101 1101 1101 XOR0100 1010 1111 0101=1101 0111 0010 1000
Plaintext = 1101 0111 0010 1000
Original = 1101 0111 0010 1000

The decryption worked!
"""
