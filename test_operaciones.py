
import unittest
import tempfile
from pathlib import Path

from operaciones import copiar_archivo, eliminar_archivo


class TestOperaciones(unittest.TestCase):

    def setUp(self):
        self.temporal = tempfile.TemporaryDirectory()
        self.carpeta = Path(self.temporal.name)

        self.origen = self.carpeta / "original.txt"
        self.destino = self.carpeta / "copia.txt"
        self.origen.write_text("Prueba de archivos", encoding="utf-8")

    def tearDown(self):
        self.temporal.cleanup()

    def test_copiar_archivo(self):
        resultado = copiar_archivo(self.origen, self.destino)

        self.assertTrue(resultado)
        self.assertTrue(self.destino.exists())
        self.assertEqual(
            self.destino.read_text(encoding="utf-8"),
            "Prueba de archivos"
        )

    def test_eliminar_archivo(self):
        resultado = eliminar_archivo(self.origen)

        self.assertTrue(resultado)
        self.assertFalse(self.origen.exists())

    def test_copiar_archivo_inexistente(self):
        with self.assertRaises(FileNotFoundError):
            copiar_archivo(self.carpeta / "no_existe.txt", self.destino)

    def test_eliminar_archivo_inexistente(self):
        with self.assertRaises(FileNotFoundError):
            eliminar_archivo(self.carpeta / "no_existe.txt")


if __name__ == "__main__":
    unittest.main()
