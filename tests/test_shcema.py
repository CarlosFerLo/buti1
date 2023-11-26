import unittest
from buti1 import Mano, Carta, Palo

class TestSchema (unittest.TestCase) :
    def test_count_method (self) :
        mano = Mano(cartas=[
            Carta(palo=Palo.OROS, numero=12),
            Carta(palo=Palo.BASTOS, numero=1),
            Carta(palo=Palo.BASTOS, numero=2),
            Carta(palo=Palo.COPAS, numero=5)
        ])
        
        count = mano.count()
        
        self.assertDictEqual(count, {Palo.OROS: 1, Palo.BASTOS: 2, Palo.COPAS: 1, Palo.ESPADAS: 0})
        
    def test_punct_method (self) :
        mano = Mano(cartas=[
            Carta(palo=Palo.OROS, numero=12),
            Carta(palo=Palo.BASTOS, numero=1),
            Carta(palo=Palo.BASTOS, numero=2),
            Carta(palo=Palo.COPAS, numero=5)
        ])
        punct = mano.punct()
        
        self.assertDictEqual(punct, {Palo.OROS: 3, Palo.BASTOS: 4, Palo.COPAS: 0, Palo.ESPADAS: 0})