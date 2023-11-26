from .schema import Palo, Carta, Mano

def cantar (mano: Mano, delegado: bool = False) ->  Palo | None :
    count = mano.count()
    
    if not delegado :
        sort = sorted(count.items(), key=lambda x: x[1])
        min_num, max_num = sort[0], sort[-1]
        
        if max_num < 5 :
            return None
        
        if min_num == 5 :
            
        