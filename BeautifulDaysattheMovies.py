import math
import os

def beautifulDays(i, j, k):
    beautiful_count = 0
    
    # Loop through each day in the inclusive range
    for day in range(i, j + 1):
        # Convert to string, reverse it, and convert back to integer
        reversed_day = int(str(day)[::-1])
        
        # Check if the absolute difference is evenly divisible by k
        if abs(day - reversed_day) % k == 0:
            beautiful_count += 1
            
    return beautiful_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    i = int(first_multiple_input[0])
    j = int(first_multiple_input[1])
    k = int(first_multiple_input[2])
    
    result = beautifulDays(i, j, k)
    
    fptr.write(str(result) + '\n')
    fptr.close()
