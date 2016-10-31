from piece import Piece
from gameNode import GameNode

# Inputs: This function accept a coordenate of a rook piece located at coord and a set of 
#         all pieces of the game ocupy
#
# Return: A list of all possible movements i.e pairs [x,y] not capturing pieces are returnet
def listMovRook(coord,ocupyCells):

    # List to store Rook movements
    listMovs=[]

    # Coordenates from the input piece
    coorx=coord[0]
    coory=coord[1]
    
    # Horizontal Posible Movemets
    leftPieces=[x for [x,y] in ocupyCells if x<coorx and y==coory]
    rightPieces=[x for [x,y] in ocupyCells if x>coorx and y==coory]

    # Sorting for safety
    leftPieces.sort()#(key=lambda x:x[0])
    rightPieces.sort()#(key=lambda x:x[0])
        
    #print leftPieces
    #print rightPieces
    
    mostRightAtLeftPiece=[0 if len(leftPieces)==0 else leftPieces.pop()].pop()
    mostLeftAtRightPiece=[5 if len(rightPieces)==0 else rightPieces[0]].pop()

    #print "mostRightAtLeftPiece:",mostRightAtLeftPiece
    #print "mostLeftAtRightPiece:",mostLeftAtRightPiece
    
    movsAtLeft=[[x,coory] for x in range(mostRightAtLeftPiece+1,coorx)]    
    #print "movsAtLeft:",movsAtLeft

    movsAtRight=[[x,coory] for x in range(coorx+1,mostLeftAtRightPiece)]    
    #print "movsAtRight:",movsAtRight

    # Vertical Posible Movemets
    downPieces=[y for [x,y] in ocupyCells if x==coorx and y<coory]
    upPieces=[y for [x,y] in ocupyCells if x==coorx and y>coory]

    #print downPieces
    
    # Sorting for safety
    downPieces.sort()#(key=lambda x:x[0])
    upPieces.sort()#(key=lambda x:x[0])
        
    #print "downPieces:",downPieces
    #print "upPieces:",upPieces

    mostUpAtDownPiece=[0 if len(downPieces)==0 else downPieces.pop()].pop()
    mostDownAtUpPiece=[5 if len(upPieces)==0 else upPieces[0]].pop()

    movsAtDown=[[coorx,y] for y in range(mostUpAtDownPiece+1,coory)]    
    #print "movsAtDown:",movsAtDown

    movsAtUp=[[coorx,y] for y in range(coory+1,mostDownAtUpPiece)]    
    #print "movsAtUp:",movsAtUp

    listMovs.extend(movsAtLeft)
    listMovs.extend(movsAtRight)
    listMovs.extend(movsAtDown)
    listMovs.extend(movsAtUp)

    return listMovs


# Inputs: This function accept a coordenate of a rook piece located at coord and a game node
#
# Return: A list of all possible adversary captures for an input the rook i.e pairs [x,y] 
def listTargetsRook(gameNode,piece):        

    listOfTargets=[]
    
    coord=piece.coordenates
    
    # filtering pieces on the same row
    horizontalTargets=[p for p in gameNode.allPieces if p.coordenates[1]==coord[1]]
    #for p in horizontalTargets:
    #    print "horizontalTargets:",p.type," ",p.coordenates
    
    horizontalTargets.sort(key=lambda x:x.coordenates,reverse=False)

    #print "horizontalTargets:",horizontalTargets

    if len(horizontalTargets)>0:
        if piece in horizontalTargets:
            index = horizontalTargets.index(piece)
            previous_value = horizontalTargets[index-1] if index-1>=0 else None
            next_value = horizontalTargets[index+1] if index+1<len(horizontalTargets) else None
            #print "index",index, "previous_value",previous_value," next_value:",next_value

            
            if previous_value!=None:            
                if piece.colour()!=previous_value.colour():
                    listOfTargets.append(previous_value)

            if next_value!=None:
            #print "piece.colour:",piece.colour()
            #print "next_value.colour:",next_value.colour()
                if piece.colour()!=next_value.colour():
                    listOfTargets.append(next_value)

    
                
    # Vertical
    verticalTargets=[p for p in gameNode.allPieces if p.coordenates[0]==coord[0]]

    verticalTargets.sort(key=lambda x:x.coordenates,reverse=False)

    if len(verticalTargets)>0:        
        if piece in verticalTargets:
            index = verticalTargets.index(piece)
            previous_value = verticalTargets[index-1] if index-1>=0 else None
            next_value = verticalTargets[index+1] if index+1<len(verticalTargets) else None

            #print "index",index, "previous_value",previous_value," next_value:",next_value

            # Append piece if is different of None and has different colour
            if previous_value!=None:            
                if piece.colour()!=previous_value.colour():
                    listOfTargets.append(previous_value)

            # Append piece if is different of None and has different colour
            if next_value!=None:            
                if piece.colour()!=next_value.colour():
                    listOfTargets.append(next_value)


    
            
    return listOfTargets
