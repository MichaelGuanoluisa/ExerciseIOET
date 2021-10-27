{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9075f282",
   "metadata": {},
   "outputs": [],
   "source": [
    "def createMatrix(n,m):\n",
    "    matriz = []\n",
    "    for i in range(n):\n",
    "        a = [0]*m\n",
    "        matriz.append(a)\n",
    "    return matriz\n",
    " \n",
    "def register (names,days,schedule,n):\n",
    "    for i in range(n):\n",
    "        name = input(\"Ingrese el nombre de la persona a registrar: \")\n",
    "        names.append(name)\n",
    "        for j in range(7):\n",
    "            schedule[i][j] = input(\"Ingrese horario del dia \" + days[j] + \": \")\n",
    "    \n",
    "    return schedule, name\n",
    "\n",
    "print(\"--------Ejercicio IOET--------\")\n",
    "\n",
    "names = []\n",
    "days = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']\n",
    "\n",
    "nameTxt = input(\"Ingrese nombre del archivo representado por semanas. Ejemplo: 'Semana 1': \\n\")\n",
    "file= open(nameTxt+\".txt\",\"w\")\n",
    "\n",
    "rows = input(\"Ingrese la cantidad de personas que va a registrar: \")\n",
    "n = int(rows)\n",
    "m = 7\n",
    "schedule = createMatrix(n,m)\n",
    "register(names,days,schedule,n)\n",
    "\n",
    "row = 0\n",
    "initial = 0\n",
    "cont = 0\n",
    "while True:\n",
    "    for i in range(initial,n-1,1):\n",
    "        for j in range(7):\n",
    "            if(schedule[row][j]==schedule[i+1][j] and schedule[row][j] != ''):\n",
    "                cont += 1\n",
    "        file.write(names[row] + \"-\" + names[i+1] + \": \" + str(cont) + \"\\n\")\n",
    "        cont = 0  \n",
    "        \n",
    "    row = row + 1\n",
    "    initial += 1\n",
    "    if(init == n):\n",
    "        file.close()\n",
    "        break\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
