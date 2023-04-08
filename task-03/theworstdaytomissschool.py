n = int(input())
groups = list(map(int, input().split()))

car_count = 0
num_1, num_2, num_3, num_4 = 0, 0, 0, 0

# count the number of groups with 1, 2, 3, and 4 members
for g in groups:
    if g == 1:
        num_1 += 1
    elif g == 2:
        num_2 += 1
    elif g == 3:
        num_3 += 1
    else:
        num_4 += 1

# count the number of cars needed for each group size
car_count += num_4  # each group of 4 can go in one car
if num_3 >= num_1:  # if there are more groups of 3 than groups of 1
    car_count += num_3  # each group of 3 can go in one car
    num_1 = 0  # all groups of 1 have been accommodated
else:  # if there are more groups of 1 than groups of 3
    car_count += num_3  # all groups of 3 have been accommodated
    num_1 -= num_3  # some groups of 1 still need to be accommodated
    # each remaining group of 1 needs to be paired with a group of 2
    if num_2 % 2 == 0:
        car_count += num_2 // 2
        num_2 = 0
    else:
        car_count += num_2 // 2 + 1
        num_2 = 1

# count the number of cars needed for the remaining groups of 1 and 2
if num_2 > 0:  # if there are any groups of 2 remaining
    car_count += (num_1 + 1) // 2  # pair them with groups of 1
else:
    car_count += num_1 // 4 + (1 if num_1 % 4 != 0 else 0)

print(car_count+1)
