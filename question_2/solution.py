from cgi import test
import random

def trappingWater(arr,n):
        left_max = [arr[0]]
        for i in range(1, n):
            left_max.append(max(arr[i], left_max[-1]))
        right_max = [arr[-1]]
        for i in range(n-2, -1, -1):
            right_max.append(max(arr[i], right_max[-1]))
        right_max.reverse()
        ans = 0
        for i in range(n):
            max_height = min(left_max[i] , right_max[i])
            if max_height > arr[i]:
                ans += max_height - arr[i]
        return ans

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        result = trappingWater(arr, n)
        print(result)