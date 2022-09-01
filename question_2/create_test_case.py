import solution
import random

output = input("Test Case Number: ")
test_case  =int(input('Number of Test Case: '))
frr = open(f'testcase{output}\input.txt', 'w')
out = open(f'testcase{output}\output.txt', 'w')
max_element = min(int(input("Enter Max Number of Element[10**6]: ") or 10**6), 10**6)
max_height = min(int(input("Enter Max Height[10**8]: ") or 10**8), 10**8)

frr.write(str(test_case)+'\n')
for _ in range(test_case):
    # n = int(input())
    n = random.randint(3, max_element)
    # arr = list(map(int, input().split()))
    arr = []
    frr.write(str(n) + '\n')
    for i in range(n):
        rr = random.randint(0, max_height)
        frr.write(str(rr) + ' ')
        arr.append(rr)

    frr.write('\n')
    result = solution.trappingWater(arr, n)
    out.write(str(result) + '\n')