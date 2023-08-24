
repuestos = [] # creo lista vacia

def agregar_repuestos(repuestos):
    refaccion= input('Ingrese refaccion ') # Creo los valores del diccionario como variables que puede llebar el usuario
    fecha = int(input('Ingrese fecha '))
    km = float(input('Ingrese kilometraje '))
    valor = float(input('ingrese valor repuesto '))

    refacciones = {
        'refaccion': refaccion, # creo el diccionario y adjunto a la clave el valor del usuario
        'fecha' : fecha,
        'km' : km,
        'valor': valor
    }

    repuestos.append(refacciones) #Agrego a la lista repuestos el diccionario refacciones
    print('repuesto guradado con exito')

def listar_repuestos(repuestos):
    for i in repuestos:
        print(i)

if __name__ == '__main__':

    while True:

        option = input('Desea ingresar repuesto a la base s[si o no] ')

        if option == 'si':
            agregar_repuestos(repuestos)
            listar_repuestos(repuestos)
            
        elif option == 'si':
            break
        else:
            print('ingrese una autoparte valida')  



