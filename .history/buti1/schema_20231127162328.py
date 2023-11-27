from typing import Dict, List
import re
from enum import Enum
from pydantic import BaseModel, Field, conlist, field_validator

Palo = Enum("Palo", ["OROS", "BASTOS", "COPAS", "ESPADAS"])

class Carta (BaseModel) :
    palo: Palo
    numero: int = Field(ge=1, le=12)
    
    def __str__(self) -> str:
        palo = {Palo.OROS: "O", Palo.BASTOS: "B", Palo.ESPADAS: "E", Palo.COPAS: "C"}[self.palo]
        return f"{self.numero}{palo}"
    
    @classmethod
    def from_str (cls, string: str) -> "Carta" :
        result = re.match(r"(?P<numero>(\d+))(?P<palo>([OCEB]))", string)
        
        if not result :
            raise ValueError("Invalid string: " + string)
        
        return cls(
            palo={"O": Palo.OROS, "B": Palo.BASTOS, "E": Palo.ESPADAS, "C": Palo.COPAS}[result["palo"]],
            numero=int(result["numero"])
        )
        
    
    def punct (self) -> int :
        punct_dict = { 9: 5, 1: 4, 12: 3, 11: 2, 10: 1 }
        
        return punct_dict.get(self.numero, 0)
    
            
        
class Mano (BaseModel) :
    cartas: conlist(Carta, min_length=1, max_length=12)
    
    @classmethod
    def from_str (cls, string: str) -> "Mano" :
        card_str_list = string.split(",")
        cards = [ Carta.from_str(c) for c in card_str_list ]
        
        return cls(cartas=cards)
    
    @field_validator("cartas")
    @classmethod
    def validate_cartas_does_not_contain_duplicates (cls, cartas: List[Carta]) :
        while len(cartas) > 0 :
            c = cartas.pop()
            
            if c in cartas :
                raise ValueError("Carta aparece dos o mas veces en la misma mano. Carta: " + str(c))
            
            cartas.append(c)
            
        return cartas
    
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