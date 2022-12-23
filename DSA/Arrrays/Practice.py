

a = [10,8,6,4,2,10,11]
diff  = a[1] - a[0]
curr = 2
ans = 2
for i in range(2,len(a)):
    s = a[i]-a[i-1]
    if s == diff:
         curr+=1
    else: 
        diff=s  
        curr = 2
    ans = max(curr,ans)

print(ans)
    
####################################
#first repeating element:

arr = [ 10, 5, 3, 4, 3, 5, 6 ]
a = [0]*(max(arr))
found = False

for i in arr:
    if a[i-1]==1:
        print(i)
        found = True
        break
    else:
        a[i-1] = 1

if found==False: 
    print("No repeating element") 

##################################
# Largest word in the sentence
s = "I am SanketZ"
word = ""
ans = ""
for i in s:
    if i!=" ":
        word+=i  
    else:
        if len(word) > len(ans):
            ans = word 
            word = ""
if len(word)>len(ans):
    print(word)
else: print(ans)

##############################
# matrix multiplication

a1 = [[2,4,1,2],[8,4,3,6],[1,7,9,5]]
a2 = [[1,2,3],[4,5,6],[7,8,9],[4,5,6]]
ans = [[0 for i in range(len(a2[0]))] for j in range(len(a1))]

for i in range(len(a1)):
    for j in range(len(a2[0])):
        for k in range(len(a1[0])):
            ans[i][j] += a1[i][k] * a2[k][j]

print(ans)

####################################################
# print all subArrays
a = [-1,4,7,2]

for i in range(len(a)):
    for j in range(i,len(a)):
        for k in range(i,j+1):
            print(a[k],end=" ")
        print("")    

####################################################
# subArrays with given sum

a = [1,2,3,8,5]
s= 16
n = len(a)

total = a[0]
i = 1
start = 0
while i <= n :
    while total > s and start<=i-1:
        total -= a[start]
        start+=1
    if total==s:
        print("indexes between: ", start,i-1)
        break
    if i<n:
        total += a[i]
    i+=1    

#################################################
# record breaking day
a = [1,2,0,7,2,0,2,8]
maxi = a[0]
count = 0

for i in range(len(a)-1):

    if a[i] > a[i+1] and a[i] > maxi:
        count+=1
    maxi = max(maxi,a[i])

if a[-1] > maxi: ## for the last value, it just needs to be greater than the previous values
    count+=1

print(count)

#################################################################

## search in sorted matrix

a = [[1,4,7,11],[2,5,8,12],[3,6,9,16],[10,13,14,17]]
n = len(a)
target = 17
found = False
r,c = 0,n-1
while r<n and c>=0:
    if a[r][c] == target:
        print("at index ",r,c)
        found = True
        break
    elif a[r][c] > target:
        c-=1
    else: 
        r+=1

if found==False: print("Not there") 

## ###############################################
# smallest positive missingNumber

arr = [1,2,3]
a = [0] * (len(arr)+1)
n = len(arr)
found = False
a[0] = 1
for i in range(n):
    if arr[i]<0 or arr[i]>n:
        arr[i] = 0
for i in range(n):
    a[arr[i]] = 1

for i in a:
    if i == 0: 
        print(a.index(i))
        found = True

if found==False: print(n+1)

##################################################
# spiral matrix

a= [[1,2,3],[4,5,6],[7,8,9]]
rb,cb=0,0
re,ce = len(a)-1, len(a[0])-1
ans=[]

while rb<re and cb<ce:
    for i in range(cb,ce+1):
        ans.append(a[rb][i])
    rb+=1

    for i in range(rb,re+1):
        ans.append(a[i][ce])
    ce-=1

    if rb<re:
        for i in range(ce,cb-1,-1):
            ans.append(a[re][i])
    re-=1

    if ce>cb:
        for i in range(re,rb-1,-1):
            ans.append(a[i][cb])
    cb+=1    

print(ans)


######################################################
# trio with sum 0
nums = [-1,0,1,2,-1,-4]
nums.sort()
i = 0
n = len(nums)
ans = set()
for i in range(n):
    j = i+1
    k = len(nums)-1
    while j<k:
        s=nums[i] + nums[j] + nums[k] 
        if s==0:
            ans.add((nums[i],nums[j],nums[k]))
            j+=1
            k-=1
        elif s>0:
            k-=1
        else: j+=1

print(list(ans))                
        







