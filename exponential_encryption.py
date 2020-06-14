# Execute the code in https://sagecell.sagemath.org/
# Encoding : encode divides the string s (plaintext)into blocks, each block includes 4 letters,
# and calls encode1 for encoding. Input for encode: String s (plaintext), encryption key:
# e, p are primes such that gcd(e,p-1) = 1. 
# Output: List L of Integers (ciphertext)


# Decoding: decode calls decode1 for decoding each block.
# Input of decode: List L of integers (ciphertext), decryption key: d, p primes
# where d in the inverse of e (mod p-1)
#
def encode1(s, e, p):
    s = str(s)  # making input a string
    r1 = sum(ord(s[i]) * 256 ^ i for i in range(len(s)))
    r2 = power_mod(r1, e, p)
    return r2


def decode1(m, d, p):
    n = power_mod(m, d, p)
    n = Integer(n)
    v = []
    while n != 0:
        v.append(chr(n % 256))
        n //= 256  # this replace n by floor (n/256)
        return ''.join(v)


def encode(s, e, p):
    s = str(s)  # making input a string
    L = []
    PL = []
    n = len(s) / 4 - 1
    for i in [0..n]:
        k = 4 * i
        PL.append(s[k:k + 4])
        if len(s) % 4 == 1:
            PL.append(s[len(s) - 1])
        if len(s) % 4 == 2:
            PL.append(s[len(s) - 2: len(s)])
        if len(s) % 4 == 3:
            PL.append(s[len(s) - 3: len(s)])

    for i in range(0, len(PL)):
        r = encode1(PL[i], e, p)
        L.append(r)
    return L


def decode(L, d, p):
    PL = []
    for i in range(0, len(L)):
        r = decode1(L[i], d, p)
        PL.append(r)
    return ''.join(PL)


# Take a sample prime and find the next prime
p = next_prime(76547984763986793869346936739673934990630345718237658237658723685428147581759874812745812745812745128)
e = next_prime(65347148876582689236582965286275457154715418754)

# The key of the encryption : (e,p) (Keep secret, at least keep e !)
d = inverse_mod(e, p - 1)

# The key of the decryption : (d,p) (Keep secret, at least keep d !)
s = 'someday will meet you'
c = encode(s, e, p)
print(c)

# Output : Encoded value

# [39606834209358969907628247898939974378087358616758329896487483869251111502244421763346497625361905122, 
# 67583726258296973697243533818983161432727552134366703099531799065916930593143904854660139611984585649, 
# 856485500832167687853863689435174948567753322160449666597735231853912969888946376517284202592184477, 
# 67583726258296973697243533818983161432727552134366703099531799065916930593143904854660139611984585649, 
# 11288105997759180424050101006000056752127749116731095869372200066615191387621158210792553525860204130, 
# 67583726258296973697243533818983161432727552134366703099531799065916930593143904854660139611984585649, 
# 55838248162017554709580538921815240987747355016325033840102571473600619589230680714967117859452522655, 
# 67583726258296973697243533818983161432727552134366703099531799065916930593143904854660139611984585649, 
# 75189979896438400142797326792946839770747404047241168115556681924039442068314646121060604748725483003, 
# 67583726258296973697243533818983161432727552134366703099531799065916930593143904854660139611984585649]


r = decode(c, d, p)
print(r)
