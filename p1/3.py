lista = []

while True:
    nombre = input('Ingrese por favor su nombre (indique no para finalizar): ')
    if nombre.lower()=='no':
        break
    edad = int(input("Ingrese su edad: "))
    lista.append((nombre,edad))

for nombre,edad in lista:
    print(f'su nombre es {nombre} y tienes {edad} años ')
    if edad >= 18:
        print('Eres mayor de edad','\n')
    else: 
        print('eres menor de edad','\n')