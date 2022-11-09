# Some tests from my webseminar


# Count positive elements
number = [-2, 8, 14, -34, -9, 7, 7, 4]
size = 8
count = 0
index = 0

while index < size:
    if number[index] > 0:
        count += 1
    index += 1

print(f"Amount of positive nums:", count)

# Arithmetic mean

size = 6
index = 0
avg = 0
sum = 0
numbers = [2, 5, 13, 7, 6, 4]

while index < size:
    sum += numbers[index]
    index += 1

avg = sum / size

print("\nArithmetic mean:", avg)

# Move the largest element to the left

numbers = [2, 5, 13, 7, 6, 4]
size = 6
index = 0
maxIndex = 0
max = numbers[maxIndex]

print("\nOld array:", numbers)

while index < size:
    if numbers[index] > max:
        maxIndex = index
        max = numbers[index]
    index = index + 1

numbers[maxIndex] = numbers[size - 1]
numbers[size - 1] = max

print("\nNew array:", numbers)

# dog run

count = 0
dist = 10000
first_f_speed = 1
sec_f_speed = 2
dog_speed = 5
friend = 2

while dist > 10:
    if friend == 1:
        time = dist / (first_f_speed + dog_speed)
        friend = 2
    else:
        time = dist / (sec_f_speed + dog_speed)
        friend = 1
    dist = dist - (first_f_speed + sec_f_speed) * time
    count += 1
print(f"Dog runs {count} times")
