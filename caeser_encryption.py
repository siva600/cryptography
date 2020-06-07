def encode(s, k):
    output = ''
    alphabets = ''.join(map(chr, range(65, 91)))
    for i in range(len(s)):
        print(s[i])
        loc = alphabets.find(s[i])
        new_loc = (loc + k) % 26
        output += alphabets[new_loc]
    return output


def decode(s, k):
    s = str(s)
    n = sum((ord(s[i]) % 256) * 256 ^ i for i in range(len(s)))
    v = []
    while n != 0:
        m = ((n % 256) + 256 - k) % 256
        v.append(chr(m))
        n //= 256
    return ''.join(v)


s = 'a'
v = encode(s, 7)  # shifting 7 positions in ASCII code.
print(v)
# r = decode(v, 3)
# print(r)
