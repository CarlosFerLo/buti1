from .schema import Palo, Carta, Mano

def cantar (mano: Mano, delegado: bool = False) ->  Palo | None :
    summary = mano.summary()
        