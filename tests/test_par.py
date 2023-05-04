# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import par

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación par
    def test_par(self):
        assert par(4) == True
        assert par(5) == False
        assert par(9) == False
        assert par(400) == True
