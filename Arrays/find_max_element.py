numbers = list(map(int, input("Enter numbers separated by space: ").split()))

largest = numbers[0]
for element in numbers[1:]:
    if element > largest:
    largest = element
print(f'{largest}: is'}
    
    

n = int(input("How many numbers: "))
numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

max_val = numbers[0]
for i in range(1, len(numbers)):
    if numbers[i] > max_val:
        max_val = numbers[i]
print(max_val)
    
