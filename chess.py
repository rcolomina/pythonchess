from piece import Piece
from gameNode import GameNode        
from functions import *
from minmax import MinMax

## TEST 0: Checking movements for Rook, Bishop, Knight and Queen
print "TEST 0"

#piece=['Q',[2,2]]
#coord=[2,2]
#listCells=[[1,1],[1,2],[4,2],[1,4],[3,3],[1,3],[2,1],[3,2]]
#print "listMovRook:",listMovRook(coord,listCells)
#print "listMovBishop:",listMovBishop(coord,listCells)
#print "listMovQueen:",listMovQueen(coord,listCells)
#coord=[1,4]
#listCells=[[1,4]]
#print "listMovKnight:",listMovKnight(coord,listCells)

listMovs=listMovRook([1,2],[[2,2]])
assert(listMovs==[[1,1],[1,3],[1,4]])
print "Checked movements for Rook on [1,2] with [2,2] occupy"
listMovs=listMovRook([1,2],[[3,2]])
assert(listMovs==[[2,2],[1,1],[1,3],[1,4]])
print "Checked movements for Rook on [1,2] with [2,2] occupy"

## TEST 1: GameNode cration. an Generating a list of movements on a game by piece

print "TEST 1"

print "Building a Game Node"
listPiecesWhite=[]
listPiecesBlack=[]
p1=Piece('Q',[2,1])
p2=Piece('N',[2,2])
p3=Piece('q',[1,4])
listPiecesWhite.append(p1)
listPiecesWhite.append(p2)
listPiecesBlack.append(p3)

gameNode=GameNode(listPiecesWhite,listPiecesBlack,"white")
assert(genListMovsPiece(gameNode,p3)==[[2,4],[3,4],[4,4],[1,1],[1,2],[1,3],[2,3],[3,2],[4,1]])
assert(not checkPieceMovValid(gameNode,p3,[4,2])) # Black Queen cannot move to [4,2], ilegal move
print "Checked movements for black queen"
assert(not checkPieceMovValid(gameNode,p2,[4,4])) # White Knight cannot move to [4,4], ilegal move
print "Checked movements for white knight"
assert(not checkPieceMovValid(gameNode,p1,[2,4])) # White Queen cannot move to [2,4], White Knight in the middle
assert(not checkPieceMovValid(gameNode,p1,[2,2])) # White Queen cannot move to [2,2], White Knight on it
print "Checked movements for white queen"

#print genListMovsPiece(gameNode,p1)

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


# TEST 2: Check whether white win after a queen eat movement
print "TEST 2"
####
listPiecesWhite=[]
listPiecesBlack=[]
p1=Piece('Q',[2,1])
listPiecesWhite.append(p1)
p2=Piece('q',[1,4])
listPiecesBlack.append(p2)

gameNode=GameNode(listPiecesWhite,listPiecesBlack,"white")
mov=[1,1]
piece=p1
gameNodeChild=gameNode.succesGameActionMove(piece,mov)

assert(not gameNode.checkWhiteWin())
print gameNodeChild.numBlackPieces()
assert(gameNodeChild.numBlackPieces()==1)
#gameNodeChild.draw()
assert(not gameNodeChild.checkWhiteWin())
assert(gameNodeChild.numBlackPieces()==1)
mov=[1,4] # position of black queen
piece=p2 # capturing black queen by white knight
gameNodeChild=gameNode.succesGameActionMove(piece,mov)
#gameNodeChild.draw()
#assert(gameNodeChild.checkWhiteWin())
#assert(gameNodeChild.numBlackPieces()==0)

# TEST 3: Generate all games nodes since a given game
print "TEST 3"
listGameNodes=genListNextGameNodesForcingColor(gameNode,"black")
#assert(len(listGameNodes)==9)
listGameNodes=genListNextGameNodesForcingColor(gameNode,"white")
#assert(len(listGameNodes)==10)
listGameNodes=genListNextGameNodes(gameNode)
#assert(len(listGameNodes)==10)

# TEST 4: Game succesors
print "TEST 4"

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


# Test 5: Apply MiniMax to gameNode
print "TEST 5"
#depth=2
#print MinimaxDecision(gameNode,depth)

#depth=1
#print MinimaxDecision(gameNode,depth)
#depth=4
#print MinimaxDecision(gameNode,depth)
#print MinMax(gameNode,depth,True)


print "Checking GameNode class"
listPiecesWhite=[]
listPiecesBlack=[]
listPiecesWhite.append(Piece('Q',[4,3]))
listPiecesWhite.append(Piece('N',[3,1]))
listPiecesWhite.append(Piece('R',[1,4]))
listPiecesWhite.append(Piece('R',[1,1]))

listPiecesBlack.append(Piece('q',[2,2]))
listPiecesBlack.append(Piece('r',[2,1]))
listPiecesBlack.append(Piece('r',[4,1]))

gameNode=GameNode(listPiecesWhite,listPiecesBlack,"white")

print "Check Rook Targets"
print "Targets Black Rook (r) at [2,1] -> "
for p in listTargetsRook(gameNode,Piece('r',[2,1])):    
    print p.type," ",p.coordenates

print "Targets White Rook (R) at [1,1] -> "
for p in listTargetsRook(gameNode,Piece('R',[1,1])):
    print p.type," ",p.coordenates

print "Targets White Rook (R) at [4,1] -> "
print listTargetsRook(gameNode,Piece('r',[4,1]))
for p in listTargetsRook(gameNode,Piece('r',[4,1])):
    print p.type," ",p.coordenates
    

depth=4
#print MinimaxDecision(gameNode,depth)
#print MinMax(gameNode,depth,True)


listPiecesWhite=[]
listPiecesBlack=[]
w1=Piece('Q',[3,1])
w2=Piece('N',[3,2])
w3=Piece('N',[4,2])
w4=Piece('B',[1,3])
listPiecesWhite.append(w1)
listPiecesWhite.append(w2)
listPiecesWhite.append(w3)
listPiecesWhite.append(w4)

b1=Piece('q',[1,2])
listPiecesBlack.append(b1)

gameNode=GameNode(listPiecesWhite,listPiecesBlack,"white")

depth=5
#print MinimaxDecision(gameNode,depth)

#print "Calculating MinMax: Sample 1"
#print "Results minimax (0 draw / 1 white win / -1 blach win : ",MinMax(gameNode,depth,True)

listPiecesWhite=[]
listPiecesBlack=[]
w1=Piece('Q',[2,2])
w2=Piece('N',[3,2])
w3=Piece('N',[4,2])
w4=Piece('B',[1,3])
listPiecesWhite.append(w1)
listPiecesWhite.append(w2)
listPiecesWhite.append(w3)
listPiecesWhite.append(w4)

b1=Piece('q',[1,2])
listPiecesBlack.append(b1)

#gameNode=GameNode(listPiecesWhite,listPiecesBlack,"black")

#gameNode.draw()
#print genListMovsPiece(gameNode,b1)

