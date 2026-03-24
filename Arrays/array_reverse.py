data = list(map(int,input("enter numbers ").split()))
n = len(data)
reversed_data = []
for i in range(n-1,-1,-1):
    reversed_data.append(data[i])
print(reversed_data)
