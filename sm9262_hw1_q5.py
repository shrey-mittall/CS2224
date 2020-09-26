def fibs(n):
   i, j = 1, 1; #sets up the first two numbers
   counter = 0; #counter for the generator

   while counter < n:
       yield i; #yields the current fib value
       counter += 1; # adds to the counter
       i, j = j, i + j; #swaps i for next value and j for i + j
