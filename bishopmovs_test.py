#!/usr/bin/python

from piece import Piece
from gameNode import GameNode        
from bishopmovs import *

print "Checking GameNode class constructur"


w1=Piece('Q',[2,2])
w2=Piece('N',[3,2])
w3=Piece('N',[4,2])
w4=Piece('B',[1,3])
w5=Piece('B',[2,4])
listPiecesWhite=[]
listPiecesWhite=[w1,w2,w3,w4,w5]


b1=Piece('q',[1,2])
b2=Piece('n',[3,1])
b3=Piece('r',[1,1])
b4=Piece('b',[4,4])
listPiecesBlack=[]
listPiecesBlack=[b1,b2,b3,b4]

gameNode=GameNode(listPiecesWhite,listPiecesBlack,"black")

print "Targets for white bishop"
#listTargetsBishop(gameNode,w1)
for p in listTargetsBishop(gameNode,w1):
    print p.type
    
listCoordenates=[p.coordenates for p in gameNode.allPieces]
print listCoordenates

print "Movements for white bishop (no targets)"
for p in listMovBishop(w1.coordenates,listCoordenates):
    print p
