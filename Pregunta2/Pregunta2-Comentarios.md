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
por el usuario. Ademas vemos que a su vez la clase Adapter sera intanciado como parte de la funcion manager() para poder 
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
separado, ahora se establece una clase la cual permite crear Cines con los parametros requeridos.
