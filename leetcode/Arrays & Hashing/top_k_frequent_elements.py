# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]


def top_k_frequent(nums, k):
    nums_dict = {}
    output = []
    
    for i in nums:
        if i in nums_dict:
            nums_dict[i] += 1
        else:
            nums_dict[i] = 1
        
    for _ in range(k):
        max_value = max(nums_dict, key = nums_dict.get)
        output.append(max_value)
        del nums_dict[max_value]
    return output  

print(top_k_frequent([1], 1))         