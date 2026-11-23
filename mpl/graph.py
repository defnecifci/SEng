def leibnitz(n):
  L=[]
  X=[]
  Z=[]
  s = 0
  for i in range(1,n+1):
    s= s+1.0*(-1)**(i+1)*4/(2*i-1)
    X.append(1)
    L.append(round(s,2))
    Z.append(3.14)
  return X, L, Z

def euler(n):
  E=[]
  total=0
  part=0
  pi=0
  for i in range(1,n+1):
    part= 1.0/(i*i)
    total+=part
    pi=total*6
    pi=pi**(0.5)
    E.append(round(pi,2))
  return E

def wallis(n):
  W=[]
  total=1
  pi=0

  for i in range(1,n+1):
    total *= (4.0*i*i)/(4.0*i*i-1)
    pi = 2*total
    W.append(round(pi,2))

  return W

rep=50
X,L,Z = leibnitz(rep)
E= euler(rep)
W=wallis(rep)

import matplotlib.pyplot as plt
plt.style.use('ggplot')
fig,ax = plt.subplots()

ax.plot(L, c='magenta', label="Leibnitz")
ax.plot(E, c='deeppink', label="Euler")
ax.plot(W, c='blue', label="Wallis")

ax.plot(Z, c='black', label="Pi=3.14")
ax.set_title("Approaching to number Pi", fontsize=12)
ax.set_xlabel('Number of iterations:' + str(rep), fontsize=10)
plt.legend(bbox_to_anchor=(1,1), ncol=4)
plt.show()