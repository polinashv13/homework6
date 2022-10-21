import random 
r = int(input("Ведите размерность массива: "))
masr = []
print("Введите элементы массива")
def massive(t):
    masr = []
    for i in range(t):
        masr.append(round(random.uniform(0,9),2))
    return masr
masr = massive(r)
m = max(masr)
ind = masr.index(m)
for i in range(ind+1,r):
    masr[i] = 0
print(masr)