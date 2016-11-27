#!/usr/bin/python

from piece import Piece
from gameNode import GameNode
from minmax import MinMax
from functions import *


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
succesors=genListNextGameNodes(gameNode)


#n1=gameNode.succesGameActionMove(w1,[4,1])
#n2=n1.succesGameActionMove(b1,[3,4])
#n2.draw()
#print "Knight movements:",genListMovsPiece(n2,Piece('N',[4,2]))

#for s in succesors:
#    print s.lastPieceMoved.type," ",s.lastPieceMoved.coordenates," lastMov:",s.lastMov
#    secondSuccesors=genListNextGameNodes(s)
#    for s2 in secondSuccesors:
#        print "     ",s2.lastPieceMoved.type," ",s2.lastPieceMoved.coordenates," lastMov:",s2.lastMov," utility:",s2.utility()
#        thirdSuccesors=genListNextGameNodes(s2)
#        if len(thirdSuccesors)>0:
#            nodeWiner=max(thirdSuccesors,key=lambda p: p.utility())
#            print "            ",nodeWiner.lastPieceMoved.type," ",nodeWiner.lastPieceMoved.coordenates," lastMov:",nodeWiner.lastMov," utility:",nodeWiner.utility()

        #for s3 in thirdSuccesors:
         #   print "            ",s3.lastPieceMoved.type," ",s3.lastPieceMoved.coordenates," lastMov:",s3.lastMov," utility:",s3.utility()

        
    
depth=3
print "Calculating MinMax: Sample 1"
print "Results minimax (0 draw / 1 white win / -1 blach win : ",MinMax(gameNode,depth,True)
print MinMax(gameNode,depth,depth)











