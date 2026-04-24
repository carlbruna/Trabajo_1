tarifa = 0
usuario = input("Ingresar Tipo de Usuario(Adulto, Estudiante, Adulto Mayor):")
horario = input("Ingrese horario del viaje(Normal, Punta):")
if usuario == "Adulto":
    if horario == "Normal":
        tarifa = tarifa + 790
    else:
        tarifa = tarifa + 890
if usuario == "Estudiante":
    if horario == "Normal":
        tarifa = tarifa + 490
    else:
        tarifa = tarifa + 590
if usuario == "Adulto Mayor":
    if horario == "Normal":
        tarifa = tarifa + 390
    else:
        tarifa = tarifa + 490
print("Usuario:", usuario)
print("Horario del viaje:", horario)
print("La tarifa a pagar es:", tarifa)
print("Gracias por viajar con nosotros")
