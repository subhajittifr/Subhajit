                  
import numpy as np
x = [0, 0, 0,0,0]                         
a = [
      [0.2,0.1,1,1,0],
      [0.1,4,-1,1,-1],
      [1,-1,60,0,-2],
      [1,1,0,8,4],
      [0,-1,-2,4,700]
                      ]
b = [1,2,3,4,5] 
n = len(a)
w=1
print(x) 
t =[7.859713071, 0.422926408,-0.073592239,-0.540643016,0.010626163]
c=np.zeros(n)
x=np.zeros(n)
#x=np.zeros(3)

count=0

for i in range(37):
      for j in range(n):
            d=b[j]
            for k in range(n):
                if(k!=j):
                    d-=a[j][k]*x[k]
            c[j]=d/a[j][j]        
        
      for l in range(n):
        x[l]=c[l]
      T=abs(x-t)
      if max(T)<=0.01:
        break
      print("Result of",i,"th iteration is:\n",x)   
print("Number of iteration=",count)      
  
    
 
        
    
    
