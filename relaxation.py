                  
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
w=1.25
print(x) 
t =[7.859713071, 0.422926408,-0.073592239,-0.540643016,0.010626163]
T=np.zeros(n)
for i in range(100):             
    for j in range(0, n):         
        d = b[j]                   
        for k in range(n):      
            if(j != k): 
                d-=a[j][k]*x[k] 
        x[j] = w*(d/a[j][j])+(1-w)*x[j]   
        T[j]=abs(t[j]-x[j])
    if max(T)<=0.01:
        break
        
    print("Result of",i+1,"iteration is:\n",x)   
print("Number of iteration=",i+1)            
        
    



