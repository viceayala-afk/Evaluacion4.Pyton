# ============================================
# Sistema de Gestión de Libros de Biblioteca
# ============================================

# ---------- Funciones del menú ----------

def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("====================================")


def leer_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe ingresar una opción entre 1 y 6.")
        except ValueError:
            print("Debe ingresar un número entero.")


# ---------- Funciones de validación ----------

def validar_titulo(titulo):
    return titulo.strip() != ""


def validar_copias(copias):
    return copias >= 0


def validar_prestamo(prestamo):
    return prestamo > 0


# ---------- Funciones del sistema ----------

def agregar_libro(libros):
    titulo = input("Ingrese el título del libro: ")

    if not validar_titulo(titulo):
        print("Error: El título no puede estar vacío.")
        return

    try:
        copias = int(input("Ingrese la cantidad de copias: "))
    except ValueError:
        print("Error: Las copias deben ser un número entero.")
        return

    if not validar_copias(copias):
        print("Error: Las copias deben ser mayor o igual a cero.")
        return

    try:
        prestamo = int(input("Ingrese el período de préstamo (días): "))
    except ValueError:
        print("Error: El período de préstamo debe ser un número entero.")
        return

    if not validar_prestamo(prestamo):
        print("Error: El período de préstamo debe ser mayor que cero.")
        return

    libro = {
        "titulo": titulo,
        "copias": copias,
        "prestamo": prestamo,
        "disponible": False
    }

    libros.append(libro)
    print("Libro agregado correctamente.")


def buscar_libro(libros, titulo):
    for i in range(len(libros)):
        if libros[i]["titulo"] == titulo:
            return i
    return -1


def actualizar_disponibilidad(libros):
    for libro in libros:
        if libro["copias"] >= 1:
            libro["disponible"] = True
        else:
            libro["disponible"] = False


def mostrar_libros(libros):
    actualizar_disponibilidad(libros)

    if len(libros) == 0:
        print("No hay libros registrados.")
        return

    print("\n=== LISTA DE LIBROS ===")

    for libro in libros:
        print("Título:", libro["titulo"])
        print("Copias:", libro["copias"])
        print("Préstamo:", libro["prestamo"])

        if libro["disponible"]:
            print("Estado: DISPONIBLE")
        else:
            print("Estado: SIN COPIAS")

        print("*" * 45)


# ---------- Programa principal ----------

libros = []

while True:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        agregar_libro(libros)

    elif opcion == 2:
        titulo = input("Ingrese el título a buscar: ")
        posicion = buscar_libro(libros, titulo)

        if posicion != -1:
            libro = libros[posicion]
            print("\nLibro encontrado.")
            print("Posición:", posicion)
            print("Título:", libro["titulo"])
            print("Copias:", libro["copias"])
            print("Préstamo:", libro["prestamo"])
            print("Disponible:", libro["disponible"])
        else:
            print("Libro no encontrado.")

    elif opcion == 3:
        titulo = input("Ingrese el título del libro a eliminar: ")
        posicion = buscar_libro(libros, titulo)

        if posicion != -1:
            del libros[posicion]
            print("Libro eliminado correctamente.")
        else:
            print(f"El libro '{titulo}' no se encuentra registrado.")

    elif opcion == 4:
        actualizar_disponibilidad(libros)
        print("Disponibilidad actualizada correctamente.")

    elif opcion == 5:
        mostrar_libros(libros)

    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break