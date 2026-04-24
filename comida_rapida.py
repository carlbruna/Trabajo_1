total = 0
iva = 0.19

usuario = input("Bienvenido a FoodGood, indíqueme su nombre:")


print("Seleccione un Combo:")
print("Combo\t\t\tNormal\tXL")
print("1-Big Gloton\t\t6.500\t8.900")
print("2-Tocomples Full\t3.000\t4.500")
print("3-Fajitas Taliban\t2.400\t3.200")
print("4-Papas US Love\t\t1.450\t2.400")

combo = int(input("Seleccione:"))

if combo == 1:
    formato = input("Normal o XL:")
    if formato == "Normal":
        sub_total = 6500
        cantidad = int(input("Cuantas:"))
        total = sub_total * cantidad
        
    if formato == "XL":
        sub_total = 8900
        cantidad = int(input("Cuantas:"))
        total = sub_total * cantidad
        
if combo == 2:
    formato = input("Normal o XL:")
    if formato == "Normal":
        sub_total = 3000
        cantidad = int(input("Cuantas:"))
        total = sub_total * cantidad
        
    if formato == "XL":
        sub_total = 4500
        cantidad = int(input("Cuantas:"))
        total = sub_total * cantidad
        
if combo == 3:
    formato = input("Normal o XL:")
    if formato == "Normal":
        sub_total = 2400
        cantidad = int(input("Cuantas:"))
        total = sub_total * cantidad
        
    if formato == "XL":
        sub_total = 3200
        cantidad = int(input("Cuantas:"))
        total = sub_total * cantidad
        
if combo == 4:
    formato = input("Normal o XL:")
    if formato == "Normal":
        sub_total = 1450
        cantidad = int(input("Cuantas:"))
        total = sub_total * cantidad
        
    if formato == "XL":
        sub_total = 2400
        cantidad = int(input("Cuantas:"))
        total = sub_total * cantidad
        
        
bebida = input("Desea Bebidas (S/N):")

if bebida == "S":
    
    print("1-Normal	$1.200")
    print("2-Grande	$2.300")
    print("3-XL		$3.200")
    
    n_bebida = int(input("Seleccione:"))

    if n_bebida == 1:
        cantidad_bebida = int(input("Cuantas:"))
        
        total_bebida = 1200 * cantidad_bebida
        
    if n_bebida == 2:
        cantidad_bebida = int(input("Cuantas:"))
        
        total_bebida = 2300 * cantidad_bebida
        
    if n_bebida == 3:
        cantidad_bebida = int(input("Cuantas:"))
        
        total_bebida = 3200 * cantidad_bebida
    
    total_todo = total + total_bebida
    
    total_iva =  total_todo * iva
                    
    todo = total_todo + total_iva
        
    cantidad_total = cantidad + cantidad_bebida
        
    print(f"Cantidad de Productos: {cantidad_total}")            
    print(f"Total:   ${total_todo}")
    print(f"IVA:         ${round(total_iva)}")
    print("-" * 45)
    print(f"Total:       ${round(todo)}")


else:
    total_iva =  total * iva
                
    todo =  total + total_iva
    
    cantidad_total = cantidad
    
    print(f"Cantidad de Productos: {cantidad_total}")            
    print(f"Total:   ${total}")
    print(f"IVA:         ${round(total_iva)}")
    print("-" * 45)
    print(f"Total:       ${round(todo)}")
    