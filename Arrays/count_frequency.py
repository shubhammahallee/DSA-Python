items = input("Enter items separated by space: ").split()

# convert numbers to int
for i in range(len(items)):
    if items[i].isdigit():
        items[i] = int(items[i])

target = input("Enter target: ")

# convert target if number
if target.isdigit():
    target = int(target)

count = 0

for item in items:
    if item == target:
        count += 1

print("Count:", count)
