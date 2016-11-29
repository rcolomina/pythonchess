from piece import Piece
from gameNode import GameNode        
from functions import *
from minmax import MinMax

## TEST 0: Checking movements for Rook, Bishop, Knight and Queen

listPiecesWhite=[]
listPiecesBlack=[]
p1=Piece('Q',[2,1])
#p2=Piece('N',[2,2])
p5=Piece('N',[2,4])
listPiecesWhite.append(p1)
#listPiecesWhite.append(p2)
listPiecesWhite.append(p5)


b1=Piece('q',[1,4])
b2=Piece('r',[2,3])
b3=Piece('n',[2,2])
listPiecesBlack.append(p1)
listPiecesBlack.append(p2)
listPiecesBlack.append(p3)

gameNode=GameNode(listPiecesWhite,listPiecesBlack,"white")

#listMovsPiece=genListMovsPiece(gameNode,p4)
#print "listMovsPiece:"
#for mov in listMovsPiece:
#    print mov

#move=[1,4]
#listWhitePieces=gameNode.genListPiecesWhite(p2,move)
#assert(p2 not in listWhitePieces)
#listBlackPieces=gameNode.genListPiecesBlack(p2,move)
#assert(p3 not in listBlackPieces)
#assert(GameNode(listWhitePieces,listBlackPieces,"black").checkWhiteWin())



# TEST 1: Testing Game Succesors
print "TEST 1"

listPiecesWhite=[]
listPiecesBlack=[]
p1=Piece('Q',[3,3])
#p2=Piece('N',[1,2])
p3=Piece('R',[2,1])
p4=Piece('B',[2,2])
listPiecesWhite.append(p1)
#listPiecesWhite.append(p2)
listPiecesWhite.append(p3)
listPiecesWhite.append(p4)

p5=Piece('q',[1,4])
listPiecesBlack.append(p5)
gameNode=GameNode(listPiecesWhite,listPiecesBlack,"white")
#gameNode.draw()
game1=gameNode.succesGameActionMove(p3,[1,1])
#game1.draw()

#listPieces=gameNode.genListPiecesWhite(p3,[1,1])
#for p in listPieces:
#    print p.type
#listPieces=gameNode.genListPiecesBlack(p3,[1,1])
#for p in listPieces:
#    print p.type


bq=Piece('q',[1,4])
move=[1,1]

listPieces=game1.listPiecesWhite
listPieces=game1.listPiecesBlack
listPieces=game1.genListPiecesWhite(bq,move)
listPieces=game1.genListPiecesBlack(bq,move)
#print "Possible movs for the black queen:",genListMovsPiece(game1,bq)
game2=game1.succesGameActionMove(bq,move) #
#game2.draw()
assert(bq not in game2.listPiecesBlack)

wB=Piece('B',[2,2])
#print "Possible movs for a white bishop:",genListMovsPiece(game2,wB)
game3=game2.succesGameActionMove(wB,[1,1])
#game3.draw()



