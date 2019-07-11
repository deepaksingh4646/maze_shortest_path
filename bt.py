m=[[1,1,1,0,0,1],
   [1,1,0,1,0,1],
   [1,1,1,0,0,1],
   [1,2,0,0,1,1],
   [0,1,1,0,0,1],
   [1,1,1,0,1,1]]
l=[]
def find(m,path,i,j,n,s):
    if i<0 or j<0 or i>=n or j>=n:
        return 0
    if ((i==n-1 or i==0 or j==0 or j==n-1) and m[i][j]==0):
        path[i][j]=1
        s+=1
        l.append(s)
        return 0
    if m[i][j]==1 or path[i][j]==1:
        return 0
    s+=1
    path[i][j]=1    
    find(m,path,i,j+1,n,s)
    find(m,path,i,j-1,n,s)
    find(m,path,i-1,j,n,s)
    find(m,path,i+1,j,n,s)
    path[i][j]=0

def sam(m,n):
    s=0
    path=[[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        for j in range(n):
            if m[i][j]==2:
                find(m,path,i,j,n,s)
    
n=len(m)
sam(m,n)
print(min(l)-1)








    
