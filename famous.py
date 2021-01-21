 
# this file includes the most famous problems:
#   Fizz Buzz Problem   LC-412
#   Fibonacci Sequence  LC-509
#   Tower of Hanoi      
#   
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Fizz Buzz Problem
    print Fizz if the number n is multiple of 3
    print Buzz if the number n is multiple of 5
    print FizzBuzz if the number n is multiple of 3*5
"""     
# solutions in one line for the number n from 1 to 100
# Fizz Buzz Solution 1
for n in range(1, 101): print("Fizz"*(n%3==0)+"Buzz"*(n%5==0) or n)

# Fizz Buzz Solution 2
print(list(map(lambda n: "Fizz"*(n%3==0)+"Buzz"*(n%5==0) or str(n), range(1,101))))

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Fibonacci Problem
    in Fibonacci Sequence, every number after first two numbers, 0 and 1,
    is the sum of the two preceeding numbers. 
        f(n) = f(n - 1) + f(n - 2)
"""
# Fibonacci Solution 1: uses two buffers
def fibonacci1(n):
    fibs = [0, 1]
    for i in range(n):
        fibs[i & 1] = fibs[(i - 1) & 1] + fibs[(i - 2) & 1]
    return fibs[(n - 1) & 1]

# Fibonacci Solution 2: use two variables
def fibonacci2(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return b

# Fibonacci testing code
#n = int(input('enter Fibonacci n-th: '))
for i in range(10):
    print(i, '-', fibonacci1(i))
    print(i, '-', fibonacci2(i))

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Tower of Hanoi
    there are 3 rods and n disks, move all disks on one rod to another rod.
    1) only one disk can be moved a one time
    2) each move consist of taking one disk on the top of one of stacks(rod)
       to placing on the top of another stack (rod).
    3) no disk can be placed on the top of a smaller disk.
"""
def tower_hanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print("move disk 1 from", from_rod, "to", to_rod)
        return
    tower_hanoi(n-1, from_rod, aux_rod, to_rod)
    print("move disk", n, "from", from_rod, "to", to_rod)
    tower_hanoi(n-1, aux_rod, to_rod, from_rod)

# tower of Hanoi testing code
n = int(input('enter number of disks: '))
tower_hanoi(n, 'A', 'B', 'C')
