# Below code is executed in https://sagecell.sagemath.org/ to test elliptic curve and to see the graph.
E=EllipticCurve([-5,4])
E;
P=E.plot(thickness=4, rgbcolor=(0.1,0.7,0.1))
P.show(figsize=[4,5])


E=EllipticCurve([-5,4])
P=E([1.,0])
Q=E([0,2.])
R = Q + Q
S = 2*Q
print(R)
print(S)
5*Q