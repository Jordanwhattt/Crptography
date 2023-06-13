[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10886544&assignment_repo_type=AssignmentRepo)
# discrete-log
See problem set for detailed instructions!

You will implement two algorithms for solving the discrete
logarithm problem in Fp* for prime p. First, implement the
brute-force algorithm.

Then, implement indices_of_match, an algorithm which returns the indices of a
match in two lists. Your algorithm must run in time O(nlogn),
where n is the maximum length of the two lists. There are
three approaches (at least). Given a list L, it may help to
make a new list L' = [[L[i],i] for i in range(len(L))] This list
keeps track of the elements of L, along with their original position (index).

Finally, using your implementation of indices_of_match, implement Shanks' babysteps-giantsteps algorithm. When all
tests pass, I suggest you figure out how long it would take
your naive algorithm (dlog) to solve the discrete logarithm problem in the third test!
