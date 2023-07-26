from src.utils import oblicz_pole_prostokata
import unittest


class TestObliczPoleProtokata(unittest.TestCase):

    def test_dwie_normalne_liczby(self):
        assert oblicz_pole_prostokata(5, 6) == 30

    def test_obie_liczby_jako_str(self):
        self.assertRaises(TypeError, oblicz_pole_prostokata, 'text', 'text')

    def test_jedna_liczba_str(self):
        pass
