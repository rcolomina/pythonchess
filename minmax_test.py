#!/usr/bin/python

from piece import Piece
from gameNode import GameNode
from minmax import MinMax

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

depth=2
#print "Calculating MinMax: Sample 1"
#print "Results minimax (0 draw / 1 white win / -1 blach win : ",MinMax(gameNode,depth,True)
print MinMax(gameNode,depth,depth)
