
nums=[-1,4,2,1,9,10]
i=0
while i<len(nums):
  
    correctIndex = nums[i]-1
    if nums[i]>0 and nums[i]<len(nums)  and nums[i]!=nums[correctIndex]:
        nums[i],nums[correctIndex] = nums[correctIndex],nums[i]
    else: i+=1    

print((nums))

found=False
for i in range(len(nums)):
    if nums[i]!=i+1:
        found=True
        print(i+1)
        break

if found==False:
    print(nums[i]+1)
