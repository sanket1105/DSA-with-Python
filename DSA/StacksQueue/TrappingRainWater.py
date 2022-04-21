

## trapping the rain water

a = [3,1,2,4,0,1,3,2]

def trap_water(a):
    stack = []
    ans = 0
    
    for i,heightA in enumerate(a):
        while stack and heightA > a[stack[-1]]:
            curr_height = a[stack.pop()]
            if not stack:  ## if stack becomes empty
                break   
            j, heightB = stack[-1], a[stack[-1]]
            volume = min(heightB, heightA) - curr_height
            ans+= volume * (i-j-1)

        stack.append(i)    

    return ans

print(trap_water(a))





