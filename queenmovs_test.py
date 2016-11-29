#!/usr/bin/python

from piece import Piece
from gameNode import GameNode        
from minmax import MinMax

from queenmovs import *

print "Checking GameNode class constructur"

listPiecesWhite=[]
listPiecesBlack=[]

w1=Piece('Q',[4,3])
w2=Piece('R',[1,4])
w3=Piece('R',[1,1])
w4=Piece('N',[3,1])
w5=Piece('N',[2,4])

b1=Piece('q',[2,2])
b2=Piece('r',[2,1])
b3=Piece('r',[4,1])
b4=Piece('n',[1,3])

listPiecesWhite=[w1,w2,w3,w4,w5]
listPiecesBlack=[b1,b2,b3,b4]

gameNode=GameNode(listPiecesWhite,listPiecesBlack,"white")

gameNode.draw()

print "Check Queen Targets"
print "Targets Black (q) at [2,2] -> "
for p in listTargetsQueen(gameNode,b1):
    print p.type," ",p.coordenates

pieces=[]
for p in listTargetsQueen(gameNode,w1):
    print p.type," ",p.coordenates
    pieces.append([p.type,p.coordenates])
    
assert(pieces==[['n', [1, 3]], ['r', [4, 1]], ['r', [2, 1]]])
print "Assertion over white queen list of targets: ",pieces
