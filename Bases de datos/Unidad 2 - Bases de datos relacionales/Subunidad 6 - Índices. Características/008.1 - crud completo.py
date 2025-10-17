import sqlite3
import os
import csv
import time
import re
from collections import deque

# ANSI colores y estilos
RESET = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
BG_BLUE = '\033[44m'
BG_GREEN = '\033[42m'
BG_RED = '\033[41m'

# Limpiar pantalla
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Base datos
conexion = sqlite3.connect("empresa.db")
cursor = conexion.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    email TEXT NOT NULL
);
''')
conexion.commit()

# Historial de acciones (últimas 5)
historial = deque(maxlen=5)

# Validar email básico
def validar_email(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, email) is not None

# Mostrar título con borde de colores
def titulo(texto):
    line = '═' * (len(texto) + 6)
    print(f"{MAGENTA}{BOLD}╔{line}╗{RESET}")
    print(f"{MAGENTA}{BOLD}║   {texto}   ║{RESET}")
    print(f"{MAGENTA}{BOLD}╚{line}╝{RESET}")

def imprimir_encabezado():
    titulo("📒 AGENDA DE CLIENTES v3.1 - Ana Sánchez Suárez")

# Funciones básicas mejoradas

def crear_cliente():
    print(f"{BG_GREEN}{BOLD}🧑‍💼 Crear nuevo cliente{RESET}")
    nombre = input("🔤 Nombre: ").strip()
    apellidos = input("🔤 Apellidos: ").strip()
    email = input("📧 Email: ").strip()
    if not nombre or not apellidos or not email:
        print(f"{RED}❌ Todos los campos son obligatorios.{RESET}")
        return
    if not validar_email(email):
        print(f"{RED}❌ Email no válido.{RESET}")
        return
    cursor.execute("INSERT INTO clientes (nombre, apellidos, email) VALUES (?, ?, ?)",
                   (nombre, apellidos, email))
    conexion.commit()
    historial.append(f"Creado cliente: {nombre} {apellidos}")
    print(f"{GREEN}✅ Cliente creado con éxito.{RESET}")

def listar_clientes(orden='asc'):
    cursor.execute(f"SELECT * FROM clientes ORDER BY nombre {'ASC' if orden == 'asc' else 'DESC'}, apellidos")
    clientes = cursor.fetchall()
    if clientes:
        print(f"{CYAN}{BOLD}📋 Lista de clientes ({'Ascendente' if orden=='asc' else 'Descendente'}):{RESET}")
        print(f"{YELLOW}{'─'*60}{RESET}")
        for c in clientes:
            print(f"🆔 {c[0]} | 👤 {c[1]} {c[2]} | 📧 {c[3]}")
        print(f"{YELLOW}{'─'*60}{RESET}")
        print(f"{GREEN}📊 Total: {len(clientes)} clientes.{RESET}")
    else:
        print(f"{RED}⚠️ No hay clientes registrados.{RESET}")

def actualizar_cliente():
    listar_clientes()
    try:
        id_cliente = int(input("🛠️ ID del cliente a actualizar: "))
    except ValueError:
        print(f"{RED}❌ ID inválido.{RESET}")
        return

    cursor.execute("SELECT * FROM clientes WHERE id = ?", (id_cliente,))
    cliente = cursor.fetchone()
    if not cliente:
        print(f"{RED}❌ Cliente no encontrado.{RESET}")
        return

    print(f"Introduce nuevos datos (ENTER para mantener actual):")
    nombre = input(f"Nombre [{cliente[1]}]: ").strip()
    apellidos = input(f"Apellidos [{cliente[2]}]: ").strip()
    email = input(f"Email [{cliente[3]}]: ").strip()

    if email and not validar_email(email):
        print(f"{RED}❌ Email no válido. Operación cancelada.{RESET}")
        return

    nombre = nombre if nombre else cliente[1]
    apellidos = apellidos if apellidos else cliente[2]
    email = email if email else cliente[3]

    cursor.execute("""
        UPDATE clientes SET nombre=?, apellidos=?, email=? WHERE id=?
    """, (nombre, apellidos, email, id_cliente))
    conexion.commit()
    historial.append(f"Actualizado cliente ID {id_cliente}")
    print(f"{GREEN}✅ Cliente actualizado.{RESET}")

def eliminar_cliente():
    listar_clientes()
    try:
        id_cliente = int(input("🗑️ ID del cliente a eliminar: "))
    except ValueError:
        print(f"{RED}❌ ID inválido.{RESET}")
        return
    confirm = input(f"{RED}⚠️ Seguro que quieres eliminar cliente {id_cliente}? (s/N): ").lower()
    if confirm == 's':
        # Animación simple de borrado
        print("Eliminando", end='', flush=True)
        for _ in range(3):
            time.sleep(0.5)
            print(".", end='', flush=True)
        print()
        cursor.execute("DELETE FROM clientes WHERE id=?", (id_cliente,))
        conexion.commit()
        if cursor.rowcount:
            historial.append(f"Eliminado cliente ID {id_cliente}")
            print(f"{GREEN}✅ Cliente eliminado.{RESET}")
        else:
            print(f"{RED}❌ No se encontró cliente con ese ID.{RESET}")
    else:
        print(f"{YELLOW}🔁 Operación cancelada.{RESET}")

def buscar_cliente():
    termino = input("🔍 Buscar (nombre, apellidos o email): ").strip()
    if not termino:
        print(f"{RED}❌ Debes ingresar un término para buscar.{RESET}")
        return
    like_term = f"%{termino}%"
    cursor.execute("""
        SELECT * FROM clientes WHERE
        nombre LIKE ? OR apellidos LIKE ? OR email LIKE ?
        ORDER BY nombre, apellidos
    """, (like_term, like_term, like_term))
    resultados = cursor.fetchall()
    if resultados:
        print(f"{CYAN}🔎 Resultados de búsqueda:{RESET}")
        for c in resultados:
            print(f"🆔 {c[0]} | 👤 {c[1]} {c[2]} | 📧 {c[3]}")
    else:
        print(f"{RED}❌ No se encontraron resultados.{RESET}")

def exportar_csv():
    archivo = input("📤 Nombre archivo exportar (ejemplo clientes.csv): ").strip()
    if not archivo:
        archivo = "clientes_exportados.csv"
    cursor.execute("SELECT * FROM clientes ORDER BY nombre, apellidos")
    clientes = cursor.fetchall()
    try:
        with open(archivo, mode="w", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Nombre", "Apellidos", "Email"])
            writer.writerows(clientes)
        print(f"{GREEN}✅ Exportado a {archivo}{RESET}")
        historial.append(f"Exportado clientes a {archivo}")
    except Exception as e:
        print(f"{RED}❌ Error exportando: {e}{RESET}")

def importar_csv():
    archivo = input("📥 Nombre archivo importar (ejemplo clientes_importar.csv): ").strip()
    if not archivo:
        archivo = "clientes_importar.csv"
    try:
        with open(archivo, mode="r", encoding='utf-8') as f:
            reader = csv.DictReader(f)
            count = 0
            for row in reader:
                if "Nombre" in row and "Apellidos" in row and "Email" in row:
                    if validar_email(row["Email"].strip()):
                        cursor.execute("INSERT INTO clientes (nombre, apellidos, email) VALUES (?, ?, ?)",
                                       (row["Nombre"].strip(), row["Apellidos"].strip(), row["Email"].strip()))
                        count += 1
                    else:
                        print(f"{YELLOW}⚠️ Email inválido ignorado: {row['Email']}{RESET}")
                else:
                    print(f"{YELLOW}⚠️ Fila inválida ignorada: {row}{RESET}")
            conexion.commit()
        print(f"{GREEN}📥 Importados {count} clientes desde {archivo}.{RESET}")
        historial.append(f"Importados {count} clientes desde {archivo}")
    except FileNotFoundError:
        print(f"{RED}❌ Archivo {archivo} no encontrado.{RESET}")
    except Exception as e:
        print(f"{RED}❌ Error al importar: {e}{RESET}")

def limpiar_base():
    print(f"{RED}{BOLD}⚠️ ATENCIÓN: Esta acción eliminará TODOS los clientes.{RESET}")
    confirm1 = input("Escribe 'ELIMINAR' para confirmar: ")
    if confirm1 == "ELIMINAR":
        confirm2 = input("¿Estás seguro? Escribe 'SI' para borrar todo: ")
        if confirm2 == "SI":
            cursor.execute("DELETE FROM clientes")
            conexion.commit()
            historial.append("Base de datos limpiada completamente")
            print(f"{GREEN}🧹 Base de datos limpia.{RESET}")
            return
    print(f"{YELLOW}🔁 Operación cancelada.{RESET}")

def mostrar_estadisticas():
    print(f"{BOLD}{CYAN}📊 Estadísticas de clientes por dominio de email:{RESET}")
    cursor.execute("""
        SELECT
            SUBSTR(email, INSTR(email, '@') + 1) as dominio,
            COUNT(*) as cantidad
        FROM clientes
        GROUP BY dominio
        ORDER BY cantidad DESC;
    """)
    datos = cursor.fetchall()
    if datos:
        for dominio, cant in datos:
            print(f"📧 {dominio}: {cant} cliente(s)")
    else:
        print(f"{RED}⚠️ No hay datos para mostrar.{RESET}")

def mostrar_historial():
    print(f"{MAGENTA}{BOLD}🕘 Historial de acciones recientes:{RESET}")
    if historial:
        for h in historial:
            print(f"• {h}")
    else:
        print("No hay acciones registradas aún.")

def mostrar_ayuda():
    clear_screen()
    titulo("🆘 AYUDA")
    print(f"""
{CYAN}Este programa es una agenda para gestionar clientes con las siguientes opciones:

{YELLOW}1{RESET}: Crear cliente.
{YELLOW}2{RESET}: Listar clientes (puedes elegir orden ascendente o descendente).
{YELLOW}3{RESET}: Actualizar cliente por ID.
{YELLOW}4{RESET}: Eliminar cliente por ID con confirmación y animación.
{YELLOW}5{RESET}: Buscar clientes por nombre, apellidos o email.
{YELLOW}6{RESET}: Exportar clientes a archivo CSV (puedes elegir nombre de archivo).
{YELLOW}7{RESET}: Importar clientes desde archivo CSV (con validación básica).
{YELLOW}8{RESET}: Limpiar toda la base de datos (requiere doble confirmación).
{YELLOW}9{RESET}: Mostrar estadísticas de clientes por dominio de email.
{YELLOW}10{RESET}: Mostrar historial de acciones recientes.
{YELLOW}0{RESET}: Mostrar esta ayuda.

{CYAN}Presiona ENTER para volver al menú.{RESET}
""")
    input()

def menu():
    while True:
        clear_screen()
        imprimir_encabezado()
        print(f"""{BOLD}{CYAN}
╔════════════════════════════════════════╗
║          📘 MENÚ PRINCIPAL              ║
╚════════════════════════════════════════╝
1️⃣  Crear cliente 🧑‍💼
2️⃣  Listar clientes 📋
3️⃣  Actualizar cliente 🛠️
4️⃣  Eliminar cliente 🗑️
5️⃣  Buscar cliente 🔍
6️⃣  Exportar clientes a CSV 📤
7️⃣  Importar clientes desde CSV 📥
8️⃣  Limpiar base de datos 🧨
9️⃣  Estadísticas por dominio 📊
10️⃣ Historial de acciones 🕘
0️⃣  Ayuda 🆘
11️⃣ Salir 🚪
{RESET}""")
        opcion = input("👉 Elige una opción (0-11): ").strip()
        clear_screen()

        if opcion == '1':
            crear_cliente()
        elif opcion == '2':
            orden = input("¿Orden ascendente (a) o descendente (d)? (a/d): ").lower()
            listar_clientes('desc' if orden == 'd' else 'asc')
        elif opcion == '3':
            actualizar_cliente()
        elif opcion == '4':
            eliminar_cliente()
        elif opcion == '5':
            buscar_cliente()
        elif opcion == '6':
            exportar_csv()
        elif opcion == '7':
            importar_csv()
        elif opcion == '8':
            limpiar_base()
        elif opcion == '9':
            mostrar_estadisticas()
        elif opcion == '10':
            mostrar_historial()
        elif opcion == '0':
            mostrar_ayuda()
        elif opcion == '11':
            print(f"{GREEN}👋 Gracias por usar la agenda. Hasta luego.{RESET}")
            break
        else:
            print(f"{RED}❌ Opción no válida. Intenta de nuevo.{RESET}")

        input(f"\n{CYAN}Presiona ENTER para continuar...{RESET}")

if __name__ == "__main__":
    menu()
    conexion.close()
