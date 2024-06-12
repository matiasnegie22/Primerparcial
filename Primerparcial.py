#Primer Parcial Algoritmos y Estructuras de Datos

#1. Desarrollar una función recursiva que permita listar los elementos de vector/lista de
#manera inversa al que están cargados. Preferentemente la función solo debe tener un
#parámetro que es la lista de elementos. 2. Dada una pila con los datos de dinosaurios resolver lo siguiente actividades:
#a) Contar cuantas especies hay;
#b) Determinar cuantos descubridores distintos hay;
#c) Mostrar todos los dinosaurios que empiecen con T;
#d) Mostrar todos los dinosaurio que pesen menos de 275 Kg
#e) Dejar en una pila aparte todos los dinosaurios que comienzan con A, Q, S;
#3. Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros, colores de sable de luz usados y especie. implementar las funciones
#necesarias para resolver las actividades enumeradas a continuación:
#a) listado ordenado por nombre y por especie;
#b) mostrar toda la información de Ahsoka Tano y Kit Fisto;
#c) mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
#d) mostrar los Jedi de especie humana y twi'lek;
#e) listar todos los Jedi que comienzan con A;
#f) mostrar los Jedi que usaron sable de luz de más de un color;
#g) indicar los Jedi que utilizaron sable de luz amarillo o violeta;
#h) indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.
#i) Mostrar todos los Jedi que tengan el ranking de Grand Master.

class stack


dinosaurios = [
    {
      "nombre": "Tyrannosaurus Rex",
      "especie": "Theropoda",
      "peso": "7000 kg",
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1902
    },
    {
      "nombre": "Triceratops",
      "especie": "Ceratopsidae",
      "peso": "6000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1889
    },
    {
      "nombre": "Velociraptor",
      "especie": "Dromaeosauridae",
      "peso": "15 kg",
      "descubridor": "Henry Fairfield Osborn",
      "ano_descubrimiento": 1924
    },
    {
      "nombre": "Brachiosaurus",
      "especie": "Sauropoda",
      "peso": "56000 kg",
      "descubridor": "Elmer S. Riggs",
      "ano_descubrimiento": 1903
    },
    {
      "nombre": "Stegosaurus",
      "especie": "Stegosauridae",
      "peso": "5000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Spinosaurus",
      "especie": "Spinosauridae",
      "peso": "10000 kg",
      "descubridor": "Ernst Stromer",
      "ano_descubrimiento": 1912
    },
    {
      "nombre": "Allosaurus",
      "especie": "Theropoda",
      "peso": "2000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Apatosaurus",
      "especie": "Sauropoda",
      "peso": "23000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Diplodocus",
      "especie": "Sauropoda",
      "peso": "15000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1878
    },
    {
      "nombre": "Ankylosaurus",
      "especie": "Ankylosauridae",
      "peso": "6000 kg",
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1908
    },
    {
      "nombre": "Parasaurolophus",
      "especie": "Hadrosauridae",
      "peso": "2500 kg",
      "descubridor": "William Parks",
      "ano_descubrimiento": 1922
    },
    {
      "nombre": "Carnotaurus",
      "especie": "Theropoda",
      "peso": "1500 kg",
      "descubridor": "José Bonaparte",
      "ano_descubrimiento": 1985
    },
    {
      "nombre": "Styracosaurus",
      "especie": "Ceratopsidae",
      "peso": "2700 kg",
      "descubridor": "Lawrence Lambe",
      "ano_descubrimiento": 1913
    },
    {
      "nombre": "Therizinosaurus",
      "especie": "Therizinosauridae",
      "peso": "5000 kg",
      "descubridor": "Evgeny Maleev",
      "ano_descubrimiento": 1954
    },
    {
      "nombre": "Pteranodon",
      "especie": "Pterosauria",
      "peso": "25 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1876
    },
    {
      "nombre": "Quetzalcoatlus",
      "especie": "Pterosauria",
      "peso": "200 kg",
      "descubridor": "Douglas A. Lawson",
      "ano_descubrimiento": 1971
    },
    {
      "nombre": "Plesiosaurus",
      "especie": "Plesiosauria",
      "peso": "450 kg",
      "descubridor": "Mary Anning",
      "ano_descubrimiento": 1824
    },
    {
      "nombre": "Mosasaurus",
      "especie": "Mosasauridae",
      "peso": "15000 kg",
      "descubridor": "William Conybeare",
      "ano_descubrimiento": 1829
    },

  ]
Pila_dinosaurio=  stack()
pila=[]
for dinosaurio in dinosaurios:

    Pila_dinosaurio.push(dinosaurio)


#2a

def contarCantidad(pila):
    lista_especies=[]
    while pila.size() > 0:
        if lista_especies.count(pila.on_top()["especie"]) == 0:
            lista_especies.append(pila.on_top()["especie"])
            Pila_dinosaurio.push(pila.pop())
        else:
            Pila_dinosaurio.push(pila.pop())
    return len(lista_especies)

print(contarCantidad(Pila_dinosaurio))




#2c
nombres_T = []
for i in range(pila_dinos.size()):
    if Pila_dinosaurio.on_top()['nombre'].startswith(('T')):
        nombres_T.append(Pila_dinosaurio.on_top()['nombre'])
        Pila_dinosaurio.pop()
    else:
        Pila_dinosaurio.pop()

print(nombres_T)
