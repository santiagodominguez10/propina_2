import math

def calculadora_propinas():
    print("Bienvenido a la calculadora de propinas.")
    
    # Solicitar al usuario el monto total de la factura y el porcentaje de propina
    total_factura = float(input("Ingresa el monto total de la factura: $"))
    porcentaje_propina = float(input("Ingresa el porcentaje de propina que deseas dar: "))
    
    # Calcular el monto de propina y el total a pagar
    monto_propina = total_factura * (porcentaje_propina / 100)
    total_pagar = total_factura + monto_propina
    
    # Solicitar al usuario el número de personas para dividir la cuenta
    num_personas = int(input("Ingresa el número de personas para dividir la cuenta: "))
    
    # Calcular el monto a pagar por cada persona
    monto_por_persona = total_pagar / num_personas
    
    # Mostrar los resultados al usuario
    print(f"\nMonto de propina: ${monto_propina:.2f}")
    print(f"Total a pagar: ${total_pagar:.2f}")
    print(f"Monto a pagar por cada persona: ${monto_por_persona:.2f}")

    
calculadora_propinas()
