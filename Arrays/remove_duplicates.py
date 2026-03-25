numbers = list(map(int, input().split()))

seen = set()
unique_element = []

for num in numbers:
    if num not in seen:
        seen.add(num)
        unique_element.append(num)

print(unique_element)
