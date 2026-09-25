def selection_sort(nums):
    length=len(nums)
    for i in range(length-1):
        max=nums[0]
        maxindex=0
    
        for j in range(1,length):
            if(nums[j]>max):
             max=nums[j]
             maxindex=j
            
        nums[maxindex],nums[length-1]=nums[length-1],nums[maxindex]
        length-=1
            
    return nums
            
print(selection_sort([29,10,14,13,37]))