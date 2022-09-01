import solution
import random

output = input("Test Case Number: ")
test_case  =int(input('Number of Test Case: '))
frr = open(f'testCases\input\input0{output}.txt', 'w')
out = open(f'testCases\output\output0{output}.txt', 'w')
max_element = min(int(input("Enter Max Number of Element[10**6]: ") or 10**6), 2**31)

frr.write(str(test_case)+'\n')
for _ in range(test_case):
    # n = int(input())
    a = random.randint(1, max_element)
    b = random.randint(1, max_element)
    # arr = list(map(int, input().split()))
    frr.write(f"{str(a)} {str(b)}" + '\n')
    
    result = solution.countBitsFlip(a, b)
    out.write(str(result) + '\n')
    