nums = [3,3]
nums_index = []
target = 6
found = False

for i in range(len(nums)):
    for j in range(1, len(nums)):
        if i == j:
            j += 1
        if nums[i] + nums[j] == target:
            nums_index.append(i)
            nums_index.append(j)
            print(nums_index)
            found = True
            break
    if found == True:
        break
            
