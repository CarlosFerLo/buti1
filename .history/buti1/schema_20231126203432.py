from typing import List, Dict
from enum import Enum
from pydantic import BaseModel

Palo = Enum("Palo", ["OROS", "BASTOS", "COPAS", "ESPADAS"])

class Carta (BaseModel) :
    palo: Palo
    numero: int # TODO: chack is in range 1-12
        
class Mano (BaseModel) :
    cartas: List[Carta] # TODO: add check for non empty and 12 max
    
    def count (self) -> Dict[Palo, int] :
        count = dict()
        for palo in Palo :
            num = len([ c for c in self.cartas if c.palo == palo ])
            count[palo] = num 
        return count
    