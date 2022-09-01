# Bit Magic

Given two numbers X and Y. Count the number of bits to be flipped to convert X into Y

### Example 1

```
Input: X = 30, B = 20
Output: 2
Explanation:
X = 11110
Y = 10100
There are 2 bits of X that need to be flipped to get Y
```

### Example 2

```
Input: X = 27, Y = 10
Output:
X = 11011
Y = 01010
There are 2 bits of X that need to be flipped to get to Y
```

### Input Format

- The first Line Contains a single integer T - The number of test case. Then the test case follow.
- The first and only line of each test case contains three space-separated integers **X** and **Y** — the parameters mentioned in the problem statment.

### Output Format

For each test case output nummbers of bits to be flipped to convert X into Y.

### constraints

1 $\le$ X, Y $\le$ 10<sup>6</sup>

**Expected Time Complexity:** O(log N)

### Solution

```
def count_set_bits(n):
    count = 0
    while n != 0:
        n = n & (n-1)
        count += 1
    return count

def countBitsFlip(a, b):
    return count_set_bits(a^b)

for _ in range(int(input())):
    print(countBitsFlip(*list(map(int, input().split()))))
```
