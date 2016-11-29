#!/usr/bin/python
from piece import Piece
from gameNode import GameNode        
from functions import *
from minmax import MinMax

## TEST 1: GameNode cration. Generating list of movements on a game node by piece
print "TEST 1: Building a Game Node"
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
print "Checked movements for black queen: Black Queen cannot move to [4,2], ilegal move"
assert(not checkPieceMovValid(gameNode,p2,[4,4])) # White Knight cannot move to [4,4], ilegal move
print "Checked movements for white knight: White Knight cannot move to [4,4], ilegal move"
assert(not checkPieceMovValid(gameNode,p1,[2,4])) # White Queen cannot move to [2,4], White Knight in the middle
print "Checked movements for white queen: White Queen cannot move to [2,4], cose white Knight in the middle"
assert(not checkPieceMovValid(gameNode,p1,[2,2])) # White Queen cannot move to [2,2], White Knight on it
print "Checked movements for white queen: White Queen cannot move to [2,2], cose white Knight is over it"


# Game Successors
print "--"
print "TEST 2: Check whether white wins after a queen do an eat movement"
####
listPiecesWhite=[]
listPiecesBlack=[]
p1=Piece('Q',[2,1])
listPiecesWhite.append(p1)
p2=Piece('q',[1,4])
listPiecesBlack.append(p2)

gameNode=GameNode(listPiecesWhite,listPiecesBlack,"white")
print gameNode.draw()
mov=[1,1]
piece=p1
gameNodeChild=gameNode.succesGameActionMove(piece,mov)
print gameNodeChild.draw()

assert(not gameNode.checkWhiteWin())
print "Num black pieces:", gameNodeChild.numBlackPieces()
assert(gameNodeChild.numBlackPieces()==1)
#gameNodeChild.draw()
assert(not gameNodeChild.checkWhiteWin())
print "Checked that white not win"
assert(gameNodeChild.numBlackPieces()==1)
mov=[1,4] # position of black queen
piece=p2 # capturing black queen by white knight
gameNodeChild=gameNode.succesGameActionMove(piece,mov)
#gameNodeChild.draw()
#assert(gameNodeChild.checkWhiteWin())
#assert(gameNodeChild.numBlackPieces()==0)



print "--"
print "TEST 3:  Generate all games nodes since a given game"
listGameNodes=genListNextGameNodesForcingColor(gameNode,"black")
assert(len(listGameNodes)==9)
print "Number for black choises is 9"
listGameNodes=genListNextGameNodesForcingColor(gameNode,"white")
assert(len(listGameNodes)==9)
print "Number for white choises is 9"
listGameNodes=genListNextGameNodes(gameNode)
#assert(len(listGameNodes)==10)


