from typing import List, Dict
from enum import Enum
from pydantic import BaseModel

Palo = Enum("Palo", ["OROS", "BASTOS", "COPAS", "ESPADAS"])

class Carta (BaseModel) :
    palo: Palo
    numero: int # TODO: chack is in range 1-12
    
    def punct (self) -> int :
        punct_dict = { 9: 5, 1: 4, 12: 3, 11: 2, 10: 1 }
        
        return punct_dict.get(self.numero, 0)
            
        
class Mano (BaseModel) :
    cartas: List[Carta] # TODO: add check for non empty and 12 max
    
    def count (self) -> Dict[Palo, int] :
        count = dict()
        for palo in Palo :
            num = len([ c for c in self.cartas if c.palo == palo ])
            count[palo] = num 
        return count
    
    def punct (self) -> Dict[Palo, int] :
        punct = dict()
        for palo in Palo :
            punct = sum([c.punct() for c in self.cartas if c.palo == palo ])
            
    