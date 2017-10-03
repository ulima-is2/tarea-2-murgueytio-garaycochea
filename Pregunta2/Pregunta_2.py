
class Cine:
    def __init__(self, id_cine,nombre):
        self.id_cine = id_cine
        self.nombre = nombre
        self.listaPeliculas = []

    def agregarPelicula(self, pelicula):
        if self.id_cine==1:
            if pelicula.nombre=='Desaparecido':
                pelicula.funciones =['21:00', '23:00']
            elif pelicula.nombre=='Deep El Pulpo':
                pelicula.funciones = ['16:00', '20:00']
            self.listaPeliculas.append(pelicula)
        elif self.id_cine==2:
            if pelicula.nombre=='Desaparecido':
                pelicula.funciones = ['20:00', '23:00']
            elif pelicula.nombre=='Deep El Pulpo':
                pelicula.funciones = ['16:00']
            elif pelicula.nombre == 'IT':
                pelicula.funciones = ['19:00', '20:30', '22:00']
            elif pelicula.nombre == 'La Hora Final':
                pelicula.funciones = ['21:00']
            self.listaPeliculas.append(pelicula)

    def listar_peliculas(self):
        print('\n********************')
        for pelicula in self.listaPeliculas:
            print("{}. {}".format(pelicula.id, pelicula.nombre))
        print('********************\n')
        return self.listaPeliculas


    def listar_funciones(self, pelicula_id):
        print('Ahora elija la función (debe ingresar el formato hh:mm): ')
        for funcion in self.listaPeliculas[int(pelicula_id) - 1].funciones:
            print('Función: {}'.format(funcion))
        _funcion = input('Funcion: ')
        _cantEnt = input('Ingrese cantidad de entradas: ')

        return Entrada(pelicula_id,_funcion,_cantEnt)


class Entrada:
    def __init__(self, pelicula_id, funcion, cantidad):
        self.pelicula_id = pelicula_id
        self.funcion = funcion
        self.cantidad = cantidad

    def guardar_entrada(self, pelicula_id,funcion,cantidad):
        print('\n***********************************')
        print('{} boletos comprados para la función de {}'.format(self.cantidad,funcion))
        print('***********************************\n')

class Pelicula:
    def __init__(self,  nombre,id):
        self.nombre = nombre
        self.id=id

class Cines:
    def __init__(self, listaCines):
        self.cines = listaCines

    def obtenerCine(self, id):
        return self.cines[id]

    def listarCines(self):
        print('\n********************')
        for cine in self.cines:
            print("{}: {}".format(cine.id_cine, cine.nombre))
        print('********************\n')


def menu():
    print('Ingrese la opción que desea realizar')
    print('(1) Listar cines')
    print('(2) Listar cartelera')
    print('(3) Comprar entrada')
    print('(0) Salir')
    return input('Opción: ')


class BD:
    def __init__(self):
        cineStark = Cine(1,"CineStark")
        cineStark.agregarPelicula(Pelicula('Desaparecido',1))
        cineStark.agregarPelicula(Pelicula('Deep El Pulpo',2))

        cinePlaneta = Cine(2,"CinePlaneta")
        cinePlaneta.agregarPelicula(Pelicula('IT',1))
        cinePlaneta.agregarPelicula(Pelicula('La Hora Final',2))
        cinePlaneta.agregarPelicula(Pelicula('Desaparecido',3))
        cinePlaneta.agregarPelicula(Pelicula('Deep El Pulpo',4))

        self.cines = Cines([cineStark,cinePlaneta])


class Adapter:
    def obtener_adapter(self, opcion):
        if opcion == '1':
            return Opcion1()
        elif opcion == '2':
            return Opcion2()
        elif opcion == '3':
            return Opcion3()
        elif opcion == '0':
            return Salir()

class Opcion1:
    datos = BD()
    def mostrar(self):
        self.datos.cines.listarCines()


class Opcion2:
    datos = BD()
    opcion1 = Opcion1()
    def mostrar(self):
        self.opcion1.mostrar()
        cine = input('Primero elija un cine: ')
        if cine == '1':
            cine = self.datos.cines.obtenerCine(int(cine)-1)
        elif cine == '2':
            cine = self.datos.cines.obtenerCine(int(cine) - 1)
        else:
            print("Se ingresó un valor no válido")
        cine.listar_peliculas()
        return cine

class Opcion3:
    datos = BD()
    opcion2= Opcion2()
    def mostrar(self):
        cines=self.opcion2.mostrar()
        pela=input("Elija la pelicula que quiere ver: ")
        entrada=cines.listar_funciones(pela)
        entrada.guardar_entrada(entrada.pelicula_id,entrada.funcion,entrada.cantidad)

class Salir():
    def mostrar(self):
        print('Finalizado')


def manager():
    flag = True
    while flag:
        opcion = menu()
        adapter=Adapter()
        modelo=adapter.obtener_adapter(opcion)
        modelo.mostrar()
        if opcion=='0':
            flag=False

def main():
   manager()

if __name__ == '__main__':
    main()
