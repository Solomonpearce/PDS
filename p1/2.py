def aproximacion(number):
  factorial=1
  eulr=1
  for i in range(1,number):
    factorial *=i
    eulr += 1/factorial

    resultado = eulr
  return resultado
  

number=int(input("ingrese el numero con el cual desea la aproximaciòn: "))

print(aproximacion(number))

3