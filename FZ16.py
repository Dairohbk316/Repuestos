
repuestos = [] # creo lista vacia

def agregar_repuestos(repuestos):
    refaccion= input('Ingrese refaccion ') # Creo los valores del diccionario como variables que puede llebar el usuario
    fecha = int(input('Ingrese fecha '))
    km = float(input('Ingrese kilometraje '))
    valor = float(input('ingrese valor repuesto '))

    autopartes= {
        'refaccion': refaccion, # creo el diccionario y adjunto a la clave el valor del usuario
        'fecha' : fecha,
        'km' : km,
        'valor': valor
    }

    repuestos.append(autopartes) #Agrego a la lista repuestos el diccionario refacciones
    print('repuesto guardado con exito')

def listar_repuestos(repuestos):
    for i in repuestos:
        print(i)

def lista_refacciones(repuestos):
    for indice, recambio in enumerate(repuestos):
        print('{refaccion} | {fecha} | {km} | {valor}'.format(uid=indice,
                                                              refaccion=autopartes['refaccion'],
                                                              fecha=autopartes['fecha'],
                                                              km=autopartes['km'],
                                                              valor=autopartes['valor']))        

if __name__ == '__main__':

    while True:

        option = input('Desea ingresar repuesto a la base s[si o no] ')

        if option == 'si':
            agregar_repuestos(repuestos)
            
            lista_refacciones(repuestos)
            
        elif option == 'no':
            listar_repuestos(repuestos)
            break
        else:
            print('ingrese una autoparte valida')  



