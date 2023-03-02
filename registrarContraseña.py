contraseñasIguales = False

while contraseñasIguales == False:
    contraseña1 = input("Digite su contraseña: ")
    contraseña2 = input("Digite nuevamente su contraseña: ")
    if contraseña1 == contraseña2:
        contraseñasIguales = True
    else:
        print("Las contraseñas son diferentes. Por favor ingresela nuevamente")
print("Su registro se ha realizado correctamente")