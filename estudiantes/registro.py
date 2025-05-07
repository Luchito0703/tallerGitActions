import pandas as pd

csv="estudiantes.csv"

def revisarEstudiantes(csv):
    df = pd.read_csv(csv,delimiter=";")
    notas = (df["nota"])
    validos= []
    for i in range(len(notas)):
        nombre = df["nombre"][i]
        if notas[i] >= 0.0 and notas[i] <= 5.0:
            nota=notas[i]
            validos.append((nombre, nota))
    return validos

def ordenarEstudiantes(estudiantes):
    estudiantes.sort()
    print("Nombre".ljust(30), "Nota") #ljust es para alinear a la izquierda
    print("-" * 35)
    for nombre, nota in estudiantes:
        print(nombre.ljust(30),nota)

def promedioNotas(estudiantes):
    suma = 0
    for nombre, nota in estudiantes:
        suma += nota
    promedio = suma / len(estudiantes)
    return promedio.round(2)
