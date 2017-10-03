import sqlite3

conn = sqlite3.connect('Q3.db')
cursor = conn.cursor()

class Cine:
    def __init__(self, id_cine,nombre):
        self.id_cine = id_cine
        self.nombre = nombre
        self.listaPeliculas = []

    def agregarPelicula(self, pelicula):
        if self.id_cine==1:
            self.listaPeliculas.append(pelicula)
        elif self.id_cine==2:
            self.listaPeliculas.append(pelicula)

    def listarPeliculas(self):
        print('\n********************')
        for pelicula in self.listaPeliculas:
            print("{}. {}".format(pelicula.id, pelicula.nombre))
        print('********************\n')
        return self.listaPeliculas


    def listarFunciones(self, pelicula_id):
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
    def __init__(self, idPelicula,nombrePelicula):
        self.nombrePelicula = nombrePelicula
        self.idPelicula=idPelicula

class Funcion:
    def __init__(self):
        pass

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
        self.sqlito = SQL()
        self.sqlito.limpiarSQL()
        self.sqlito.iniciarSQL()
        
        cineStark = Cine(1,"CineStark")
        cinePlaneta = Cine(2, "CinePlaneta")
        self.sqlito.insertarCine(cineStark)
        self.sqlito.insertarCine(cinePlaneta)

        pDesaparecido=Pelicula(1, 'Desaparecido')
        pPulpo=Pelicula(2,'Deep El Pulpo')
        pIT=Pelicula(3,'IT')
        pHora=Pelicula(4,'La Hora Final')

        self.sqlito.agregarPelicula(pDesaparecido)
        self.sqlito.agregarPelicula(pPulpo)
        self.sqlito.agregarPelicula(pIT)
        self.sqlito.agregarPelicula(pHora)

        self.sqlito.agregarPeliculaxCine(1,pDesaparecido,cineStark)
        self.sqlito.agregarPeliculaxCine(2,pPulpo, cineStark)
        self.sqlito.agregarPeliculaxCine(1,pIT, cinePlaneta)
        self.sqlito.agregarPeliculaxCine(2,pHora, cinePlaneta)
        self.sqlito.agregarPeliculaxCine(3,pDesaparecido, cinePlaneta)
        self.sqlito.agregarPeliculaxCine(4,pPulpo, cinePlaneta)

        self.sqlito.agregarFunciones(['21:00', '23:00'],cineStark,pDesaparecido)
        self.sqlito.agregarFunciones(['16:00', '20:00'],cineStark,pPulpo)
        self.sqlito.agregarFunciones(['20:00', '23:00'],cinePlaneta,pIT)
        self.sqlito.agregarFunciones(['16:00'],cinePlaneta,pHora)
        self.sqlito.agregarFunciones(['19:00', '20:30', '22:00'],cinePlaneta,pDesaparecido)
        self.sqlito.agregarFunciones(['21:00'],cinePlaneta,pPulpo)

        print('Datos insertados con éxito')
        self.cines = Cines([cineStark,cinePlaneta])

class SQL:

    def iniciarSQL(self):
        cursor.execute('''CREATE TABLE IF NOT EXISTS CINE (idCine integer, nombreCine text)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS PELICULA (idPelicula integer, nombrePelicula text)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS CARTELERA (id integer, nombrePelicula text,nombreCine text)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS FUNCION (idFuncion,horario text, idCine integer, idPelicula text)''')
        conn.commit()

    def limpiarSQL(self):
        cursor.execute("DROP TABLE IF EXISTS CINE")
        cursor.execute("DROP TABLE IF EXISTS PELICULA")
        cursor.execute("DROP TABLE IF EXISTS CARTELERA")
        cursor.execute("DROP TABLE IF EXISTS FUNCION")
        conn.commit()

    def insertarCine(self,cine):
        cursor.execute("INSERT INTO CINE (idCine, nombreCine) VALUES (?,?)",
                       (cine.id_cine, cine.nombre))
        conn.commit()

    def agregarPelicula(self,pelicula):
        cursor.execute("INSERT INTO PELICULA (idPelicula, nombrePelicula) VALUES (?,?)",
                       (pelicula.idPelicula, pelicula.nombrePelicula))
        conn.commit()

    def agregarPeliculaxCine(self, id,pelicula,cine):
        cursor.execute("INSERT INTO CARTELERA (id, nombrePelicula,nombreCine) VALUES (?,?,?)",
                       (id,pelicula.nombrePelicula, cine.nombre))
        conn.commit()


    def agregarFunciones(self,horarios,cine,pelicula,):
        for index,hora in enumerate(horarios):
            cursor.execute("INSERT INTO FUNCION (idFuncion,horario, idCine, idPelicula) VALUES (?,?,?,?)",
                           (index,hora,cine.id_cine,pelicula.idPelicula))
            conn.commit()



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
        cine.listarPeliculas()
        return cine

class Opcion3:
    datos = BD()
    opcion2= Opcion2()
    def mostrar(self):
        cines=self.opcion2.mostrar()
        pela=input("Elija la pelicula que quiere ver: ")
        entrada=cines.listarFunciones(pela)
        entrada.guardar_entrada(entrada.pelicula_id,entrada.funcion,entrada.cantidad)

class Salir():
    def mostrar(self):
        print('Finalizado')


def manager():
    BD()

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
