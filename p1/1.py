'''

Escriba un programa que encuentre el valor aproximado del n´umero de euler en
base a la suma infinita de la Ecuaci´on 1. El usuario debe ingresar el n´umero de
elementos usados en la aproximaci´on. Por ejemplo, si se ingresa 3: $e= 1/0! + 1/(1! + 1/2! + ...$
$
'''
number = int(input ("Ingrese el número para realizar la aproximación: "))
factorial=1
eulr=1
for i in range(1,number):
  factorial *= i
  eulr += 1/factorial
  resultado=eulr
print("e es aproximadamente: " , resultado)