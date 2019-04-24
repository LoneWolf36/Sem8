def gcd(a, b):  # calculates GCD of a and b
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

# multiplicative inverse of 'a'  
# under modulo 'm' 
def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def coprimes(a):  # calculates all possible co-prime numbers with a
    l = []
    for x in range(2, a):
        if gcd(a, x) == 1 and modinv(x, phi) != None:
            l.append(x)
    for x in l:
        if x == modinv(x, phi):
            l.remove(x)
    return l


def encrypt_block(m):  # encrypts a single block
    c = m ** e % n
    return c


def decrypt_block(c):  # decrypts a single block
    m = c ** d % n
    return m


def encrypt_string(plain_text):  # applies encryption
    return ''.join([chr(encrypt_block(ord(x))) for x in list(plain_text)])


def decrypt_string(s):  # applies decryption
    return ''.join([chr(decrypt_block(ord(x))) for x in list(s)])


if __name__ == "__main__":
    p = int(input('Enter prime p: '))

    for i in range(2, p):
        if(p%i == 0):
            print("p isnt prime:", p)
            exit(0)

    q = int(input('Enter prime q: '))
  
    for i in range(2, q):
        if(q%i == 0):
            print("q isnt prime:", q)
            exit(0)

    print("Choosen primes:\np=" + str(p) + ", q=" + str(q) + "\n")

    # Public key = (e,n)
    # Private key = (d,n)

    n = p * q
    print("n = p * q = " + str(n) + "\n")

    phi = (p - 1) * (q - 1)
    print("Euler's function (totient) [phi(n)]: " + str(phi) + "\n")

    print("Choose an e from a below coprimes array:\n")
    print(str(coprimes(phi)) + "\n")
    e = int(input())

    d = modinv(e, phi)  # calculates the decryption key d

    print("\nYour public key is a pair of numbers (e=" +
          str(e) + ", n=" + str(n) + ").\n")
    print("Your private key is a pair of numbers (d=" +
          str(d) + ", n=" + str(n) + ").\n")

    plain_text = input("Enter a message to encrypt: ")
    print("\nPlain message: " + plain_text + "\n")
    enc = encrypt_string(plain_text)
    print("Encrypted message: ", enc, "\n")
    dec = decrypt_string(enc)
    print("Decrypted message: " + dec + "\n")