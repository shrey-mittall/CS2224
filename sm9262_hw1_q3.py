#Part A
def sumSquares(n):
    sum = 0;
    for i in range(1,n):
        sum += i**2;
    return sum;

#Part B
sum([i**2 for i in range(1,n)]);

#Part C
def sumOddSquares(n):
    sum = 0;
    for i in range(1,n,2):
        sum += i**2;
    return sum;

#Part D
sum([i**2 for i in range(1,n,2)]);

