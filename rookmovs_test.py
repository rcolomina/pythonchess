#!/usr/bin/python

from piece import Piece
from gameNode import GameNode        
from minmax import MinMax
from rookmovs import *


listMovs=listMovRook([1,2],[[2,2]])
assert(listMovs==[[1,1],[1,3],[1,4]])
print "checking listMovRook [OK]"


listPiecesWhite=[]
listPiecesBlack=[]

w1=Piece('Q',[4,3])
w2=Piece('R',[1,4])
w3=Piece('R',[1,1])
w4=Piece('N',[3,1])
w5=Piece('N',[2,3])
w6=Piece('R',[3,3])

b1=Piece('q',[2,2])
b2=Piece('r',[2,1])
b3=Piece('r',[4,1])
b4=Piece('n',[1,3])

listPiecesWhite=[w1,w2,w3,w4,w5,w6]
listPiecesBlack=[b1,b2,b3,b4]

gameNode=GameNode(listPiecesWhite,listPiecesBlack,"white")
print gameNode.draw()

print "Check Rook Targets"
print "Targets Black Rook (r) at [2,1] -> "
for p in listTargetsRook(gameNode,b2):    
    print p.type," ",p.coordenates

print "Targets White Rook (R) at [1,1] -> "
for p in listTargetsRook(gameNode,w3):
    print p.type," ",p.coordenates

print "Targets White Rook (r) at [4,1] -> "
for p in listTargetsRook(gameNode,b3):
    print p.type," ",p.coordenates

print "Targets White Rook (R) at [3,3] -> "
for p in listTargetsRook(gameNode,w6):
    print p.type," ",p.coordenates



listMovs=listMovRook([1,2],[[3,2]])
assert(listMovs==[[2,2],[1,1],[1,3],[1,4]])
print "Checked movements for Rook on [1,2] with [2,2] occupy"
