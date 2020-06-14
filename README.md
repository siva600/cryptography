# cryptography
math and programming in Cryptography 
```text
Cryptography is one of fascinating subject in computer science. It is the study of making and braking codes.
We could always find a hidden message underneath the data we receive. The data could be a picture, alpha numeric 
characters, symbols, morse code, sounds, or any form of communication medium. 
We use a series of well defined steps called cipher which is an algorithm or the key to encrypt and decrypt.


Do you know the first cipher machine was developed in 1920's. Well we might heard of enigma used by allies to broadcast 
encrypted messages. For a single encoded message there were assumed total of approx 159 million million million chances 
and only one of them is correct. Later these were decoded in 1940's by mainly two great mathematicians of Gordan Welchman 
(his work led to development of Internet and Cloud) and Alan Turing (father of modern computer science and AI).
 

As a software engineer we might have come across various industry standard encryption algorithms used to protect our data.
Such as DES, RSA, Blowfish, AES, Twofish, SHA1, IDEA, MD5.... 

This repo will walk through detail working of below crypto systems. Start with Math -> Algorithm -> Encoding -> Decoding.
Below shows Encryption Schemas in Increasing order of cracking.

Facts: With a normal computer you carry it would take 300 trillion years to break the RSA-2048 bit encryption key. But using 
a quantum computer it would take 8 hours.

So you might be aware of ssl layer: (SSH/TLS)
Diffie-Hellman is an algorithm used to create a secure session key that allows to parties to exchange keys and have a 
one to one connection.

A type of ECC called ECDSA (Elliptic Curve Digital Signature Algorithm) is commonly used for identifying parties in SSH.
ECDSA is super popular: it protects how you know you're talking to Twitter under "https", protects bitcoin wallet sigs, etc.
Elliptic Curve Cryptography is the most efficient algorithm. Most crypto currencies Bitcoin and ethereum uses secp256k1 
elliptic curve.
To crack one of the these is not possible even with a super computer.

Reference:

https://www.technologyreview.com/2019/05/30/65724/how-a-quantum-computer-could-break-2048-bit-rsa-encryption-in-8-hours/

Pre-requisites: Number Theory algorithms, Algebra, Probability, basic calculus. 
Programming: Python for Implementing the algorithms, testing encoding and decoding messages. 
Though some problems could not be solved using programming, I personally recommend using https://sagecell.sagemath.org/ 
which is a mathematical software system also supporting python.


Generally, we assume that the message that we wish to send has been converted to
an integer in the set Jm = {0, 1, 2, 3, . . . , m − 1}, where m is some integer (positive)
to be determined. 

For Encipher  
        E : Jm -→ Jm  
            x −→ E(x)  

For Decipher 
        D : Jm −→ Jm  
      such that  D (E(x)) = x 
```

Categories: <br/>
1. Symmetric Encryption <br/>
    a. Caesar Encryption. Explanation: [caesar_encryption_theory](caesar_encryption_theory.md) <br/>
    b. Exponential Encryption ( Deffie - Hellman Encryption) <br/>
2. Asymmetric Encryption <br/>
    a. RSA Encryption & RSA Digital Signature <br/>
    b. Elgamal Encryption <br/>
    c. Elliptic Curve cryptography <br/>


   ![](images/io.png)   

```text

Encryption Algorithms:

1. Encoding a Phrase in a Number:
   Suppose s is a sequence of capital letters and spaces, and that s does not begin with a space. We encode s as a 
   number in base 27 as follows:
   a single space corresponds to 0 , the letter A to 1, B to 2, ..... z to 26.
   Thus 'Hi XORLD' becomes a number written in base 27:
```
e.g;
   "HI XORLD" - 27<sup>7</sup>.8 + 27<sup>6</sup>.9 + 27<sup>5</sup>.0 + 27<sup>4</sup>.23 + 27<sup>3</sup>.15 + 
                27<sup>2</sup>.18 + 27<sup>1</sup>.12 + 27<sup>0</sup>.4  = 87182673304. <br/>

```text   
   To recover the letters from the deciaml number, repeatedly divide the 27 and read off the letter corresponding to each 
   remainder.
   87182673304  = 27 * 3228987900 + 4
   3228987900 =  27 * 119592144 + 12 
   119592144 = 27 * 4429338 + 18     
   4429338 = 27 * 164049 + 15        
   164049 = 27 * 6075 + 24           
   6075 = 27 * 225 + 0               
   225 = 27 * 8 + 9                  
   8 = 27 * 0 + 8                    
   
```   
   Here the pattern is ( from top to bottom ) 4, 12, 18, 15, 24, 0, 9, 8 == "HI XORLD". 
   The base can be 256, 128.. and alpha numeric can be mapped with ASCII like 'a' -> 97...
   Code: [basic_encryption](basic_encryption.py) 
