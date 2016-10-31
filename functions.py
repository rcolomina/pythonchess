from rookmovs import *
from bishopmovs import *
from queenmovs import *
    

# List of Knight movements 
def listMovKnight(coord,ocupyCells):

    maxsize=5 # max size gameboard
    
    l=[]
    x=coord[0]
    y=coord[1]
    l.append([x+1,y+2])
    l.append([x+2,y+1])
    l.append([x+1,y-2])
    l.append([x+2,y-1])
    l.append([x-1,y-2])
    l.append([x-2,y-1])
    l.append([x-1,y+2])
    l.append([x-2,y+1])
    
    lfinal=[]
    for p in l:
        if p[0]>0 and p[0]<maxsize and p[1]>0 and p[1]<maxsize:
            lfinal.append(p)

    return [x for x in lfinal if x not in ocupyCells]


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
    listTargetsPieces=[]
    if piece.type=="r" or piece.type=="R":
        listTargetsPieces=listTargetsRook(gameNode,piece)
    if piece.type=="b" or piece.type=="B":
        listTargetsPieces=listTargetsBishop(gameNode,piece)
    if piece.type=="q" or piece.type=="Q":
        listTargetsPieces=listTargetsQueen(gameNode,piece)
    if piece.type=="n" or piece.type=="N":
        listTargetsPieces=listTargetsKnight(gameNode,piece)
                
    # Adding posible capturing movements
    for p in listTargetsPiece:
        listMovsPiece.append(p.coordenates)
                    
    return listMovsPiece

def checkPieceMovValid(gameNode,piece,mov):
    listMovsPiece=genListMovsPiece(gameNode,piece)
    #print listMovsPiece
    #print mov
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

# Return (1==White Win / 2==Black Win / 3==Draw)
def Utility(gameNode):
    if gameNode.checkWhiteWin():
        return 1
    else:
        if gameNode.checkBlackWin():
            return -1
        else:
            return 0        
        
def genListNextGameNodes(gameNode):
    listgameNodes=[]

    # If game is finished not expand more
    val=Utility(gameNode)
    if val!=0:
        return listgameNodes
    
    listPieces=gameNode.listPiecesToMove()
    for piece in listPieces:
        listMovsPiece=genListMovsPiece(gameNode,piece)
        for mov in listMovsPiece:
            gameNodeChild=gameNode.succesGameActionMove(piece,mov)
            listgameNodes.append(gameNodeChild)

    return listgameNodes

