
'''
MAx number of consecutive days for which the price of the stocks was less than or equal to 
todays price.
'''

price = [10, 4, 5, 90, 120, 80]
ans = [0] * len(price) 

def stockspan(price,ans):
    n = len(price)
    st = [] ## for storing indexes
    st.append(0)
    ans[0] = 1

    for i in range(1,n):
        while st and price[i] >= price[st[-1]]:
            st.pop()
        ans[i] = (i+1) if len(st)<=0 else (i-st[-1])    

        st.append(i)   
    print("Max consecutive days for which price was lower is: ")
    print(max(ans))     

stockspan(price,ans)