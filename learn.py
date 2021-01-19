# Python Practice


""" Find K closet points
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        d1 = [x[0]*x[0] + x[1]*x[1] for x in points]
        print(d1)
#        d2 = list(map(lambda x: x[0]*x[0] + x[1]*x[1], points))    # same as d1
#        print(d2)
        d2 = sorted(d1)
#        print(d2, d2[K-1])
        rlist = [x for x in points if x[0]*x[0] + x[1]*x[1] <= d2[K-1]]
        return rlist[:K]
"""
    
""" intger frequency
class Solution(object):
    def intFrequent(self, nums):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        mdict = {}
        for x in nums:
            if x not in mdict.keys():
                mdict[x] = 1
            else:
                mdict[x] += 1
        return mdict
                
#        rlist = sorted(mdict.items(), key = lambda kv: (kv[1], kv[0]), reverse = True)
#        rkeys = [x[0] for x in rlist]
#        return rkeys[:k]

nums = [1,1,3,4,1,3]

sobj = Solution()
sint = sobj.intFrequent(nums)
print(sint)
"""

"""
nums = [2, 7, 11, 15]

class Solution(object):
    def twoSum(self, nums, target):
        s = list(map(lambda x, y: (x + y) == target , nums))
        return s

ss = Solution()
print(ss.twoSum(nums, 9))
"""

""" Tree
class Tree(object):
    def __init__(self):
        self.left = None
        self.rught = None
        self.data = None

root = Tree()
root.data = "root"
root.left = "left-0"
root.right = "right-0"
print(root.data)
"""

""" Bubble Sort using recursiion
alist = [12, 3, 54, 39, 59, 6, 24, 39, 22, 78, 99, 11]
print("original list:", alist)

def bubbleSort(alist):
    count = 0
    for i in range(len(alist) - 1):
        if alist[i] > alist[i + 1]:
            alist[i], alist[i + 1] = alist[i + 1], alist[i]
            count += 1
    if count == 0:
        return alist
    else:
        bubbleSort(alist)

bubbleSort(alist)
print("sorted list:", alist)
"""

""" Binary Search on sorted list

def binarySearch(alist, x):
    m = int(len(alist)/2)
    if m == 0:
        if alist[0] == x:
            print("Found it", m)
        else:
            print("Couldn't found it")
        return
    if alist[m] == x:
        print("Found it:", m)
        return m
    elif x < alist[m]:
        print(m, ":", alist[:m])
        binarySearch(alist[:m], x)
    else:
        print(m, ":", alist[m:])
        binarySearch(alist[m:], x)

x = int(input("number to search?"))
binarySearch(alist, x)
"""

""" Bubble Sort using Nested Loop
alist = [12, 3, 54, 39, 59, 6, 24, 39, 22, 78, 99, 11]
print("original list:", alist)

def bubbleSort(alist):
    for _ in range(len(alist) - 1):
        for i in range(len(alist) - 1):
            if alist[i] > alist[i + 1]:     # asending
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
    return alist
                
bubbleSort(alist)
print("sorted list:", alist)
"""

""" List, Tuple, Dictionary
names = ['a', 'b', 'c', 'd']
identifies = [1, 2, 3, 4, 5]
print(names + identifies)
print(names[:2], names[2:], names[1:3], names[:])   # list slicing
names.append('z')
print(names)
names.remove('z')
print(names)
del names[2]
print(names)
names.insert(2, 'c')
print(names)
if 'c' in names:
    print("found 'c' at: ", names.index('c'))
names.reverse()  #does not return a copy
print(names)
names.sort()     #does not return a copy
print(names)
names.append('b')
print(sorted(names))    # build-in sorted()
names.pop(2)    # different from python 2
print(names)
new_list = [sub.replace('b', 'd') for sub in names]     # list comprehension 
print(new_list) # replace all the 'b' in the list names
print(names)    # the orignal is not changed
names.insert(2, 'c')
names.pop()
print(names)
print([odds for index, odds in enumerate(names) if index % 2 == 1])
#print(list(map(lambda i : i % 2 == 1, enumerate(names))))
print([evens for index, evens in enumerate(identifies) if index % 2 == 0])

tpl = ('a', 'c', 'b')
print(tpl)
print(sorted(tpl))  # sorted() makes new copy, and covert the tuple to list
print(tpl)

dict = {}
dict["a"] = 1
print(dict)
dict[2] = 'b'
print(dict)
print(dict.keys())
print(dict.values())
for k in dict.keys():
    print(k, dict[k])
dict[2] = 'c'   # not append, will replace 'b'
print(dict)
#print({sd for sd in dict if sd.values() == 'c'})
"""

