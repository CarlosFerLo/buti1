from .schema import Palo, Carta, Mano

def cantar (mano: Mano, delegado: bool = False) ->  Palo | None :
    if not delegado :
        """Comprobar q del palo q tengo mas tenga almenos 5 y un semifallo 
        """
        palo, count = mano.max_palo()