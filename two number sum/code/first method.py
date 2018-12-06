def number(self,nums,target):
  n=len(nums)
  for x in range(n）：
    for j in range(x+1,n):
        if nums[j] == target - nums[x] :
            return x,j
            break
        else:
           continue

