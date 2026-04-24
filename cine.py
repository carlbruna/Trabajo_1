print("Bienvenido Al Cine")

usuario = input("Ingrese Nombre de Usuario:")

clave = input("Ingrese Contraseña:")

tipo_publico = input("Indique el tipo de público (Normal, Estudiante, Adulto Mayor):")

if tipo_publico == "Normal":
    tipo_sala = input("Tipo de Sala (Normal, 3D, 4DX):")

    cantidad_ticket = int(input("Ingrese Cantidad de Entradas:"))