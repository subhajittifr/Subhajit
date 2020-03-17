



import numpy as np
import time
def invert(M):
	n=max(M.shape)
	N=np.zeros((n,n))
	for i in range(n):
		for j in range(n):
			N[j][-i-1]=M[j][i]
	return(N)
R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
  
  
print("Enter the entries in a single line row wise(separated by space): ") 
  
# User input of entries in a  
# single line separated by space 
entries = list(map(int, input().split())) 
  
# For printing the matrix 
A = np.array(entries).reshape(R, C) 
start_time1=time.time()
print('The given matrix is:\n',A) 
# A=[
#    [0,1,1],
#    [0,1,0],
#    [1,1,0],
#    [0,1,0],
#    [1,0,1]]
a=np.transpose(A)

c=np.matmul(A,a)
d=np.matmul(a,A)
u1,U1=np.linalg.eigh(c)
v1,V1=np.linalg.eigh(d)

U=invert(U1)
V=invert(V1)


S=np.matmul(np.transpose(U),np.matmul(A,V))
start_time2=time.time()
print('After performing SVD we obtain:')
print('U:\n',U)
print('S:\n',S)
print('V:\n',V)

print("Time required: ",time.time()-start_time1)

start_time2=time.time()
U1,S1,V1=np.linalg.svd(A)
print("SVD form using np.linalg.svd: \n")
print('U1\n:',U1)
print('S1\n:',S1)
print('V1\n:',V1)
print("Time required for performing SVD: ",(time.time()-start_time2))

