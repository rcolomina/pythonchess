from rookmovs import *
from bishopmovs import *
from queenmovs import *
from knightmovs import *

# Accept a gamenode and a piece returning its list of movements
def genListMovsPiece(gameNode,piece):
    
    listMovsPiece=[]
    #occupy=[gameNode.listCoordsWhite
     #       if piece.type.isupper() else gameNode.listCoordsBlack].pop()
    occupy=[]
    occupy.extend(gameNode.listCoordsWhite)
    occupy.extend(gameNode.listCoordsBlack)

    # Free moves (witout capturing)
    coord=piece.coordenates
    if piece.type=="r" or piece.type=="R":
        listMovsPiece=listMovRook(coord,occupy)        
    if piece.type=="b" or piece.type=="B":
        listMovsPiece=listMovBishop(coord,occupy)
    if piece.type=="q" or piece.type=="Q":
        listMovsPiece=listMovQueen(coord,occupy)
    if piece.type=="n" or piece.type=="N":
        listMovsPiece=listMovKnight(coord,occupy)

    # Getting pieces for capturing movements
    listTargetsPiece=[]
    if piece.type=="r" or piece.type=="R":
        listTargetsPiece=listTargetsRook(gameNode,piece)
    if piece.type=="b" or piece.type=="B":
        listTargetsPiece=listTargetsBishop(gameNode,piece)
    if piece.type=="q" or piece.type=="Q":
        listTargetsPiece=listTargetsQueen(gameNode,piece)
    if piece.type=="n" or piece.type=="N":
        listTargetsPiece=listTargetsKnight(gameNode,piece)

    #print listTargetsPiece
        
    # Adding posible capturing movements
    for p in listTargetsPiece:
        listMovsPiece.append(p.coordenates)
                    
    return listMovsPiece

def checkPieceMovValid(gameNode,piece,mov):
    listMovsPiece=genListMovsPiece(gameNode,piece)
    for m in listMovsPiece:
        if m==mov:
            return True
    return False


def genListNextGameNodesForcingColor(gameNode,color):
    listgameNodes=[]

    listPieces=[gameNode.listPiecesBlack if color=="black" else gameNode.listPiecesWhite].pop()
    for piece in listPieces:
        listMovsPiece=genListMovsPiece(gameNode,piece)
        for mov in listMovsPiece:
            gameNodeChild=gameNode.succesGameActionMove(piece,mov)
            listgameNodes.append(gameNodeChild)
            
        #print "listMovsPiece:",listMovsPiece
    return listgameNodes

        
def genListNextGameNodes(gameNode):
    listgameNodes=[]

    # If game is finished not expand more
    val=gameNode.utility();
    if val!=0:
        return listgameNodes
    
    listPieces=gameNode.listPiecesToMove()
    for piece in listPieces:
        listMovsPiece=genListMovsPiece(gameNode,piece)
        for mov in listMovsPiece:
            gameNodeChild=gameNode.succesGameActionMove(piece,mov)
            listgameNodes.append(gameNodeChild)

    return listgameNodes

