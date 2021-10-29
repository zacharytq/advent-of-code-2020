target_number = 2020

with open('input_day_1.txt') as input:
    nums = []
    while (line := input.readline().rstrip()):
        nums.append(int(line))
    nums.sort()
    for i, number in enumerate(nums):
        complementary_number = target_number - number
        if complementary_number in nums[i+1:]:
            product = complementary_number * number
            print('Number 1: {} Number 2 {} Product: {}'.format(number, complementary_number, product))
            break

