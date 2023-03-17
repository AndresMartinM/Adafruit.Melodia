# Santiago de Chile 2022 - Andres Martin
# para Adafruit Circuit Playground Bluefruit

import time
from adafruit_circuitplayground.bluefruit import cpb


# datos para el calculo de la escala musical
frecuencia = 432 / 16  #La0
cant_notasA = 12  #escala occidental
notas = []
multiplo = 2 ** (1.0/cant_notasA)

# lectura del archivo con los nombres de las notas
nombreNotas = open('nombreNotas.csv').readlines()[0].split(',')

# funcion que nos sirve para calcular el largo de una lista
def cap(lista):
    cont = 0
    for i in lista:
        cont += 1
    return cont

# calculo de la escala musical
for i in range(80):
    notas = notas + [frecuencia * (multiplo ** i)]

# lectura del erchivo con la melodia
with open('tabla.csv') as f:
    lines = f.readlines()
melodia = lines[0].split(',')
figuras = list(map(int,(lines[1].split(','))))

# asignacion de las notas de la melodia a una lista
notasMelodia = []
for i in range(cap(melodia)-2):
    notasMelodia = notasMelodia + [melodia[i+1]]

print(notasMelodia)# para ver las notas de la melodia en la consola

while True:
    if cpb.button_a:
        for i in range(cap(notasMelodia)+1):
            cpb.start_tone(notas[nombreNotas.index(notasMelodia[i-1])], 1)# se busca el indice de la nota en nombreNotas y se asigna a notas[] para extraer la frecuencia de la nota
            print(notas[nombreNotas.index(notasMelodia[i-1])])# para ver la frecuencia de a nota que va a sonar
            time.sleep(figuras[i]/7)
            cpb.stop_tone()


