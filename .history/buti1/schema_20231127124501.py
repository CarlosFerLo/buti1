from typing import Dict
import re
from enum import Enum
from pydantic import BaseModel, Field, conlist

Palo = Enum("Palo", ["OROS", "BASTOS", "COPAS", "ESPADAS"])

class Carta (BaseModel) :
    palo: Palo
    numero: int = Field(ge=1, le=12)
    
    def __str__(self) -> str:
        return f"{self.numero} {self.palo}"
    
    @classmethod
    def from_str (cls, string: str) -> "Carta" :
        result = re.match(r"(\d+)([OCEB])")
    
    def punct (self) -> int :
        punct_dict = { 9: 5, 1: 4, 12: 3, 11: 2, 10: 1 }
        
        return punct_dict.get(self.numero, 0)
    
            
        
class Mano (BaseModel) :
    cartas: conlist(Carta, min_length=1, max_length=12)
    
    def count (self) -> Dict[Palo, int] :
        count = dict()
        for palo in Palo :
            num = len([ c for c in self.cartas if c.palo == palo ])
            count[palo] = num 
        return count
    
    def punct (self) -> Dict[Palo, int] :
        punct = dict()
        for palo in Palo :
            num = sum([c.punct() for c in self.cartas if c.palo == palo ])
            punct[palo] = num

        return punct