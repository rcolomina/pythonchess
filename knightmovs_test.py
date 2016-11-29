#!/usr/bin/python

from piece import Piece
from gameNode import GameNode
from knightmovs import *
from functions import *


listPiecesWhite=[]
listPiecesBlack=[]
w1=Piece('Q',[3,1])
w2=Piece('N',[3,2])
w3=Piece('N',[4,2])
w4=Piece('B',[2,3])
listPiecesWhite.append(w1)
listPiecesWhite.append(w2)
listPiecesWhite.append(w3)
listPiecesWhite.append(w4)

b1=Piece('q',[3,4])
listPiecesBlack.append(b1)

gameNode=GameNode(listPiecesWhite,listPiecesBlack,"white")


assert(listTargetsKnight(gameNode,w3)==[[3,4]])
print "Checked knight movements on ",w2.coordenates," which should be ",listTargetsKnight(gameNode,w3)
