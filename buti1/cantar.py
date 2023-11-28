from .schema import Palo, Carta, Mano

def cantar (mano: Mano, delegado: bool = False) ->  Palo | None :
    count = mano.count()
    sort = sorted(count.items(), key=lambda x: x[1])
    min_num, max_num = sort[0][1], sort[-1][1]    
    
    # Comprobar si se delega o no
    if not delegado :
        if max_num < 5 :
            return None
        
        if max_num == 5 :
            if min_num >= 2 :
                return None
            
    # Ver q palo cantar
    punct = mano.punct()
    
    max_palos = [ palo for palo in Palo if count[palo] == max_num ]
    
    palo = max(max_palos, key=lambda x: punct[x])
    
    return palo
    
        