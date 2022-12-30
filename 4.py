def factorial (numero):
    resultado=1
    for i in range(numero):
        resultado *= i +1
    return resultado

def factorial1(numero):
    if numero ==0 or numero == 1:
        resultado =1
    else:
        resultado = factorial(numero-1)
    return resultado

numero =int(input('ingrese el numero: '))
print('el resultado no recursivo es: ', factorial(numero) )
print('el resultado recursivo es: ', factorial1(numero) )
