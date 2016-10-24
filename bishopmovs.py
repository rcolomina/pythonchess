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
