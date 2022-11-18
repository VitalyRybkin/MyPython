from array import *
import time
import random

start = time.time()

nums = array('i')
index = 0

# arrSize = int(input('Enter an array size:'))
arrSize = 6

while index < arrSize:
    nums.append(random.randint(1, 100))
    index += 1

#nums = [5, 4, 11, 0, 1, 10]
index = 0
print(nums)

while index < arrSize - 1:
    if nums[index] > nums[index + 1]:
        changeIndex = index + 1
        curIndex = index
        check = 0
        print(index, curIndex, changeIndex)
        for check in range(0, changeIndex, 1):
            print(nums[check], nums[changeIndex])
            if nums[check] > nums[changeIndex]:
                nums.insert(check, nums[changeIndex])
                del nums[changeIndex + 1]
                break
    index += 1
print(nums)

end = time.time()

print("Execution time of the program is- ", end-start)

