import numpy as np
                     
a = [
      [0.2,0.1,1,1,0],
      [0.1,4,-1,1,-1],
      [1,-1,60,0,-2],
      [1,1,0,8,4],
      [0,-1,-2,4,700]
                      ]
b = [1,2,3,4,5] 
n = len(a)


t =[7.859713071, 0.422926408,-0.073592239,-0.540643016,0.010626163]
count=0
T=np.zeros(n)
r=np.zeros(n)
x=np.zeros(n)

R=np.zeros(n)
d=np.zeros(n)
print(x)

for k in range(n):
 r[k]=b[k]
 d[k]=b[k]
 

count=0
for i in range(100):
	s=np.matmul(r,r)/np.matmul(d,np.matmul(a,d))
	p=np.matmul(a,d)
	for j in range(n):
	    x[j]+=s*d[j]
	    R[j]=r[j]
	    r[j]-=s*p[j]
	    T[j]=abs(t[j]-x[j])
	print('x',i+1,':',x)
	if (max(T))<=0.01:
		break
	
	c=np.matmul(r,r)/np.matmul(R,R)
	
	for l in range(n):
	        d[l]=r[l]+c*d[l]
	count+=1   
print('NUmber of iteration required to reach within 1% accuracy is:',i+1)
