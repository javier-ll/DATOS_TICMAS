# Función para calcular promedio
def calcular_promedio(sueldo1,sueldo2,sueldo3):
    promedio=(sueldo1*6+sueldo2*4+sueldo3*2)/12
    return promedio

# Sueldos de Juan en el año
sueldo_enero_junio=300
sueldo_julio_octubre=500
sueldo_noviembre_diciembre=700
# Cálculo de promedio
promedio_matematico=calcular_promedio(sueldo_enero_junio,sueldo_julio_octubre,sueldo_noviembre_diciembre)
print("El promedio del sueldo de Juan calculado matemáticamente es: ",promedio_matematico)
#Definir si el sueldo es bajo, medio o alto
if promedio_matematico<300:
    print("El sueldo de Juan es bajo")
elif 300<=promedio_matematico<=900:
    print("El sueldo de Juan es normal")
else:
    print("El sueldo de Juan es alto")
