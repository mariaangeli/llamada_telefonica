# programa para calcular el costo de una llamada telefónica 

# toda llamada que dure 3 minutos o menos tiene un costo de $300
# cada minuto adicional cuesta $50

print("------------------------------------------")
print("------------COSTO DE LLAMADA--------------")
print("------------------------------------------")

# input 
minutos = int(input("ingrese los minutos de la llamda: "))

# processing 

if minutos < 3:
    costo = 300

else:
    costo = (minutos * 50) +300 -150

# output 
print(" el costo de la llamda es: " + str(costo))
