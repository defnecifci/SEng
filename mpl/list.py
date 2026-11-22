import random
t = []
print(len(t))

for i in range(8):
    element = int (6*random.random())+1
    t.append(element)
    
print(t)
print(len(t))

print(t[2])
print(t[7])
print(t[-1]) #listedeki son elementi yazdırıyor.

print(t[2:5])

t.reverse()
print(t)

print(t[::-1]) #reverse yapıyor listeyi