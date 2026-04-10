"""
Simulador financiero: interés simple y semáforo de alerta.
Uso:
  python main.py              → interfaz gráfica
  python main.py --consola    → modo consola (comportamiento original)
"""

from __future__ import annotations

import argparse
import re
import sys
import tkinter as tk
from tkinter import messagebox, ttk
from typing import Literal, TypedDict


class ResultadoPrestamo(TypedDict):
    capital: float
    tasa_porcentaje: float
    años: int
    interes: float
    monto_total: float
    porcentaje_interes: float
    semaforo: Literal["VERDE", "AMARILLO", "ROJO"]


def simular_prestamo(capital: float, tasa_porcentaje: float, años: int) -> ResultadoPrestamo:
    """Calcula interés simple, total a pagar y nivel del semáforo."""
    if capital <= 0:
        raise ValueError("El capital debe ser mayor que cero.")
    if años < 0:
        raise ValueError("El plazo en años no puede ser negativo.")

    tasa = tasa_porcentaje / 100
    interes = capital * tasa * años
    monto_total = capital + interes
    porcentaje_interes = (interes / capital) * 100

    if porcentaje_interes < 5:
        semaforo: Literal["VERDE", "AMARILLO", "ROJO"] = "VERDE"
    elif porcentaje_interes < 7:
        semaforo = "AMARILLO"
    else:
        semaforo = "ROJO"

    return {
        "capital": capital,
        "tasa_porcentaje": tasa_porcentaje,
        "años": años,
        "interes": interes,
        "monto_total": monto_total,
        "porcentaje_interes": porcentaje_interes,
        "semaforo": semaforo,
    }


def _parse_float_es(texto: str) -> float:
    texto = texto.strip().replace(",", ".")
    if not texto:
        raise ValueError("Valor vacío.")
    return float(texto)


def ejecutar_consola() -> None:
    print(
        r"""
  ____                   __   __                   _____ _                        _
 / ___|  ___ _ __ ___   /_/_ / _| ___  _ __ ___   |  ___(_)_ __   __ _ _ __   ___(_) ___ _ __ ___
 \___ \ / _ \ '_ ` _ \ / _` | |_ / _ \| '__/ _ \  | |_  | | '_ \ / _` | '_ \ / __| |/ _ \ '__/ _ \
  ___) |  __/ | | | | | (_| |  _| (_) | | | (_) | |  _| | | | | | (_| | | | | (__| |  __/ | | (_) |
 |____/ \___|_| |_| |_|\__,_|_|  \___/|_|  ____/  |_|   |_|_| |_|\__,_|_| |_|\___|_|  \___/
"""
    )

    print("=" * 80)
    print("        📥 INGRESO DE DATOS\n")

    capital = float(input("💰 Ingrese el monto del préstamo ($): "))
    tasa_input = input("📈 Ingrese la tasa de interés anual (%): ")
    tasa_porcentaje = _parse_float_es(tasa_input)
    años = int(input("⏳ Ingrese el plazo en años: "))

    try:
        r = simular_prestamo(capital, tasa_porcentaje, años)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    color_red = "\033[1;91m"
    color_yellow = "\033[1;93m"
    color_green = "\033[1;92m"
    color_reset = "\033[0m"

    if r["semaforo"] == "VERDE":
        semaforo_simbolo = f"{color_green}● {r['semaforo']}{color_reset}"
    elif r["semaforo"] == "AMARILLO":
        semaforo_simbolo = f"{color_yellow}● {r['semaforo']}{color_reset}"
    else:
        semaforo_simbolo = f"{color_red}● {r['semaforo']}{color_reset}"

    print("========================================")
    print("        📊 RESULTADOS DEL PRÉSTAMO")
    print("======================================== ")
    print(f"💰 Capital inicial  :    ${r['capital']:,.2f}")
    print(f"📈 Tasa anual       :   {r['tasa_porcentaje']}%")
    print(f"⏳ Plazo            :   {r['años']} años")
    print("\n----------------------------------------")
    print(f"💵 Interés total    :   ${r['interes']:,.2f}")
    print(f"💳 Total a pagar    :   ${r['monto_total']:,.2f}")
    print(f"📊 % Interés        :   {r['porcentaje_interes']:.2f}%")
    print("\n----------------------------------------")
    print(f"🚦 Nivel de alerta  :   {semaforo_simbolo}")
    print("========================================")


