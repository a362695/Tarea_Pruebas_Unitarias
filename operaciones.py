
from pathlib import Path
import shutil


def copiar_archivo(origen, destino):
    origen = Path(origen)
    destino = Path(destino)

    if not origen.is_file():
        raise FileNotFoundError("El archivo de origen no existe")

    shutil.copy2(origen, destino)
    return True


def eliminar_archivo(ruta):
    ruta = Path(ruta)

    if not ruta.is_file():
        raise FileNotFoundError("El archivo no existe")

    ruta.unlink()
    return True
