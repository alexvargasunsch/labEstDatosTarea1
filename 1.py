import random
def desorden (a, n):
    for i in range(a,n):
        ra = random.randint(i , n-1)
        a [i], a [ra] = a [i],a[i]
lista =[1,2,3,4,5,6,7,8,9]
desorden(lista,len(lista))
print(lista)