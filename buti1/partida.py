from pydantic import BaseModel, conlist
from .schema import Mano, Palo, Carta
from typing import Optional, List

class Ronda(BaseModel):
    start: int
    cartas: List[Carta]
    ganador: int

class Partida(BaseModel):
    manos: conlist(Mano, min_length=4, max_length=4)

    trumfo: Optional[Palo]
    cantado_por: Optional[int]
    delegado: Optional[bool]

    rondas: List[Ronda]