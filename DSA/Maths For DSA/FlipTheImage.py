

## reverse the image and flip it
## Input: image = [[1,1,0],[1,0,1],[0,0,0]]
## Output: [[1,0,0],[0,1,0],[1,1,1]]

def flip_image(arr):
    return [[i^1 for i in row[::-1]]for row in arr]
    ## 1 ^ i  or 1 - i

s = flip_image([[1,1,0],[1,0,1],[0,0,0]])    
print(s)