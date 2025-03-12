import argparse

# Mostrar y preparar los argumentos que admite el programa por la línea de comandos
def MostrarArgumentos():
    # Iniciamos el programa, obteniendo los argumentos pasados por la línea de comandos
    # Conformamos los argumentos que admitirá el programa por la línea de comandos
    parser = argparse.ArgumentParser()
    parser.add_argument("-ur", "--urlraiz", type=str, required=True,
        help="URL raíz a analizar (sin htt://)")
    parser.add_argument("-uc", "--urlcompleta", type=str, required=True,
        help="URL completa a analizar (con http o https://)")
    parser.add_argument("-p", "--puerto", type=int, required=False,
        help="Puerto de conexión")
    parser.add_argument("-m", "--modulo", type=str, required=True,
        help="Nombre del módulo")
    parser.add_argument("-v", "--version", action="store_true", required=False,
        help="Muestra por pantalla la versión de OpenSSL")
    parser.add_argument("-e", "--ComprobarPorEncabezado", action="store_true", required=False,
        help="Para obtener web activa usa un encabezado, necesita los parámetros -EncabezadoNombre -EncabezadoValor")
    parser.add_argument("-c", "--ComprobarPorCodigoRespuesta", action="store_true", required=False,
        help="Para obtener web activa usa un encabezado, necesita los parámetros -EncabezadoNombre -EncabezadoValor")    
    parser.add_argument("-en", "--EncabezadoNombre", type=str, required=False,
        help="Nombre del encabezado para obtener su valor y comprobar si es igual. Por ejemplo 'X-Redirect-By'. El valor del encabezado se indica en el parámetro -ev")
    parser.add_argument("-ev", "--EncabezadoValor", type=str, required=False,
        help="Valor del encabezado indicado en parámetro -en para comprobar si es igual, si lo es la web se marca como activa")
    parser.add_argument("-me", "--MostrarEncabezados", action="store_true", required=False,
        help="Devuelve todos los encabezados del sitio web y sus valores")
    
    return parser.parse_args()

# Ejemplo de uso desde la línea de comandos
# python.exe argumentos_argparse.py  -ur proyectoa.com -uc https://proyectoa.com/index.php -m "Web_OK_ProyectoA" -e -en "Server" -ev "HTTPd"