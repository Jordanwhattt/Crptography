[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10031152&assignment_repo_type=AssignmentRepo)
# modular-inverse

In this programming assignment, you will implement the extended euclidean algorithm, along with an algorithm for computing a modular inverse and the square-and-multiply algorithm. 

First, 
implement the extended euclidean algorithm, as defined in Problem 5 of Homework 2. Your algorithm should return the tuple (g,s,t) on input a,b such that 
g=gcd(a,b)=as+bt. 

Then, implement the square-and-multiply algorithm, as defined in Problem 2 of Homework 2. Your algorithm should return g^x modulo m. To test your work: you can compute g^x modulo m using pow(a,x,m) in python (obviously you may NOT use pow() in your implementation -- implement it as described above). 

Finally, using your extended euclidean algorithm, implement an algorithm which accepts integers a,m as input (which you can assume to be coprime) and outputs 
an integer b such that ab=1 mod m. For some brownie points: think about how you would implement this so that it accepts *any* pair of integers a,m, and returns an inverse of a mod m if gcd(a,m)=1 and otherwise raises a value error. Even more brownie points: when gcd(a,m)=1, have your algorithm return an integer b in Z/mZ, i.e. 0<= b<m. 
