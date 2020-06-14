# Execute the code in https://sagecell.sagemath.org/

def encode(s):
    s = str(s)
    return sum(ord(s[i]) * 256 ^ i for i in range(len(s)))


def decode(n):
    n = Integer(n)
    v = []
    while n != 0:
        v.append(chr(n % 256))
        n //= 256  # this replace n by floor (n/256)
    return ''.join(v)


s = 'how are you?'
n = encode(s)
print(n)

r = decode(n)
print(r)

# Output
# 19639526356709680135919857512
# how are you?
