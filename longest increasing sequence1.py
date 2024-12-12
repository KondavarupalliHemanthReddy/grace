s=[-1,2,3,0,1,2,3,-5,-4,-3,-2,-1,9]
n=len(s)
dp=[1]*n
for i in range(1,n):
    if s[i]>s[i-1]:
        dp[i]=max(dp[i],dp[i-1]+1)
print(max(dp))