def ejecutar_gui() -> None:
    root = tk.Tk()
    root.title("Simulador financiero — interés simple")
    root.minsize(420, 380)
    root.geometry("480x420")

    main = ttk.Frame(root, padding=16)
    main.grid(row=0, column=0, sticky="nsew")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    ttk.Label(main, text="Monto del préstamo ($)").grid(row=0, column=0, sticky="w", pady=(0, 4))
    var_capital = tk.StringVar()
    ent_capital = ttk.Entry(main, textvariable=var_capital, width=28)
    ent_capital.grid(row=1, column=0, sticky="ew", pady=(0, 10))

    ttk.Label(main, text="Tasa de interés anual (%)").grid(row=2, column=0, sticky="w", pady=(0, 4))
    var_tasa = tk.StringVar()
    ent_tasa = ttk.Entry(main, textvariable=var_tasa, width=28)
    ent_tasa.grid(row=3, column=0, sticky="ew", pady=(0, 10))

    ttk.Label(main, text="Plazo (años)").grid(row=4, column=0, sticky="w", pady=(0, 4))
    var_años = tk.StringVar()
    ent_años = ttk.Entry(main, textvariable=var_años, width=28)
    ent_años.grid(row=5, column=0, sticky="ew", pady=(0, 14))

    resultado_frame = ttk.LabelFrame(main, text="Resultados", padding=10)
    resultado_frame.grid(row=7, column=0, sticky="nsew", pady=(0, 10))
    main.rowconfigure(7, weight=1)
    main.columnconfigure(0, weight=1)

    lbl_interes = ttk.Label(resultado_frame, text="Interés total: —")
    lbl_interes.grid(row=0, column=0, sticky="w")
    lbl_total = ttk.Label(resultado_frame, text="Total a pagar: —")
    lbl_total.grid(row=1, column=0, sticky="w", pady=(4, 0))
    lbl_pct = ttk.Label(resultado_frame, text="% interés / capital: —")
    lbl_pct.grid(row=2, column=0, sticky="w", pady=(4, 0))

    semaforo_frame = ttk.Frame(resultado_frame)
    semaforo_frame.grid(row=3, column=0, sticky="w", pady=(10, 0))
    ttk.Label(semaforo_frame, text="Nivel de alerta:").pack(side=tk.LEFT, padx=(0, 8))
    lbl_dot = tk.Label(semaforo_frame, text="●", font=("Segoe UI", 16))
    lbl_dot.pack(side=tk.LEFT, padx=(0, 4))
    lbl_semaforo = ttk.Label(semaforo_frame, text="—")
    lbl_semaforo.pack(side=tk.LEFT)

    colores = {"VERDE": "#1a7f37", "AMARILLO": "#b58900", "ROJO": "#c5221f"}

    def calcular() -> None:
        try:
            capital = _parse_float_es(var_capital.get())
            tasa_porcentaje = _parse_float_es(var_tasa.get())
            años_str = var_años.get().strip()
            if not re.fullmatch(r"-?\d+", años_str):
                raise ValueError("El plazo debe ser un número entero de años.")
            años = int(años_str)
            r = simular_prestamo(capital, tasa_porcentaje, años)
        except ValueError as e:
            messagebox.showerror("Datos inválidos", str(e))
            return

        lbl_interes.config(text=f"Interés total:    ${r['interes']:,.2f}")
        lbl_total.config(text=f"Total a pagar:    ${r['monto_total']:,.2f}")
        lbl_pct.config(text=f"% interés / capital: {r['porcentaje_interes']:.2f}%")
        c = colores[r["semaforo"]]
        lbl_dot.config(fg=c)
        lbl_semaforo.config(text=r["semaforo"])

    btn = ttk.Button(main, text="Calcular", command=calcular)
    btn.grid(row=6, column=0, sticky="w", pady=(0, 8))

    ttk.Label(
        main,
        text="Consola: python main.py --consola",
        font=("Segoe UI", 8),
        foreground="gray",
    ).grid(row=8, column=0, sticky="w")

    ent_capital.focus()
    root.bind("<Return>", lambda _e: calcular())
    root.mainloop()


def main() -> None:
    parser = argparse.ArgumentParser(description="Simulador de préstamo con interés simple.")
    parser.add_argument(
        "--consola",
        "-c",
        action="store_true",
        help="Ejecutar en modo consola (entrada y salida por terminal).",
    )
    args = parser.parse_args()
    if args.consola:
        ejecutar_consola()
    else:
        ejecutar_gui()


if __name__ == "__main__":
    main()
