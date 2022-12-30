def potencia (base,exponente):
    if exponente == 0:
        repuesta = 1
    elif exponente == 1:
        respuesta = base
    else:
        repuesta= base ** exponente
    return repuesta

base = int (input('Ingrese la base de la potencia: '))
exponente = int (input('Ingrese el exponente de la potencia: '))

resultado = potencia(base,exponente)
print('el resultado de la potencia es: ',resultado)