# CycleDetection
Assignments | University of Piraeus 2022

Using the Robert W. Floyd method, we begin to go through the sequence using two
indexes. The first index moves one step at a time but the second one two steps at a
time. We detect a cycle when the first and the second index are in the same position.
This method requires a lot of space so we are going to use an alternative.
Instead of examining all the values of the sequence, we only examine b values.
These b values are between g and b (gb distance), where g and b are parameters.
We store these values in an array, named table. Table contains pairs (y, j), where y is
a value of the sequence and j is the position of the value. For every y, table may
include more than one j.

Reference: Sedgewick, Robert, Thomas G. Szymanski, and Andrew C. Yao. 1982. “The Complexity of Finding Cycles in Periodic Functions.” SIAM Journal on Computing 11 (2): 376–390. https://doi.org/10.1137/0211030.
