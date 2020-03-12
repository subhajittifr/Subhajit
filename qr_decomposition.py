import numpy as np
n=100 #maxium iteration
a=[
   [5,-2],
   [-2,8]]
m=len(a)
d=np.zeros(m)
T=np.zeros((m,m))
e,v=np.linalg.eigh(a)
e=e[::-1] #reversing e
D=np.zeros((m,m))
for k in range(m):
	D[k][k]=e[k]
print('Target matrix to obtain:\n',D)	
#print(e)
q,r=np.linalg.qr(a)
# print(q)
# print(r)
for i in range(n):
	a=np.matmul(r,q)
	q,r=np.linalg.qr(a)
	print('After',i+1,'iteration:\n',a)
	#for j in range 
	T=abs(D-a)
	if T.max()<=0.01:
		break
	
print('Thus',i+1,"iteration required to diagonalize the given matrix within 1% accuracy")
	