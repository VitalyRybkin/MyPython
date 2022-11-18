import random
import time
from array import *


def main():
    start = time.time()
# Creating an array
    nums = array('i')
    MakeArray(nums)
    print("Old array", end=": ")
    for i in range(0, len(nums), 1):
        print(nums[i], end=' ')
# Sorting an array
    NowSorting(nums)
    print("\nNew array", end=": ")
    for i in range(0, len(nums), 1):
        print(nums[i], end=' ')
# Program execution time
    end = time.time()
    print(f"\n\nExecution program time is: {end - start:.6f}")


def MakeArray(nums):
    # arr_size = int(input("Enter an array size:"))
    arr_size = 10
    # nums = [12, 4, 11, 10, 8, 1]
    for index in range(0, arr_size, 1):
        # nums.append(int(input(F"Enter num ${index + 1} for array:")))
        nums.append(random.randint(1, 100))
    return nums


def NowSorting(nums):
    index = 1
    while index < len(nums):
        cur_index = 0
        flag = False
        for cur_index in range(0, index, 1):
            if nums[cur_index] > nums[index]:
                flag = True
                break
        if flag:
            nums.insert(cur_index, nums[index])
            del nums[index + 1]
        index += 1
    return nums

main()
