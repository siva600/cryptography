def encode(s):
    """
    :param s: string
    :return: encrypted integer value
    """
    return sum((256**i)*ord(s[i]) for i in range(len(s)))


def decode(n):
    """
    :param n: long int (decrypted)
    :return: original message
    """
    n = int(n)
    output = []
    while n != 0:
        output.append(chr(n % 256))
        n //= 256
    return ''.join(output)


value = encode("hi world")
print(value)
print(decode(value))
