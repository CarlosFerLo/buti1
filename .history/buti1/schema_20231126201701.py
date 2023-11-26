from typing import List
from enum import Enum
from pydantic import BaseModel

Palo = Enum("Palo", ["OROS", "BASTOS", "COPAS", "ESPADAS"])

class Carta (BaseModel) :
    palo: Palo
    numero: int # TODO: chack is in range 1-12
    
class Mano (BaseModel) :
    cartas: List[Carta] # TODO: add check for non empty and 12 max
    
    
    
    
    