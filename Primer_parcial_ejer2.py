#1. Desarrollar una función recursiva que permita listar los elementos de vector/lista de
#manera inversa al que están cargados. Preferentemente la función solo debe tener un
#parámetro que es la lista de elementos. 2. Dada una pila con los datos de dinosaurios resolver lo siguiente actividades:


def listar_inversa_numeros(lista_n):
    if len(lista_n) == 0 :
        return (0)
    else:
        print(lista_n[-1])
        return(listar_inversa_numeros(lista_n[:-1]))


lista_numero = [1, 2, 3, 4, 5]
print(listar_inversa_numeros(lista_numero))