import sys

# Comprobamos si se han pasado argumentos por línea de comandos
# Teniendo en cuenta que el primer argumento argv[0] es el propio nombre del ejecutable Python
argumentos = sys.argv
numArg = len(argumentos)
if (numArg > 0):
    print(f"Has pasado {numArg} argumentos por la línea de comandos")
    print("Los argumentos que has pasado son:")
    i = 0
    for argumento in argumentos:
        i = i + 1
        print(f"Argumento {i} -> {argumento}")
else: 
    print("No has pasado argumentos por la línea de comandos")
    
# Ejemplo de uso desde la línea de comandos
# argumentos_argv.py Argumento1 Argumento2