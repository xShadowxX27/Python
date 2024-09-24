import limpiar_datos as lp 

lista = lp.crear_lista_diccionarios('inscrip_paes2024.csv')
puntaje = lp.crear_lista_diccionarios_pc('inscrip_paes2024.csv') 

def recopilador_datos():
    disclaimer = "POR FAVOR INGRESA LOS DATOS QUE SE TE SOLICITARAN A CONTINUACION, EN CASO DE NO HABER RENDIDO ALGUNA DE LAS PRUEBAS OPCIONALES, POR FAVOR INGRESA 0"
    print(disclaimer)
    nem = int(input("¿CUAL ES TU PUNTAJE NEM? (OBLIGATORIO) -> "))
    rank = int(input('¿CUAL ES TU PUNTAJE RANKING? (OBLIGATORIO) -> '))
    m1 = int(input("¿CUAL ES TU PUNTAJE EN M1? (OBLIGATORIO) -> "))
    leng = int(input('¿CUAL ES TU PUNTAJE DE LENGUAJE? (OBLIGATORIO) -> '))
    m2 = int(input("¿CUAL ES TU PUNTAJE EN M2? ->"))
    his = int(input("¿CUAL ES TU PUNTAJE DE HISTORIA? ->"))
    cien = int(input("¿CUAL ES TU PUNTAJE DE CIENCIAS? -> "))
    datos_usuario = [nem,rank,m1,leng,m2,his,cien]
    return datos_usuario
        
def puntaje_de_corte():
    global lista
    global puntaje
    cod_carrera = (input("INGRESA EL CODIGO DE TU CARRERA -> "))
    puntajes = []
    for l in puntaje:
        if str(l['TIPO_PREF']) == "REGULAR":
            if (l['COD_CARRERA_PREF']) == cod_carrera:
                if int(l['ESTADO_PREF']) == 24:
                    puntajes.append((l['PTJE_PREF']))
    print(puntajes)
    lista_ordenada = sorted(puntajes)
    print('-------------')
    print(lista_ordenada)
    print('-------------')
    print('EL PUNTAJE DE CORTE DE TU CARRERA ES',lista_ordenada[0])

recopilador_datos()
puntaje_de_corte()



