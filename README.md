# Exercise IOET
Ejercicio del proceso de selección

# Resolución:
El ejercicio fue resuelto con lenguaje de programación python, el enfoque en el que me centré para resolver el problema fue crear una matriz para almacenar los horarios y de esa forma permitirme recorrer las filas, comparando los valores de cada columna. Cada columna representa un dia a la semana, es por eso que la matriz tiene una dimención de 7 columnas, el numero de filas es un valor que va a depender de la cantidad de personas que se registren, este valor de la cantidad de personas lo debe ingresar el usuario por teclado teniendo una comprobación de que sea un entero. Los nombres se almacenan en una lista, la misma que los indices me permiten saber de quien es el registro de horarios por filas, es decir ese mismo indice de la lista es el indice de filas en la matriz. Para finalizar úse dos for y dos variables que me permitieron recorrer la matriz buscando la frecuencia con la que coincidieron los empleados, y esto se guarda en un archivo txt.
El código se encuentra estructurado de la siguiente forma:
1. función para crear una matriz.
    En esta función se recibe dos valores las filas y las columnas que pertenecen a la matriz que se creará, con el uso de un for se recorre el numero de filas creando listas con     el numero de columnas y al final agregando estas listas como filas en la matriz.
2. función para el registro de nombres y horarios.
    Usando ciclo for para recorrer numeros de filas y columnas para almacenar los horarios en una matriz.
3. declaración de vectores.
4. crear documento txt.
5. ciclo while con comprobación de dato ingresado por teclado.
6. declaración de variables de matriz y llamada a las funciones.
7. ciclo while con proceso de cálculo de coincidencia entre horarios de los empleados.

Usé la herramienta llamada jupyter notebook para tener un entorno de desarrollo en el cual escribir el código del programa. Aquí en el GitHub podrán encontrar dos archivos uno .ipynb que es el tipo de archivo que genera jupyter notebook, y además un archivo tipo .py. Para poder ejecutar los scripts, el primero mencionado se lo puede ejecutar en jupyter notebook y el segundo se lo puede ejecutar en una terminal de windows simplemente arrastrando y soltando el archivoen la terminal.
