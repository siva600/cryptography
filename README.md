# cryptography
math and programming in Cryptography 

Cryptography is one of fascinating subject in computer science. We could always find a hidden message underneath the 
data we receive. The data could be a picture, alpha numeric characters, symbols, morse code, sounds, or any form of 
communication medium. We use a series of well defined steps called cipher which is an algorithm to encrypt and decrypt.
<br/>

Do you know the first cipher machine was developed in 1920's. Well we might heard of enigma used by allies to broadcast 
encrypted messages. For a single encoded message there were assumed total of approx 160 million million chances and only 
one of them is correct. Later Alan Turing a great mathematician comes up with intelligent way of cracking the message 
during WorldWarII and saved millions of lives. <br/>

As a software engineer we might have come across various industry standard encryption algorithms used to protect our data.
Such as DES, RSA, Blowfish, AES, Twofish, SHA1, IDEA, MD5.... <br/>

This repo presents some of the ways and the math behind well known encryption standards. <br/>
Pre-requisites: Number Theory algorithms, Algebra, Probability, basic calculus. <br/>
Programming: Python is used for designing the algorithms, encoding and decoding messages. <br/>


Generally, we assume that the message that we wish to send has been converted to
an integer in the set Jm = {0, 1, 2, 3, . . . , m − 1}, where m is some integer (positive)
to be determined. <br/>

For Encipher  <br/>
        E : Jm −→ Jm  <br/>
            x −→ E(x)  <br/>

For Decipher <br/>
        D : Jm −→ Jm  <br/>
      such that  D (E(x)) = x <br/>
   
   ![](images/io.png)   <br/>
    
The Basic ways of Encryption: <br/>
1. Encoding a Phrase in a Number: <br/>
   Suppose s is a sequence of capital letters and spaces, and that s does not begin with a space. We encode s as a 
   number in base 27 as follows: <br/>
   a single space corresponds to 0 , the letter A to 1, B to 2, ..... z to 26. <br/>
   Thus 'RUN NIKITA' becomes a number written in base 27: <br/>

   "HI XORLD" - 27<sup>7</sup>.8 + 27<sup>6</sup>.9 + 27<sup>5</sup>.0 + 27<sup>4</sup>.23 + 27<sup>3</sup>.15 + 
                27<sup>2</sup>.18 + 27<sup>1</sup>.12 + 27<sup>0</sup>.4  = 87182673304. <br/>
   
   To recover the letters from the deciaml number, repeatedly divide the 27 and read off the letter corresponding to each 
   remainder. <br/>
   87182673304  = 27 * 3228987900 + 4 <br/>
   3228987900 =  27 * 119592144 + 12  <br/>
   119592144 = 27 * 4429338 + 18      <br/>
   4429338 = 27 * 164049 + 15         <br/>
   164049 = 27 * 6075 + 24            <br/>
   6075 = 27 * 225 + 0                <br/>
   225 = 27 * 8 + 9                   <br/>
   8 = 27 * 0 + 8                     <br/>
   
   
   Here the pattern is ( from top to bottom ) 4, 12, 18, 15, 24, 0, 9, 8 == "HI XORLD". <br/>
   The base can be 256, 128.. and alpha numeric can be mapped with ASCII like 'a' -> 97...<br/><br/>
   
   
   
   
   
 
    

