def fibonacci (numero):
    if numero==0:
        respuesta =0
    else:
        n1=0
        n2=1
        for i in range(1,numero):
            n3 = n1 + n2 
            n1 =n2
            n2 =n3
            respuesta = n2
    return respuesta

def fibonacci1(numero):
    if numero == 0 or numero == 1:
        respuesta = numero
    else:
        respuesta = fibonacci1(numero-1) + fibonacci1(numero-2)
    return respuesta

numero =int(input('ingrese el numero: '))
print('el resultado no recursivo es: ', fibonacci(numero) )
print('el resultado recursivo es: ', fibonacci1(numero) )