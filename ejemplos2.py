import limpiar_datos as lp 

lista=lp.crear_lista_diccionarios('oferta_academica.csv')
# print(list(lista[0].keys()))
# for l in lista:
    # print(l['NOMBRE_UNIVERSIDAD'])

universidades=[]
clave='NOMBRE_CARRERA'

for e in lista[1:]:
    if e[clave] not in universidades:
        universidades.append(e[clave])

for u in universidades:
    print(u)
