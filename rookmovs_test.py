from piece import Piece
from gameNode import GameNode        
from functions import *
from minmax import MinMax

print "Checking GameNode class constructur"

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

#pairs=[['Q',[4,3]],['N',[3,1]],['R',[1,4]],['R',[1,1]],
#       ['q',[2,2]],['r',[2,1]],['r',[4,1]]]

#gameNode=GameNode.buildWithPairs(pairs,"white")
#gameNode.draw()

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
