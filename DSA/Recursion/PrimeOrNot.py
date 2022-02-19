
def Prime(n,i):
   if n<2 : return False
   if n==i : return True
   if n%i==0 : return False

   return Prime(n,i+1)
            
           
if Prime(99,2) : print("is a prime number")
else :print("not a prime")       