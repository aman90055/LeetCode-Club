import os

def birthdayCakeCandles(candles):
    # Find the maximum height among all candles
    max_height = max(candles)
    # Count how many times the maximum height appears in the list
    return candles.count(max_height)

if __name__ == '__main__':
    # HackerRank stub code
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    
    result = birthdayCakeCandles(candles)
    
    fptr.write(str(result) + '\n')
    fptr.close()
