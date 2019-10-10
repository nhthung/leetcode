def threeSum(self, nums: List[int]) -> List[List[int]]:
    '''
    Given an array nums of n integers, are there elements a, b, c in nums
    such that a + b + c = 0? Find all unique triplets in the array
    which gives the sum of zero.
    '''
    triplets = []
    n = len(nums)
    
    # If size < 3, can't have a triplet
    if n < 3:
        return triplets

    # Sort array for 2 ptrs solution
    nums.sort()

    # If min > 0 or max < 0, then can't have sum = 0
    if nums[0] > 0 or nums[-1] < 0:
        return triplets
    
    # Iterate i through list
    for i in range(n):
        # Skip if same value of i
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        # Pointer j at right of i, k at end of list,
        # both will travel torwards the middle
        j = i + 1
        k = n - 1
        
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            
            # If sum < 0, then increase sum by moving j to the right (higher values)
            if s < 0:
                j += 1
                # Skip duplicates
                while j < k and nums[j] == nums[j-1]:
                    j += 1
            
            # If sum > 0, decrease it by moving k to the left (lower values)
            elif s > 0:
                k -= 1
                # Skip duplicates
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
            
            # If sum = 0, add triplet to list of results
            else:
                triplets.append([nums[i], nums[j], nums[k]])
                j += 1

                # Move both j to right and k to left
                while j < k and nums[j] == nums[j-1]:
                    j += 1
                k -= 1
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
        
    return triplets
