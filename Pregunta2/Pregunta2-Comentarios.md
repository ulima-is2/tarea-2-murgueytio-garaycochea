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

