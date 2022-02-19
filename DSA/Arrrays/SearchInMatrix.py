
## rows and cols sorted in ascending order 

a = [[1,4,7,11],[2,5,8,12],[3,6,9,16],[10,13,14,17]]
n = len(a)

target = 199
## start from [0][n-1]
r,c = 0,0
answer = False

while(r<n and c>=0): ## since we are starting from max value of c, so c can go upto min value that is zero
    if a[r][c]==target:
        answer = True
        break

    if a[r][c]>target:
        c-=1
    else: r+=1
      
print(answer)     