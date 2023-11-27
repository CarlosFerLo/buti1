import unittest
from buti1 import Mano, Carta, Palo
import pydantic

class TestSchema (unittest.TestCase) :
    def test_carta_class_can_only_be_init_with_number_in_range_1_to_12 (self) :
        carta = Carta(palo=Palo.OROS, numero=3)
        self.assertIsInstance(carta, Carta)
        
        self.assertRaises(pydantic.ValidationError, Carta, palo=Palo.OROS, numero=0)
        self.assertRaises(pydantic.ValidationError, Carta, palo=Palo.OROS, numero=13)
        
    def test_carta_can_be_instantiated_from_string (self) :
        carta1 = Carta.from_str("12O")
        carta2 = Carta(palo=Palo.OROS, numero=12)
        
        self.assertEqual(carta1, carta2)
        
        self.assertRaises(ValueError, Carta.from_str, "not valid string")
        
    def test_carta_str_conversion_works_as_expected (self) :
        string = "3C"
        carta = Carta.from_str(string)
        
        self.assertEqual(str(carta), string)
        
    def test_mano_from_string_class_method_returns_correct_instance (self) :
        cartas = [
           Carta(palo=Palo.OROS, numero=12),
            Carta(palo=Palo.BASTOS, numero=1),
            Carta(palo=Palo.BASTOS, numero=2),
            Carta(palo=Palo.COPAS, numero=5) 
        ]
    
        mano1 = Mano(cartas=cartas)
        
        string = ",".join(cartas)

    
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