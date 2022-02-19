
def root(n):
    x = n
    while True:
        root = 0.5 * (x+(n/x))

        if abs(root-x)<1:
            break;

        x = root    

    return root   

print(root(4))         