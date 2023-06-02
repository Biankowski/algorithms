from functools import reduce

# Works but it isn't O(n)
import copy
def product_except_self(nums):
    output = []
    temp = 0
    temp_array = []
    
    for i in range(len(nums)):
        temp = nums[i]
        temp_array = nums.copy()
        nums.remove(nums[i])
        output.append(reduce(lambda x,y: x*y, nums))
        nums = temp_array
        nums[i] = temp
    
    return output


def product_except_self_2(nums):
    length = len(nums)
    output = [1] * length
    
    pre = 1
    post = 1
    
    for i in range(length):
        output[i] *= pre
        pre = pre *nums[i]
        
        output[length - i - 1] *= post
        post = post*nums[length - i - 1]
    return output

# Neetcode solution - Best time complexity - O(n) & Best memory Complexity - O(1)

def neetcode_solution(nums):
    output = [1] * (len(nums))
    
    prefix = 1
    for i in range(len(nums)):
        output[i] = prefix
        prefix *= nums[i]
        
    postfix = 1
    for i in range(len(nums) -1, -1, -1):
        output[i] *= postfix
        postfix *= nums[i]
    
    return output

print(neetcode_solution([1,2,3,4]))