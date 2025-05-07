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

print(revisarEstudiantes(csv))