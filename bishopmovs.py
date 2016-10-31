#!/usr/bin/python

from piece import Piece
from gameNode import GameNode        

# Inputs: This function accept a coordenate of a bishop piece located at coord and a set of 
#         all pieces of the game ocupy
# Return: A list of all possible movements i.e pairs [x,y] not capturing pieces are returnet
def listMovBishop(coord,ocupyCells):

    # List to store Rook movements
    listMovs=[]

    # Coordenates from the input piece
    coorx=coord[0]
    coory=coord[1]
    
    #Diagonal1
    diagonal=[[coorx+t,coory+t] for t in range(-4,5)
        if (coorx+t)<5 and (coorx+t)>0 and (coory+t)<5 and (coory+t)>0]

    # Getting pieces at left and right of the current piece
    leftPieces=[x for [x,y] in ocupyCells if [x,y] in diagonal and x<coorx]
    rightPieces=[x for [x,y] in ocupyCells if [x,y] in diagonal and x>coorx]

    #print "leftPieces:",leftPieces
    #print "rightPieces:",rightPieces
        
    leftPieces.sort()
    rightPieces.sort()

    mostRightAtLeftPiece=[0 if len(leftPieces)==0 else leftPieces.pop()].pop()
    mostLeftAtRightPiece=[5 if len(rightPieces)==0 else rightPieces[0]].pop()

    #print "mostRightAtLeftPiece:",mostRightAtLeftPiece
    #print "mostLeftAtRightPiece:",mostLeftAtRightPiece
    
    d1=[[coorx+t,coory+t] for t in range(-4,5)
        if (coorx+t)<mostLeftAtRightPiece and (coorx+t)>mostRightAtLeftPiece and (coory+t)<5 and (coory+t)>0]
    
    d1.remove([coorx,coory])
    #print "Diagonal1:",d1
    
    #Diagonal2
    diagonal=[[coorx+t,coory-t] for t in range(-4,5)
        if coorx+t<5 and (coorx+t)>0 and (coory-t)<5 and (coory-t)>0]

    leftPieces=[x for [x,y] in ocupyCells if [x,y] in diagonal and x<coorx]
    rightPieces=[x for [x,y] in ocupyCells if [x,y] in diagonal and x>coorx]

    leftPieces.sort()
    rightPieces.sort()

    mostRightAtLeftPiece=[0 if len(leftPieces)==0 else leftPieces.pop()].pop()
    mostLeftAtRightPiece=[5 if len(rightPieces)==0 else rightPieces[0]].pop()

    d2=[[coorx+t,coory-t] for t in range(-4,5)
        if (coorx+t)<mostLeftAtRightPiece and (coorx+t)>mostRightAtLeftPiece and (coory-t)<5 and (coory-t)>0]    
    d2.remove([coorx,coory])

    listMovs.extend(d1)
    listMovs.extend(d2)
    
    return listMovs




# Inputs: This function accept a coordenate of bishop piece located at coord and a game node
#
# Return: A list of all possible adversary captures for an input bishop i.e pairs [x,y] 
def listTargetsBishop(gameNode,piece):        

    listOfTargets=[]
    coord=piece.coordenates

    cX=piece.coordenates[0]
    cY=piece.coordenates[1]
    
    # First Diagonal \
    #Diagonal1: Equations that rules diagonal are -->  d=y+x => y=d-x
    diff=cY+cX
    firstDiagonalTargets=[p for p in gameNode.allPieces if p.coordenates[1]==diff-p.coordenates[0]]

    # print piecesDiagonal
    firstDiagonalTargets.sort(key=lambda x:x.coordenates,reverse=False)

    if len(firstDiagonalTargets)>0:
        index = firstDiagonalTargets.index(piece)
        previous_value = firstDiagonalTargets[index-1] if index-1>=0 else None
        next_value = firstDiagonalTargets[index+1] if index+1<len(firstDiagonalTargets) else None
        
        if previous_value!=None:            
            if piece.colour()!=previous_value.colour():
                listOfTargets.append(previous_value)

        if next_value!=None:
            if piece.colour()!=next_value.colour():
                listOfTargets.append(next_value)        

    # Second Diagonal    
    #Diagonal1: Equations that rules diagonal are -->  d=y-x => y=x+d
    diff=cY-cX
    secondDiagonalTargets=[p for p in gameNode.allPieces if p.coordenates[1]==diff+p.coordenates[0]]
                
    # print piecesDiagonal
    secondDiagonalTargets.sort(key=lambda x:x.coordenates,reverse=False)

    if len(secondDiagonalTargets)>0:
        index = secondDiagonalTargets.index(piece)
        previous_value = secondDiagonalTargets[index-1] if index-1>=0 else None
        next_value = secondDiagonalTargets[index+1] if index+1<len(secondDiagonalTargets) else None
        
        if previous_value!=None:            
            if piece.colour()!=previous_value.colour():
                listOfTargets.append(previous_value)

        if next_value!=None:
            if piece.colour()!=next_value.colour():
                listOfTargets.append(next_value)        

                
    return listOfTargets
    
