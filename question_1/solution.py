def count_set_bits(n):
    count = 0
    while n != 0:
        n = n & (n-1)
        count += 1
    return count

def countBitsFlip(a, b):
    return count_set_bits(a^b)
    
if __name__ == '__main__':
    for _ in range(int(input())):
        print(countBitsFlip(*list(map(int, input().split()))))