""" remove duplicates
mylist = ['a', 'c', 'b', 'b', 'd']
#mlist = [ x for x in mylist if x not in mlist]  # doesn't work, mlist is not defined
mylist = list(dict.fromkeys(mylist))
print(mylist)
"""

""" use to two lists to build a dictionary
names = ['a', 'b', 'c', 'd']
identifies = [1, 2, 3, 4, 5]
min_len = min(len(names), len(identifies))
new_dict = {}
for i in range(min_len):
    new_dict[identifies[i]] = names[i]
print(new_dict)
"""

""" merge two list
import itertools
names = ['a', 'b', 'c', 'd']
identifies = ['1', '2', '3', '4']
#result = list(map(list.__add__, names, identifies))
result = [list(itertools.chain(*i))
          for i in zip(names, identifies)] 
print(str(result))
"""

""" string
rstring = "Hello World"[::-1]
print(rstring)
rrstring = "".join(reversed(rstring))
print(rrstring)
rpstring = rrstring.replace('World', 'Hello')
print(rpstring)
#print(rpstring[::2])    # letter every other

import re
sp = [m.start() for m in re.finditer(r"Hello", rpstring)]
print(rpstring[sp[1]:])
"""

""" lambda, anonymous function
# lambda with filter()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
odd_list = list(filter(lambda x: (x%2 != 0), li))   # filter(), keep the True
print(odd_list)

odd_list = [i for i in li if (i % 2 != 0)]  # the other way
print(odd_list)

# lambda with map()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
double_list = list(map(lambda x: x*2, li))
print(double_list)

# lambda with reduce()
from functools import reduce    # perform repetive operation over a list
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
sum = reduce((lambda x, y: x + y), li)  # add items in a list
print(sum)
"""

""" print current time
import datetime
when = datetime.datetime(2020, 4, 3, 10, 53, 0)
print("year", when.year, "month", when.month, "day", when.day)
print("now", datetime.datetime.now())
"""

"""
class Card:
    def __init__(self, suit_id, rank_id):
        self.suit_id = suit_id
        self.rank_id = rank_id
        # error checking
        self.name = self.suit_id + self.rank_id

    def append(self, card):
        # some

    def remove(self, card)

deck = []
"""

""" Coin Head in Row
from random import *
coin = ["Heads", "Tails"]
head_in_row = 0
ten_head_in_row = 0
for i in range(1000000):
    if choice(coin) == "Heads":
        head_in_row += 1
    else:
        head_in_row = 0
    if head_in_row == 10:
        ten_head_in_row += 1
        head_in_row = 0
print("got 10 heads in row", ten_head_in_row, "times")
"""

""" Dice Statatistics
import random
totals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(1000):
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)
    dice = die_1 + die_2
    totals[dice] += 1

for i in range(2, 13):
    print(i, totals[i], 100 * totals[i] / 1000, "%")
#    print("total", i, "came up", totals[i], "times", "persentage", 100 * totals[i] / 1000, "%")
"""

""" Print Times Table
for i in range(1, 10):
    for j in range(1, 10):
        if j <= i:
            print(i, "x", j, "=", i * j, end = '\t')
    print()
"""

""" T[k] = k + T[k-1]
def tri_recursion(n):
    if n <= 0:
        return 0
    else:
        return(n + tri_recursion(n - 1))

def tri_sequence(n):
    tri_list = []
    for i in range(n):
        tri_list.append(tri_recursion(i))
    return tri_list

print(tri_sequence(7))
"""
        
""" Print Fabonacci Sequence
a, b = 0, 1
for i in range(10):
    print(a)
    a, b = b, a + b
"""

""" Build Fabonacci List
def fab(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fab(n - 1) + fab(n - 2)
    
def fab_seq(n):
    fab_list = []
    i = 0
    while i < n:
        fab_list.append(fab(i))
        i += 1
    return fab_list

print(fab_seq(10))
"""

""" Fizz Buzz with if-elif-else
for i in range(1, 101): # 101 is not included
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
"""

""" Fizz Buzz in one line
for i in range(1, 101): print("Fizz"*(i%3==0)+"Buzz"*(i%5==0) or i)
# print(list(map(lambda i: "Fizz"*(i%3==0)+"Buzz"*(i%5==0) or str(i), range(1,101))))
"""

""" Guess the Input
import  random
secret = random.randint(1, 99)
guess = 0
tries = 0
while guess != secret and tries < 3:
    guess = int(input("what is your guess? "))
    print(guess, secret) 
    tries += 1

if guess == secret:
    print("good")
else:
    print("bad")
"""

""" Try, Except, Else, Finally
f = open("beach_ball.png", 'rb')
try:
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when writing to the file")
else:
    print("good")
finally:
    f.close()
"""

""" raise an exception
x = 1.0
if not type(x) is int:
  raise TypeError("Only integers are allowed")
"""
# Debugging 
