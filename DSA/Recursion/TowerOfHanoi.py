
def TowerOfHanoi(n,source,destination,helper):
    if n==0: return
    TowerOfHanoi(n-1,source,helper,destination)
    print("Move disk ",n, "from rod ", source," to ", destination)
    TowerOfHanoi(n-1,helper,destination,source)

  
n=2
TowerOfHanoi(n,"S","D","H")


## see how to calculate the time complexity of this problem