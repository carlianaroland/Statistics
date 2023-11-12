# Carliana Roland 2/10/23 Comp163

# You are to calculate the statistics using a series of numbers, but you have to create your own algorithm.
print('These are your numbers for statistic calculation, the range for the series of numbers is 0-100.')
num1 = int(input('Enter number here: '))
num2 = int(input('Enter number here: '))
num3 = int(input('Enter number here: '))
num4 = int(input('Enter number here: '))
num5 = int(input('Enter number here: '))

# Find the mean for the statistic numbers.
numbers = {num1, num2, num3, num4, num5}
for i in numbers:
    if i > 100:
        print(i, 'This number is out of range')
    else:
        print(i, "This number is fine")
mean = 0
x = 0
for i in numbers:
    mean += i
    x += 1
mean //= x
print(f'The mean for the series of numbers is: {mean}')
# Find the max for the statistic numbers.
y = 0
for i in numbers:
    if y > i:
        i = y
print(f'The max for the series of numbers is: {y}')
# Find the min for the statistic numbers.
min_num = 100
for i in numbers:
    if min_num >= i:
        min_num = i
print(f'The min for the series of numbers is: {min_num}')
# Find the mode for the statistic numbers.
mode = 0
for i in numbers:
    if mode <= i:
        mode += 1
        mode = i
print(f'The mode for the series of numbers is: {mode}')
# Find the median for the statistic numbers.
median = 0
for i in numbers:
    if median < num3:
        median = num3
print(f'The median for the series of numbers is: {median}')
print('Goodbye.')
