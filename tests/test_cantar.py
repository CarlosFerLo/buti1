import unittest
from buti1 import Mano, Carta, Palo, cantar


class TestCantar(unittest.TestCase):
    def test_cantar_delega(self):
        mano = Mano.from_str("1O,2O,3O,4O,5E")
        self.assertIsNone(cantar(mano))

        mano = Mano.from_str("1O,2O,3O,4O,5O,5E,6E,7C,8C,9B,10B,11B")
        self.assertIsNone(cantar(mano))

    def test_cantar_delegado_no_delega(self):
        mano = Mano.from_str("1O,2O,3O,4O,5E")
        self.assertIsNotNone(cantar(mano,True))

        mano = Mano.from_str("1O,2O,3O,4O,5O,5E,6E,7C,8C,9B,10B,11B")
        self.assertIsNotNone(cantar(mano,True))