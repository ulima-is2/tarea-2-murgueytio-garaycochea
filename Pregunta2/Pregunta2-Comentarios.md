## Pregunta 2 - Comentarios
```python
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
```

Este es un metodo que permite etablecer el patron de adaptador (Adapter) que se encarga de manejar la opcion seleccionada
por el usuario. Además vemos que a su vez la clase Adapter será intanciado como parte de la funcion manager() para poder 
establecer un patron de fachada:  

```python
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
```

Por otro lado el codigo general para el cine:

```python
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

```

Se puede observar un primer acercamiento al patron Factory ya que a diferencia del codigo inicial donde se creaba cada cine por 
separado, ahora se establece una clase, la cual permite crear Cines con los parametros requeridos.

```python
class Opcion:
    datos = BD()

class Opcion1(Opcion):
    def mostrar(self):
        self.datos.cines.listarCines()

class Opcion2(Opcion):
    opcion1 = Opcion1()
    def mostrar(self):
        self.opcion1.mostrar()
        cine = input('Primero elija un cine: ')
        if cine == '1':
            cine = self.datos.cines.obtenerCine(int(cine) - 1)
        elif cine == '2':
            cine = self.datos.cines.obtenerCine(int(cine) - 1)
        else:
            print("Se ingresó un valor no válido")
        cine.listarPeliculas()
        return cine

class Opcion3(Opcion):
    opcion2 = Opcion2()
    def mostrar(self):
        cines = self.opcion2.mostrar()
        pela = input("Elija la pelicula que quiere ver: ")
        entrada = cines.listarFunciones(pela)
        entrada.guardar_entrada(entrada.pelicula_id, entrada.funcion, entrada.cantidad)

```

Por último, se puede observar un patrón básico de Composite donde la clase Opcion hereda la variable 'datos' a 'Opcion1'.'Opcion2' y 'Opcion3' para no instanciar nuevamente la clase BD() y logre que el código sea más óptimo y rápido. Ayudó sobretodo para la implementación de la bd con SQLite en la pregunta3.