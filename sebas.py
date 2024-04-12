def validarf(msj):
    intentos = 0
    while True:
        try:
            entrada = float(input(msj))
            return entrada
        except ValueError:
            print("Ingrese solo números. Inténtelo nuevamente.")
            intentos += 1
            if intentos >= 3:
                print("Ya no tienes más intentos.")
                break
def validar(msj):
    while True:
        try:
            entrada = int(input(msj))
            return entrada
        except:
            print("Ingrese solo numeros enteros. Intentelo nuevamente!!") 