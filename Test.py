
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    retList=[]
    for i in range(0,len(nums)-1):
        for j in range(i+1, len(nums)-1):
            if nums[i]+nums[j]== target:
                print("Inside if")
                return [i,j]   


print(twoSum([1,2,3,3,45,2], 48))