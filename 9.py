def suma (a, b):
    if b == 0:
        repuesta = a
    else:
        for i in range(0,b+1):
            contador =0
            contador +=1
            respesta = contador + a
    return respesta
n1 =int (input('ingrese el numero a: '))
n2 =int (input('ingrese el numero b: '))   
resultado = suma (n1,n2)
print('resultado de la suma es: '+resultado)
        

        