def twonumSum(self,nums,target):
    d={}
    l=len(nums)
    for i in range(l):
        v=target - nums[i]
        if nums[i] in d:
          return(d[nums[i]],i)
        else:
            d[v]=i
            
