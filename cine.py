print("Bienvenido Al Cine")

iva = 0.19

usuario = input("Ingrese Nombre de Usuario:")

clave = input("Ingrese Contraseña:")

tipo_publico = input("Indique el tipo de público (Normal, Estudiante, Adulto Mayor):")

if tipo_publico == "Normal":
    tipo_sala = input("Tipo de Sala (Normal, 3D, 4DX):")
    
    if tipo_sala == "Normal":
        cantidad_ticket = int(input("Ingrese Cantidad de Entradas:"))
        total_entradas = 5600 * cantidad_ticket
                
        total_iva = total_entradas * iva
                
        total = total_entradas + total_iva
                
        print(f"Sub total:   ${total_entradas}")
        print(f"IVA:         ${round(total_iva)}")
        print("-" * 45)
        print(f"Total:       ${round(total)}")
        
    if tipo_sala == "3D":
        cantidad_ticket = int(input("Ingrese Cantidad de Entradas:"))
        total_entradas = 7800 * cantidad_ticket
                
        total_iva = total_entradas * iva
                
        total = total_entradas + total_iva
                
        print(f"Sub total:   ${total_entradas}")
        print(f"IVA:         ${round(total_iva)}")
        print("-" * 45)
        print(f"Total:       ${round(total)}")
        
    if tipo_sala == "4DX":
        cantidad_ticket = int(input("Ingrese Cantidad de Entradas:"))
        total_entradas = 12000 * cantidad_ticket
                
        total_iva = total_entradas * iva
                
        total = total_entradas + total_iva
                
        print(f"Sub total:   ${total_entradas}")
        print(f"IVA:         ${round(total_iva)}")
        print("-" * 45)
        print(f"Total:       ${round(total)}")
        
if tipo_publico == "Estudiante":
    tipo_sala = input("Tipo de Sala (Normal, 3D, 4DX):")
    
    if tipo_sala == "Normal":
        cantidad_ticket = int(input("Ingrese Cantidad de Entradas:"))
        total_entradas = 3400 * cantidad_ticket
                
        total_iva = total_entradas * iva
                
        total = total_entradas + total_iva
                
        print(f"Sub total:   ${total_entradas}")
        print(f"IVA:         ${round(total_iva)}")
        print("-" * 45)
        print(f"Total:       ${round(total)}")
        
    if tipo_sala == "3D":
        cantidad_ticket = int(input("Ingrese Cantidad de Entradas:"))
        total_entradas = 4800 * cantidad_ticket
                
        total_iva = total_entradas * iva
                
        total = total_entradas + total_iva
                
        print(f"Sub total:   ${total_entradas}")
        print(f"IVA:         ${round(total_iva)}")
        print("-" * 45)
        print(f"Total:       ${round(total)}")
        
    if tipo_sala == "4DX":
        cantidad_ticket = int(input("Ingrese Cantidad de Entradas:"))
        total_entradas = 7000 * cantidad_ticket
                
        total_iva = total_entradas * iva
                
        total = total_entradas + total_iva
                
        print(f"Sub total:   ${total_entradas}")
        print(f"IVA:         ${round(total_iva)}")
        print("-" * 45)
        print(f"Total:       ${round(total)}")
        
if tipo_publico == "Adulto Mayor":
    tipo_sala = input("Tipo de Sala (Normal, 3D, 4DX):")
    
    if tipo_sala == "Normal":
        cantidad_ticket = int(input("Ingrese Cantidad de Entradas:"))
        total_entradas = 2500 * cantidad_ticket
                
        total_iva = total_entradas * iva
                
        total = total_entradas + total_iva
                
        print(f"Sub total:   ${total_entradas}")
        print(f"IVA:         ${round(total_iva)}")
        print("-" * 45)
        print(f"Total:       ${round(total)}")
        
    if tipo_sala == "3D":
        cantidad_ticket = int(input("Ingrese Cantidad de Entradas:"))
        total_entradas = 3500 * cantidad_ticket
                
        total_iva = total_entradas * iva
                
        total = total_entradas + total_iva
                
        print(f"Sub total:   ${total_entradas}")
        print(f"IVA:         ${round(total_iva)}")
        print("-" * 45)
        print(f"Total:       ${round(total)}")
        
    if tipo_sala == "4DX":
        cantidad_ticket = int(input("Ingrese Cantidad de Entradas:"))
        total_entradas = 4800 * cantidad_ticket
                
        total_iva = total_entradas * iva
                
        total = total_entradas + total_iva
                
        print(f"Sub total:   ${total_entradas}")
        print(f"IVA:         ${round(total_iva)}")
        print("-" * 45)
        print(f"Total:       ${round(total)}")
        


    
# elif tipo_publico == "3D":
#     tipo_sala = input("Tipo de Sala (Normal, 3D, 4DX):")
    
# if tipo_sala == "Normal":
#     cantidad_ticket = int(input("Ingrese Cantidad de Entradas:"))
#     total_entradas = 5600 * cantidad_ticket
                
#     total_iva = total_entradas * iva
                
#     total = total_entradas + total_iva
                
#     print(f"Sub total:   ${total_entradas}")
#     print(f"IVA:         ${round(total_iva)}")
#     print("-" * 45)
#     print(f"Total:       ${round(total)}")

            
