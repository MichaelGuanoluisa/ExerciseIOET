###Funcion para crear una matriz
def createMatrix(n,m):
    matriz = []
    for i in range(n):
        a = [0]*m
        matriz.append(a)
    return matriz
 
 ###Funcion para registrar nombres y horarios
def register (names,days,schedule,n):
    for i in range(n):
        name = input("Ingrese el nombre de la persona a registrar: ")
        names.append(name)
        for j in range(7):
            schedule[i][j] = input("Ingrese horario del dia " + days[j] + ": ")
    
    return schedule, name

print("--------Ejercicio IOET--------")

names = []
days = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']

nameTxt = input("Ingrese nombre del archivo representado por semanas. Ejemplo: 'Semana 1': \n")
file= open(nameTxt+".txt","w")

while True:
    rows = input("Ingrese la cantidad de personas que va a registrar: ")
    try:
        if(int(rows)):
            break
    except ValueError:
        print("Ingresa un número")
        
n = int(rows)
m = 7
schedule = createMatrix(n,m)
register(names,days,schedule,n)

row = 0
initial = 0
cont = 0
while True:
    for i in range(initial,n-1,1):
        for j in range(7):
            if(schedule[row][j]==schedule[i+1][j] and schedule[row][j] != ''):
                cont += 1
        file.write(names[row] + "-" + names[i+1] + ": " + str(cont) + "\n")
        cont = 0  
        
    row = row + 1
    initial += 1
    if(init == n):
        file.close()
        break
