
from pathlib import Path
from operaciones import copiar_archivo, eliminar_archivo

original = Path("original.txt")
copia = Path("copia.txt")

print("\nDEMOSTRACION DE OPERACIONES CON ARCHIVOS")
print("---------------------------------------")

# Preparar los archivos para repetir la demostracion
if copia.exists():
    copia.unlink()

print("\n1. CREAR ARCHIVO")
original.write_text(
    "Prueba de archivos para la universidad",
    encoding="utf-8"
)
print("Archivo creado:", original.name)

print("\n2. COPIAR ARCHIVO")
copiar_archivo(original, copia)
print("Copia realizada correctamente.")
print("Existe el original:", original.exists())
print("Existe la copia:", copia.exists())

print("\n3. ELIMINAR ARCHIVO")
eliminar_archivo(copia)
print("Copia eliminada correctamente.")
print("Existe el original:", original.exists())
print("Existe la copia:", copia.exists())

print("\nDEMOSTRACION FINALIZADA")
