def twonumSum(self,nums,target):
l=len(nums)
for i in range(l):
  v=target- nums[i]
  if v in nums:
    b=nums.index(v)
    if i ！=b:
      return i,b
      break
     else:
        continue
