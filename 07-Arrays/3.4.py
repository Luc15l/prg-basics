arr=[15, 8, -31, 47, -2, 19]
max=arr[0]
min=arr[0]
for n in arr:
    if n>max:
        max=n
    if n<min:
        min=n
print(f'max to {max} a min to {min}')