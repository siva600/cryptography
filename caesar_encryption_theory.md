```text
The simplest encryption : Caesar encryption
Caesar encryption is a type of shift cryptosystem, is a symmetric-
    key cryptosystem in which each secret key k is an element of Z/nZ, it is clear that the key space Z/nZ consists of n 
    possible keys.
    Let P = (p0, p1, p2, ..., pm−1) be a non-empty plaintext consisting of m elements, 
    
    Steps:
        a) Convert the elements of the plaintext into numbers P (including any notations : ' ' (blank), #, !, ?, ..., )
        b) Use the secret key k to produce a ciphertext C:
            C = P + k (mod n) ( n may be chosen as the base, the number of alphabets or, 
                                if using the ASCII table : n = 256).
                                The ciphertext is C, may convert to alphabets before sending.
        c) Decryption Key
            P = C + k (mod n)
            and convert to the alphabets to get the original plaintext.
        
```

