nums = []

for i in range(5):
    value = int(input("Enter any 5 number:  "))
    nums.append(value)

largest = max(nums)
smallest = min(nums)
add = sum(nums)

print(largest)
print(smallest)
print(add)