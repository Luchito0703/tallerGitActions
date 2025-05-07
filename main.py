from estudiantes.registro import revisarEstudiantes, ordenarEstudiantes, promedioNotas

def main():
    csv = "estudiantes.csv"
    estudiantesValidos = revisarEstudiantes(csv)
    print("Estudiantes válidos:")
    ordenarEstudiantes(estudiantesValidos)
    print("\n Calculo del promedio de notas:")
    print(promedioNotas(estudiantesValidos))

if __name__ == "__main__":
    main()
