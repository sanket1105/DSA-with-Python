def KadanesAlgorithms(arr):
    currmax = arr[0]
    maxtillNow = arr[0]

    for i in range(1,len(arr)):
        currmax = max(arr[i], currmax+arr[i])
        maxtillNow = max(maxtillNow, currmax)
    return maxtillNow   


## This idea is taking too much time
'''

def circular(arr):
    s = arr[0]
    for i in range(len(arr)):
        k = arr[i:] + arr[:i]
        s = max(KadanesAlgorithms(k),s)
    print(s) 

'''
## see the video for better understanding

def circular(arr):
    nonwrap = KadanesAlgorithms(arr)

    if nonwrap < 0: 
        print(nonwrap)  ## when  all the entries  are negative
        return 0

    totalsum = 0
    for i in range(len(arr)):
        totalsum += arr[i]
        arr[i] *= -1

    wrapsum = totalsum + KadanesAlgorithms(arr)

    print(max(nonwrap,wrapsum))    
   


circular([4,-4,6,-6,10,-11,12])
circular([-1,4,-6,7,5,-4])
circular([-18,-12])
circular([-3,-18,-22,-21,-17,16,-14,28,-22])

## most optimized method

def circularopt(arr):

    totalsum,maxtillnow,mintillnow,summax,summin = 0,arr[0],arr[0],0,0

    for i in range(len(arr)):
        summax = max(summax+arr[i],arr[i])
        maxtillnow = max(maxtillnow,summax)

        summin = min(summin+arr[i],arr[i])
        mintillnow = min(mintillnow,summin)

        totalsum += arr[i]

    return max(maxtillnow,totalsum - mintillnow) if totalsum >0 else maxtillnow


print(circularopt([1,-6,-7,4]))
