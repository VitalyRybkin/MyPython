from array import *
import random
import time

start = time.time()

nums = array('i')
index = 0
startIndex = 0
# arrSize = int(input("Enter an array size:"))
arrSize = 6

while index < arrSize:
    nums.append(random.randint(1, 100))
    index += 1

print(nums)
# index = 0

while arrSize - 1 > startIndex:
    for index in range(startIndex, arrSize - 1, 1):
        if nums[index] > nums[index + 1]:
            nums[index], nums[index + 1] = nums[index + 1], nums[index]
    arrSize -= 1
    for index in range(arrSize - 1, startIndex, -1):
        if nums[index] < nums[index - 1]:
            nums[index], nums[index - 1] = nums[index - 1], nums[index]
    startIndex += 1
    print(nums)

end = time.time()

print("Execution time of the program is- ", end-start)
