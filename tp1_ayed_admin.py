
# Declarativa de variables generales
"""
usuario_ingresado, contrasena_ingresada: string
intentos: integer
opcion: integer
nombre_aerolinea, codigo_iata, descripcion, codigo_pais, continuar: string
cant_arg, cant_chi, cant_bra: integer
"""

import getpass

def cartel():
    print("🔧 En construcción...")

def crear_aerolineas():
    cant_arg = 0
    cant_chi = 0
    cant_bra = 0
    continuar = "si"

    while continuar.lower() == "si":
        print("\n--- CARGA DE AEROLÍNEA ---")

        nombre_aerolinea = input("Nombre de la Aerolínea: ")

        codigo_iata = input("Código IATA (máx 3 caracteres): ")
        while len(codigo_iata) > 3:
            codigo_iata = input("Inválido. Ingrese un código IATA de hasta 3 caracteres: ")

        descripcion = input("Descripción: ")

        codigo_pais = input("Código de país (ARG / CHI / BRA): ").upper()
        while codigo_pais not in ["ARG", "CHI", "BRA"]:
            codigo_pais = input("Inválido. Ingrese ARG, CHI o BRA: ").upper()

        if codigo_pais == "ARG":
            cant_arg += 1
        elif codigo_pais == "CHI":
            cant_chi += 1
        elif codigo_pais == "BRA":
            cant_bra += 1

        continuar = input("¿Desea cargar otra aerolínea? (si / no): ")

    # Mostrar estadísticas
    print("\n📊 ESTADÍSTICAS DE AEROLÍNEAS CARGADAS")
    print("Argentina (ARG):", cant_arg)
    print("Chile (CHI):", cant_chi)
    print("Brasil (BRA):", cant_bra)

    mayor_pais = "ARG"
    mayor_cant = cant_arg
    menor_pais = "ARG"
    menor_cant = cant_arg

    if cant_chi > mayor_cant:
        mayor_pais = "CHI"
        mayor_cant = cant_chi
    elif cant_chi < menor_cant:
        menor_pais = "CHI"
        menor_cant = cant_chi

    if cant_bra > mayor_cant:
        mayor_pais = "BRA"
        mayor_cant = cant_bra
    elif cant_bra < menor_cant:
        menor_pais = "BRA"
        menor_cant = cant_bra

    print("➡️ País con MÁS aerolíneas:", mayor_pais, "(", mayor_cant, ")")
    print("➡️ País con MENOS aerolíneas:", menor_pais, "(", menor_cant, ")")

def menu_aerolineas():
    opcion = 1
    while opcion != 4:
        print("\n--- GESTIÓN DE AEROLÍNEAS ---")
        print("1. Crear Aerolínea")
        print("2. Modificar Aerolínea")
        print("3. Eliminar Aerolínea")
        print("4. Volver")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            crear_aerolineas()
        elif opcion == 2 or opcion == 3:
            cartel()
        elif opcion == 4:
            print("↩️ Volviendo al menú principal...")
        else:
            print("❌ Opción inválida.")

def menu_principal():
    opcion = 1
    while opcion != 5:
        print("\n======= MENÚ PRINCIPAL - ADMINISTRADOR =======")
        print("1. Gestión de Aerolíneas")
        print("2. Aprobar/Denegar Promociones")
        print("3. Gestión de Novedades")
        print("4. Reportes")
        print("5. Salir")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            menu_aerolineas()
        elif opcion == 2:
            cartel()
        elif opcion == 3:
            cartel()
        elif opcion == 4:
            cartel()
        elif opcion == 5:
            print("👋 Saliendo del sistema...")
        else:
            print("❌ Opción inválida. Intente nuevamente.")

def login():
    usuario_correcto = "admin@ventaspasajes777.com"
    contrasena_correcta = "admin"

    intentos = 0
    acceso_concedido = False

    while intentos < 3 and not acceso_concedido:
        print("\nIniciar sesión como ADMINISTRADOR")
        usuario_ingresado = input("Ingrese su usuario: ")
        contrasena_ingresada = getpass.getpass("Ingrese su contraseña (no visible): ")

        if usuario_ingresado == usuario_correcto and contrasena_ingresada == contrasena_correcta:
            acceso_concedido = True
        else:
            intentos += 1
            print("❌ Usuario o contraseña incorrectos. Intento", intentos, "de 3.")

    if acceso_concedido:
        print("\n✅ Acceso concedido. Bienvenido, administrador.\n")
        menu_principal()
    else:
        print("\n🚫 Acceso denegado. Se superaron los 3 intentos permitidos.")

# Programa principal
login()

# Variables simuladas para 3 novedades
codigo_novedad1, texto1, fecha_pub1, fecha_exp1 = "1", "Mantenimiento en pista principal", "2025-04-20", "2025-04-22"
codigo_novedad2, texto2, fecha_pub2, fecha_exp2 = "2", "¡Felices fiestas! Descuentos especiales", "2025-12-01", "2025-12-31"
codigo_novedad3, texto3, fecha_pub3, fecha_exp3 = "3", "Recomendación: llegar 3h antes a vuelos internacionales", "2025-04-01", "2025-06-30"

def ver_novedades():
    print("\n📢 NOVEDADES DEL SISTEMA")
    print("-" * 80)
    print("{:<10} {:<50} {:<12} {:<12}".format("Código", "Texto", "Publicación", "Expiración"))
    print("-" * 80)
    print("{:<10} {:<50} {:<12} {:<12}".format(codigo_novedad1, texto1, fecha_pub1, fecha_exp1))
    print("{:<10} {:<50} {:<12} {:<12}".format(codigo_novedad2, texto2, fecha_pub2, fecha_exp2))
    print("{:<10} {:<50} {:<12} {:<12}".format(codigo_novedad3, texto3, fecha_pub3, fecha_exp3))
    print("-" * 80)

def modificar_novedad():
    global texto1, fecha_pub1, fecha_exp1
    global texto2, fecha_pub2, fecha_exp2
    global texto3, fecha_pub3, fecha_exp3

    print("\n✏️ MODIFICAR NOVEDAD")
    codigo = input("Ingrese el código de la novedad que desea modificar (1, 2, 3): ")

    if codigo == "1":
        texto1 = input("Nuevo texto: ")
        fecha_pub1 = input("Nueva fecha de publicación (AAAA-MM-DD): ")
        fecha_exp1 = input("Nueva fecha de expiración (AAAA-MM-DD): ")
    elif codigo == "2":
        texto2 = input("Nuevo texto: ")
        fecha_pub2 = input("Nueva fecha de publicación (AAAA-MM-DD): ")
        fecha_exp2 = input("Nueva fecha de expiración (AAAA-MM-DD): ")
    elif codigo == "3":
        texto3 = input("Nuevo texto: ")
        fecha_pub3 = input("Nueva fecha de publicación (AAAA-MM-DD): ")
        fecha_exp3 = input("Nueva fecha de expiración (AAAA-MM-DD): ")
    else:
        print("❌ Código inválido.")

    ver_novedades()

def menu_novedades():
    opcion = 1
    while opcion != 5:
        print("\n--- GESTIÓN DE NOVEDADES ---")
        print("1. Crear Novedad")
        print("2. Modificar Novedad")
        print("3. Eliminar Novedad")
        print("4. Ver Novedades")
        print("5. Volver")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1 or opcion == 3:
            cartel()
        elif opcion == 2:
            modificar_novedad()
        elif opcion == 4:
            ver_novedades()
        elif opcion == 5:
            print("↩️ Volviendo al menú principal...")
        else:
            print("❌ Opción inválida.")
