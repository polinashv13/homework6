import random 
r = int(input("Ведите размерность массива: "))
masr = []
print("Введите элементы массива")
for i in range(r):
    masr.append(round(random.uniform(0,9),2))
m = max(masr)
ind = masr.index(m)
for i in range(ind+1,r):
    masr[i] = 0
print(masr)