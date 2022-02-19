#Arrays and Strings in Python

# Python has a number of built-in data structures, such as arrays.
# Arrays give us a way to store and organize data, and we can use the built-in
# Python methods to retrieve or change that data.

# Arrays are useful if you want to work with many values of the same Python data type.

import array as arr

#Elements of an arrays ex)
students = ['Alex', 'Bill', 'Catherine', 'Andy', 'Molly', 'Rose']
print(students)

#indexing starts from zero



#Calling Elements
print(students[2]) # prints Catherine
print(students[-2]) # prints Molly



#Slicing
print(students[1:5]) #['Bill', 'Catherine', 'Andy', 'Molly']
#- include 1st element to 4th
print(students[:2]) #calling the 0th and 1st elements, everything till 2



#Extended Slicing : [start:stop:end]
>>> "ABCD"[0:2]
'AB'

>>> "ABCD"[0:4:2]
'AC'

>>> "ABCD"[1:]
'BCD'
>>> "ABCD"[:3]
'ABC'
>>> "ABCD"[1:3]
'BC'
>>> "ABCD"[1:3:]
'BC'
>>> "ABCD"[::2]
'AC'
>>> "ABCD"[::]
'ABCD'
>>> "ABCD"[:]
'ABCD'

>>> "ABCD"[::-1]
'DCBA'
>>> [0, 1, 2, 3][::-1]
[3, 2, 1, 0]

>>> # slices can be used to replace multiple items
>>> l = [0, 1, 2, 3]
>>> l[:2] = ("AB", "CD")
>>> l
['AB', 'CD', 2, 3]

>>> l = [0, 1, 2, 3]
>>> l[1:2] = (7, 8, 9, 10)
>>> l
[0, 7, 8, 9, 10, 2, 3]

>>> # when using extended slice syntax both chunks must match
>>> l = [0, 1, 2, 3]
>>> l[::2] = "ABCD"
Traceback (most recent call last):
  File "<interactive input>", line 1, in <module>
ValueError: attempt to assign sequence of size 4 to extended slice of size 2

>>> # deleting items
>>> l = [0, 1, 2, 3]
>>> del l[::2]
>>> l
[1, 3]



# Modifying items
students[5] = "Amy"




# Python Array Append and Pop


O(1)  append()	Adds an item to an array
O(1)-if last element, O(n)   pop()	Removes an item from an array
clear()	Removes all items from an array
O(n)   copy()	Returns a copy of an array             O(n)
 len()	Returns the number of elements in a list
0(1)  index()	Returns the index of the first element with a specific value
insert()	Adds an element to the array at a specific position
reverse()	Reverses the order of the array
sort()	Sorts the list

ex)
lst.append(2)
lst.pop()
lst.clear()
len(lst)
lst.index(0 #location you want index)
lst.insert()



# !!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!

ARRAYS
- One of the most important topics for programming interviews
- Most companies ask array questions at some point in the process
- Has specific upper and lower bounds (i.e. IndexOutOfBoundsException)
- Can be iterated through easily (O(n))
- Has lots of neat tricks to make your life easier, if you look closely!


Types of Problems
-Properties of Arrays (Does this array contain X? How do you check if…)
-2-D Matrices, n-D Arrays
-ArrayList (“endless” array; can be added to)
-Character Arrays (Strings)
-Rotation and Rearrangement
-Sorting & Searching


EXAMPLE PROBLEM: 2 POINTERS
Goal: Find the pair of elements in a sorted array of positive and negative integers whose sum is closest to zero.

Naive Solution O(n2): Sum all of the pairs, keep track of the indices of the pair with the sum closest to zero

Optimized Solution O(n): Use two pointers to compute sums
Begin with a pointer to the beginning and end of the list
Keep track of the smallest sum & the pair of indices
If the sum is negative, move the left pointer over.
If the sum is positive, move the right pointer over.
Stop when the pointers are adjacent
Return the pair of indices with the smallest sum



Things To Think About
 - Is this array already sorted?
 - Can I sort it, and still have the most efficient solution?
        (Better than O(nlogn)?)
 - What is the range of elements in the array?
 - Did I check my upper and lower bounds?
 - Would traversing in reverse make it more efficient?
 - Can I keep track of values in O(1) space? O(n) space?


Edge Cases
 - Empty arrays
 - Arrays with 1 or 2 elements
 - Repeated elements
 - If you encounter elements that are not allowed
What to return in these cases


TYPES OF SOLUTIONS
- Naive Solution: Typically use for loops
- Sliding Window Technique
- Fast i, slow j
- Use element values as indices (Bijection from ℕ → Elements)

SLIDING WINDOW
Used to get a contiguous subsequence of an array
Questions like:
“Given an array of size n and a number k, find the minimum summation of k elements.”


FAST i, SLOW j
- Variation of Sliding Window
- Has a reaching i, and a stationary j
- Good for in-place modification of an array

USE ARRAY ELEMENTS AS INDEX (FLAGGING!)
- Create a new array (O(k) extra space), and store TRUE (1) or
FALSE (0) in the indices whose values correspond with the element
you are keeping track of
- OR use your original array (O(1) extra space) to mark presence of
an element x by changing the value at the index x to negative




# !!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!
ARRAYs and Strings Approach

Buckets of types of problem solving approaches
1. Sliding Window
2. Two Pointer
3. Binary Search
4. Rearrange items by index

These types of algorithms reduce time complexting
Sliding window O(n^2) becomes O(n)
Two pointer O(n^2) becomes O(n)
Binary Search O(n^2) becomes O(log(n))
Rearrange items by index O(n^2) becomes O(n)


Problem 1. Shortest word distance - Sliding Window/Two Pointer method

words = ['hi', 'alpha', 'moon', 'bye', 'hi', 'mars', 'moon']
Find shortest distance between two words

ex) shortestDist('hi', 'bye')

def shorestDist(arr, word1, word2):
    i = -1 #index for word1
    j = -1 #index for word2
    min_dist = len(arr) + 1
    for x in range(0,len(arr))
        if arr[x] == word1:
            i=x
        if arr[x] == word2:
            j=x
        if i>-1 && j>1:
            min_dist = min(min_dist, abs(i-j)) #min, max, abs built-in funcs
    if min_dist==len(arr)+1
        return None
    return min_dist



Problem 2. Two pointer

[1,0,0,1,0,1,1,0,1,0]
Another example
[blue, green, blue, ......]

Sorting this array, could be done in O(nlogn) using a sorting algorithms
But O(n)?

arr = [1,0,0,1,0,1,1,0,1,0]
a=0 #we have 0s
b=1 #we have 1s
#a and b are the two types of data

def twoPointer(arr,a,b):
    i=0
    j=len(arr)-1
    while i<j:
        if(arr[i]==b):
            if(arr[j]==a):
                arr[i]=a
                arr[j]=b
                i+=1
                j-=1
            else:
                j-=1
        elif(arr[j]==a):
            i+=1
        else:
            i+=1
            j-=1
    return arr



Problem 3. Dutch Flag Problem (Two Pointer approach w/ Three Pointers)

# Will continue tom
