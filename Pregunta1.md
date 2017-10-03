# Pregunta 1

## Open - Close:
Se entiende por poder extender el comportamiento de una entidad sin modificar su codigo fuente. En este caso los cines (CineStark 
y Cine Planeta) son entidades que usan funciones (listar_peliculas, listar_funciones, guardar_entrada) que podrian ser heredadas
para evitar manipularlas individualmente por cada cine. 

---

## Single Responsability:
Se entiende por individualizar y encapsular las funcionalidades. En este caso se puede observar que el Main se encarga de realizar
la logica con los inputs requeridos. Estas operaciones deberian estar definidas previamente y luego llamadas en el Main. De 
esta manera tendriamos funciones individuales que se encargen de una funcionalidad especifica.

---

## Interface Segregation:
Se entiende por segregar funcionaliades que no sean estrictamente necesarias. En este caso, y de forma similar al principio
open-close, se debe abstraer las funcionalidades. Existe la posibilidad de que no se separe entradas para un cine por lo que
esta funcionalidad debe abstraerse y solo invocarse de ser necesaria. 
