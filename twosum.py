#include <stdio.h>
#include <stdlib.h> // Required for malloc

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {

    int* result = (int*)malloc(2 * sizeof(int));
    *returnSize = 2;

    for (int i = 0; i < numsSize; i++) {
         
        for (int j = i + 1; j < numsSize; j++) {

            if (nums[i] + nums[j] == target)  {
                result[0] = i;
                result[1] = j;
                return result;
            }
        } 
    }

    // FIXED: Changed resultSize to returnSize to match the function parameter
    *returnSize = 0;
    return NULL;
}
