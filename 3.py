lista =[3,4,1,6,32,0,86,36,2]
def ordenar (lista):
    lista_des=[]
    lista.sort()
    lista_des.append(lista.sort(reverse = True))
    return lista_des
print ('La lista para ordenar es: ',lista[:])
print('la lista ordenada descendiente es:', ordenar(lista))