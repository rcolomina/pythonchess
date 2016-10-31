from rookmovs import *
from bishopmovs import *


def listMovQueen(coord,ocupyCells):
    listMovs=[]
    
    coorx=coord[0]
    coory=coord[1]

    # Movs like a Rook
    rookMovs=listMovRook(coord,ocupyCells)
    
    # Movs like a Bishop
    bishopMovs=listMovBishop(coord,ocupyCells)

    listMovs.extend(rookMovs)
    listMovs.extend(bishopMovs)
    
    return listMovs

def listTargetsQueen(gameNode,piece):

    listTargetsQueen=[]

    # Targets like a Rook
    rookTargets=listTargetsRook(gameNode,piece)

    # Targets like a Bishop
    bishopTargets=listTargetsBishop(gameNode,piece)
    
    listTargetsQueen.extend(rookTargets)
    listTargetsQueen.extend(bishopTargets)
    
    return listTargetsQueen
