n = int(input())

# Create sets to store the x and y coordinates of the points
x_coords = set()
y_coords = set()

# Create sets to store the points with at least one neighbor in each direction
right = set()
left = set()
up = set()
down = set()

# Read the points and populate the sets
for i in range(n):
    x, y = map(int, input().split())
    x_coords.add(x)
    y_coords.add(y)
    if x not in right and all((x+1, y) in {(x1, y1) for x1, y1 in points} for points in [left, up, down]):
        right.add((x, y))
    if x not in left and all((x-1, y) in {(x1, y1) for x1, y1 in points} for points in [right, up, down]):
        left.add((x, y))
    if y not in up and all((x, y+1) in {(x1, y1) for x1, y1 in points} for points in [left, right, down]):
        up.add((x, y))
    if y not in down and all((x, y-1) in {(x1, y1) for x1, y1 in points} for points in [left, right, up]):
        down.add((x, y))

# Find the points that have at least one neighbor in each direction
optimal_vantage_points = [(x, y) for x in x_coords for y in y_coords if (x, y) in right and (x, y) in left and (x, y) in up and (x, y) in down]

# Print the number of optimal vantage points
print(len(optimal_vantage_points))
