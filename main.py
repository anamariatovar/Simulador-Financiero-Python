
# Arte ASCII para el título (diseño visual)
print(r"""
  ____                   __   __                   _____ _                        _
 / ___|  ___ _ __ ___   /_/_ / _| ___  _ __ ___   |  ___(_)_ __   __ _ _ __   ___(_) ___ _ __ ___
 \___ \ / _ \ '_ ` _ \ / _` | |_ / _ \| '__/ _ \  | |_  | | '_ \ / _` | '_ \ / __| |/ _ \ '__/ _ \
  ___) |  __/ | | | | | (_| |  _| (_) | | | (_) | |  _| | | | | | (_| | | | | (__| |  __/ | | (_) |
 |____/ \___|_| |_| |_|\__,_|_|  \___/|_|  ____/  |_|   |_|_| |_|\__,_|_| |_|\___|_|  \___/
""")

# Sección de entrada de datos (diseño visual)
print("="*80)
print("        📥 INGRESO DE DATOS\n")

# SEMÁFORO DE INTERÉS
# Proyecto: cálculo del interés simple con apoyo de Python
# 1. Pedimos los datos al usuario (interacción con el usuario)
capital = float(input("💰 Ingrese el monto del préstamo ($): "))
tasa_input = input("📈 Ingrese la tasa de interés anual (%): ")
tasa_porcentaje = float(tasa_input.replace(',', '.'))
años = int(input("⏳ Ingrese el plazo en años: "))

# 2. Convertimos la tasa de porcentaje a decimal (lógica de cálculo)
tasa = tasa_porcentaje / 100

# 3. Calculamos el interés simple (lógica de cálculo)
interes = capital * tasa * años

# 4. Calculamos el monto total a pagar (lógica de cálculo)
monto_total = capital + interes

# 5. Calculamos el porcentaje de interés respecto al capital (lógica de cálculo)
porcentaje_interes = (interes / capital) * 100

# Definir colores ANSI para la salida en consola (diseño visual)
COLOR_RED = "\033[1;91m" # Agregado '1;' para negrita
COLOR_YELLOW = "\033[1;93m" # Agregado '1;' para negrita
COLOR_GREEN = "\033[1;92m" # Agregado '1;' para negrita
COLOR_RESET = "\033[0m"

# 6. Condicional para el color del semáforo basado en el porcentaje de interés (lógica de negocio y diseño visual)
if porcentaje_interes < 5:
    semaforo_texto = "VERDE"
    semaforo_simbolo = f"{COLOR_GREEN}● {semaforo_texto}{COLOR_RESET}" # Aplicar color y reset al final
elif porcentaje_interes < 7:
    semaforo_texto = "AMARILLO"
    semaforo_simbolo = f"{COLOR_YELLOW}● {semaforo_texto}{COLOR_RESET}" # Aplicar color y reset al final
else:
    semaforo_texto = "ROJO"
    semaforo_simbolo = f"{COLOR_RED}● {semaforo_texto}{COLOR_RESET}" # Aplicar color y reset al final

# 7. Imprimir resultados formateados (diseño visual y salida de datos)
print("========================================")
print("        📊 RESULTADOS DEL PRÉSTAMO")
print("======================================== ")
print(f"💰 Capital inicial  :    ${capital:,.2f}")
print(f"📈 Tasa anual       :   {tasa_porcentaje}%")
print(f"⏳ Plazo            :   {años} años")
print("\n----------------------------------------")
print(f"💵 Interés total    :   ${interes:,.2f}")
print(f"💳 Total a pagar    :   ${monto_total:,.2f}")
print(f"📊 % Interés        :   {porcentaje_interes:.2f}%")
print("\n----------------------------------------")
print(f"🚦 Nivel de alerta  :   {semaforo_simbolo}")
print("========================================")