import os

def lonelyinteger(a):
    result = 0
    for num in a:
        # XOR each number with the result
        result ^= num 
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    
    result = lonelyinteger(a)
    
    fptr.write(str(result) + '\n')
    fptr.close()
