
def bubble_sort(nums):
    for i in range(0,len(nums)-1):
        swapped=False
        for j in range(0,len(nums)-i-1):
            if(nums[j]>nums[j+1]):
                nums[j],nums[j+1]=nums[j+1],nums[j]
                swapped=True
                
                
        if(swapped==False):
            break
        
    return nums
        
print(bubble_sort([5,3,8,2]))
                   