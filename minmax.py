from piece import Piece
from gameNode import GameNode        
from functions import *

## Minimax algorithm
def MinMax(gameNode,depth,maxPlayer):


    #if gameNode.turnNumber==2:
     #   gameNode.draw()

    
    result=Utility(gameNode)
    if depth==0:
        return result
    
    if maxPlayer:
        bestValue=-1
        succesors=genListNextGameNodes(gameNode)
        for s in succesors:           
            val=MinMax(s,depth-1,False)
            bestValue=max(bestValue,val)
            #print s.lastPieceMoved.type," ",s.lastPieceMoved.coordenates," Utility:",Utility(s)
        #print "Depth:",depth," Max "  ,gameNode.lastPieceMoved.type, " BestValue:",bestValue, " Num. Succesors:", len(succesors)," White Win:",gameNode.checkWhiteWin(), " Turn Number:", gameNode.turnNumber
        #if gameNode.checkWhiteWin():
        #    gameNode.draw()
        return bestValue
    else:
        bestValue=1
        succesors=genListNextGameNodes(gameNode)                          
        for s in succesors:
            #print  "Depth:",depth, " Min " ,s.lastPieceMoved.type
            val=MinMax(s,depth-1,True)
            bestValue=min(bestValue,val)
            #print s.lastPieceMoved.type," ",s.lastPieceMoved.coordenates," Utility:",Utility(s)
        #print "Depth:",depth," Min "  ,gameNode.lastPieceMoved.type, " BestValue:",bestValue, " Num. Succesors:", len(succesors)," White Win:",gameNode.checkWhiteWin(), " Turn Number:", gameNode.turnNumber
        #if gameNode.checkWhiteWin():
        #    gameNode.draw()
        return bestValue
