"""
Ponto de entrada da Calculadora em Python.
Permite iniciar tanto em modo gráfico (GUI) quanto em modo terminal (CLI).
"""

import argparse
import sys


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Calculadora em Python com suporte a GUI e CLI interativa."
    )
    parser.add_argument(
        "--cli",
        action="store_true",
        help="Inicia a calculadora no modo terminal (linha de comando).",
    )
    parser.add_argument(
        "--gui",
        action="store_true",
        help="Inicia a calculadora no modo gráfico desktop (padrão).",
    )
    parser.add_argument(
        "--web",
        action="store_true",
        help="Inicia o servidor Web App para celular (Wi-Fi) e navegador.",
    )

    args = parser.parse_args()

    if args.web:
        from calculadora.web import start_web
        start_web()
    elif args.cli:
        from calculadora.cli import start_cli
        start_cli()
    else:
        try:
            from calculadora.gui import start_gui
            start_gui()
        except Exception as e:
            print(f"Não foi possível iniciar a interface gráfica ({e}).")
            print("Iniciando em modo linha de comando (CLI)...\n")
            from calculadora.cli import start_cli
            start_cli()


if __name__ == "__main__":
    main()
