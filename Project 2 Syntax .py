Project 2 Syntax 


#two sum, brute force approach
def twoSum(nums, target):
    if not nums: #if array is empty, return nothing
        return None
    else:
        for i in range(len(nums)): #starts at first index
            for j in range(i+1, len(nums)): #starts at index i+1 
                if nums[i] + nums[j] == target: #if num at index i + num at index j = target
                    return i,j #return indices
print(twoSum([3,4,5,6], 11)) #test run
