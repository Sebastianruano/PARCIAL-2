from sebas import *         # Importa todas las funciones y variables definidas en el módulo sebas

contAc = 0    # Inicializa un contador para el número de pacientes ingresados
info_pacientes = {}     # Crea un diccionario para almacenar la información de los pacientes
# Definición de rangos para los valores de LH según el género y la edad
rango_mujer_ant_menopausia = (5, 25)
rango_mujer_post_menopausia = (14.2, 52.3)
rango_mujer_joven = (0, 5)
rango_hombre_adulto = (1.8, 8.6)
rango_hombre_joven = (1, 1.8)

def obtener_diagnostico(resultado_lh, genero):
    if genero == "mujer":                                   # Verifica en qué rango se encuentra el resultado de LH y devuelve el diagnóstico correspondiente
        if rango_mujer_ant_menopausia[0] <= resultado_lh <= rango_mujer_ant_menopausia[1]:
            return "Normal (antes de la menopausia)"
        elif rango_mujer_post_menopausia[0] <= resultado_lh <= rango_mujer_post_menopausia[1]:
            return "Normal (después de la menopausia)"                    
        elif rango_mujer_joven[0] <= resultado_lh <= rango_mujer_joven[1]:
            return "Normal (entre 0 y 18 años)"
        else:
            return "Fuera de los rangos normales"
    elif genero == "hombre":
        if rango_hombre_adulto[0] <= resultado_lh <= rango_hombre_adulto[1]:
            return "Normal (mayores de 18 años)"
        elif rango_hombre_joven[0] <= resultado_lh <= rango_hombre_joven[1]:
            return "Normal (entre 0 y 18 años)"
        else:
            return "Fuera de los rangos normales"
    else:
        return "Género no válido"
# Función para ingresar la información de un nuevo paciente
def ingresar_paciente(contAc):
    Nombre = input("Nombre del paciente: ")
    fecha = int(validarf("Fecha de nacimiento (YYYY-MM-DD): "))
    documento = validarf("Número de cédula: ")
    genero = input("Género (1/mujer--2/hombre): ")
    if genero == "1":
        genero = "mujer"
    elif genero == "2":
        genero = "hombre"
    else:
        print("Opción no válida. Se asignará género no válido.")
        genero = "no válido"

    resultado = validarf("Resultado de LH (UI/L)")
    print("\nSeleccione la EPS del paciente:")
    eps_options = ["Sura", "Coomeva", "Medimas", "IPS Universitaria", "Salud Total"]
    for index, eps in enumerate(eps_options, start=1): # Bucle for para iterar sobre las opciones de EPS
        # Imprime el índice y la opción de EPS utilizando una f-string
        print(f"{index}. {eps}")

    opcion_eps = validar("\nIngrese el número de su EPS: ")
    if 1 <= opcion_eps <= 5:          # Verifica si la opción ingresada está dentro del rango válido
        eps = eps_options[opcion_eps - 1] # Asigna la EPS seleccionada a la variable eps utilizando el índice ingresado
    else:
        print("Opción no válida. Se asignará EPS-SISBEN.")
        eps = "SISBEN"
    
    diagnostico = obtener_diagnostico(resultado, genero)

    codigo = f"EPS-{eps}-{contAc+1}"
    print(f"El paciente {Nombre}, identificado con cédula {documento}, ha sido ingresado exitosamente con el código {codigo} y su diagnóstico es {diagnostico}.")

    info_pacientes[documento] = [Nombre, codigo, fecha, diagnostico, genero, eps]

    return documento, info_pacientes[documento]

while True: # iniciamos con un Bucle infinito para el menú principal
    print("========================\n1.-INGRESAR UN PACIENTE-.\n2.--Informe de afiliación.\n3.--Borrar paciente\n4.--Salir")
    entrada = validar("\nIngrese 1, 2, 3 o 4 según requiera: ")
    if entrada == 1:  # Opción para ingresar un nuevo paciente
        contAc += 1   #aumenta un paciente
        documento, datos_paciente = ingresar_paciente(contAc)
        info_pacientes[documento] = datos_paciente            #llamo la funcion 
        
    elif entrada == 2:  # Opción para generar informe de afiliación
        print("========================\n1.-Ver cantidad de pacientes menores de 10-.\n2.-Ver cantidad de pacientes mayores de 60-")
        entrada2 = validar("\nIngrese 1, 2 según requiera: ")
        if entrada2 == 1:
            from datetime import datetime
            hoy = datetime.now()
            cantidad_menores_10 = sum(1 for paciente in info_pacientes.values() if (hoy.year - int(paciente[2][:4])) < 10)
            print("Cantidad de pacientes menores de 10 años:", cantidad_menores_10)
        elif entrada2 == 2:
            from datetime import datetime
            hoy = datetime.now()
            cantidad_mayores_60 = sum(1 for paciente in info_pacientes.values() if (hoy.year - int(paciente[2][:4])) > 60)
            print("Cantidad de pacientes mayores de 60 años:", cantidad_mayores_60)
        else:
            print("Opción no válida. Por favor, ingrese 1 o 2.")
    elif entrada == 3: #aqui borramos con la cedula los ya registrados
        eliminar = validarf("Ingrese el documento del paciente que desea eliminar: ")
        if eliminar in info_pacientes:   #buscamos en el diccionario y eliminamos
            del info_pacientes[eliminar]
            print("Paciente eliminado correctamente.")
        else:
            print("El documento del paciente no existe.")
        
    elif entrada == 4:
        print("Saliendo del sistema.")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")