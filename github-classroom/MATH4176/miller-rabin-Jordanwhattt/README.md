[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10316216&assignment_repo_type=AssignmentRepo)
# miller-rabin

In this programming assignment, you will implement the Miller-Rabin primality test.

First, you will write a function which, given a positive integer M, computes integers k and q such that M=2^kq where q is odd.

Next, you will implement the Miller-Rabin primality test. Note that you will need the first function in order to do this. Also, you'll need a way to quickly compute a^b mod c given integers a,b,c. Feel free to use the python primitive pow(a,b,c) for this (https://docs.python.org/3/library/functions.html#pow). Note 
that the input to miller_rabin is both an integer N and an
*optional* input a. This means you can call this function with
just N, or with both N and your own choice of a. I already
handle this issue for you, so you don't need to worry about it.
You can see how this works in the test file. One challenge:
implement Miller-Rabin so that if you input an even integer, it
correctly returns false (if you're not careful with your
implementation, it may not even halt on an even input!)
