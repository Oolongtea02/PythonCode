data = [4, 5, 104, 105, 110, 120, 130, 150, 160,
        170, 183, 185, 187, 188, 191, 350, 360]

# del data[0:2]
# print(data)
# del data[14:]
# print(data)

min_valid = 100
max_valid = 200

for index, value in enumerate(data):
    if (value < min_valid) or (value > max_valid):
        stop = index
        break

print(stop)
del data[:stop]
print(data)

# process the high value
start = 0
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        # set 'start' to the position of the first
        # item to delete, which is 1 after the index
        start = index + 1
        break

print(start)
del data[start + 1:]
print(data)