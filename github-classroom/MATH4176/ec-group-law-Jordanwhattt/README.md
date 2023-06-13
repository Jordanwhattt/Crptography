[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10768303&assignment_repo_type=AssignmentRepo)
# ec-group-law

In this assignment, you will implement the group law on an
elliptic curve y^2=x^3+Ax+B over the finite field Fp.

<ol>
  <li>You may assume throughout that p is prime.</li>
  <li>The inputs A,B are integers in [0,p-1].</li>
  <li>A nonzero point P on the curve is represented by a tuple (xP,yP)
  where xP,yP are integers in [0,p-1]</li>
  <li>The point at infinity is simply represented by None, so,
  for example, add(P,None,A,B,p) should return P; neg(None,p)
  should return None; add(P,neg(P,p),A,B,p) should return None, etc...</li>
  <li>Implement all operations in pure python. Use pow(x,-1,p) to compute
  the inverse of x modulo p. (Alternatively, you may include your
    own modular inversion algorithm)
</ol>
