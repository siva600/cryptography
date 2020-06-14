# Encoding, input: string s (plaintext), an integer k (shift number),
# output: string v (ciphertext)

def encode(s,k):
	s=str(s)
	n=sum(((ord(s[i])+ k) % 256)*256^i for i in range (len(s)))
	v=[]
	while n != 0 :
		v.append(chr(n % 256))
		n //=256
	return ''.join(v)

# Decoding, input: string s (ciphertext), an integer k (shift number: the key),
# output: string v (plaintext)
#

def decode(s,k):
	s=str(s)
	n=sum((ord(s[i]) % 256)*256^i for i in range (len(s)))
	v=[]
	while n != 0 :
		m= ((n % 256)+ 256-k) % 256
		v.append(chr(m))
		n //=256
	return ''.join(v)


s = "test"
v = encode(s, 7)
print(v)

r = decode(v, 7)
print(r)

# Output
# {lz{
# test

