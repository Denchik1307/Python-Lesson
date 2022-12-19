import os
os.system('cls')  # сибки


# array = [1,2,3,4,5,6,7,8,9,10]
# k = 2
# for i in range(0,k):
#     array.insert(0,array[-1])
#     array.pop(-1)

# print(array)


array = [0, -1, 5, 2, 3, 3, 9, 7, 6, 9]
count = 0
for i in range(0, len(array)-1):
    if array[i] < array[i+1]:
        count += 1

print(array)
print(count)


print("\n\n\n\n")


inpDict = {"I": "S001", "II": "S002", "III": "S001",
           "IV": "S005", "V": "S005", "VI": "S009", "VII": "S007"}

res = set(inpDict.values())

print(inpDict.values(), "\n")
print(sorted(res))
