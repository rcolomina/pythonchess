#!/usr/bin/python

from piece import Piece
from gameNode import GameNode        

# Inputs: This function accepts as first arg. a coordenate from a knight piece located at coord and
#         as a second arg. all pieces that are in game ocupy
# Return: A list of all possible movements i.e pairs [x,y] not capturing pieces are returned
def listMovKnight(coord,ocupyCells):

    maxsize=5 # max size gameboard
    
    l=[]
    x=coord[0]
    y=coord[1]
    l=[[x+1,y+2],[x+2,y+1],[x+1,y-2],[x+2,y-1],[x-1,y-2],[x-2,y-1],[x-1,y+2],[x-2,y+1]]
    
    lfinal=[]
    for p in l:
        if p[0]>0 and p[0]<maxsize and p[1]>0 and p[1]<maxsize:
            lfinal.append(p)

    return [p for p in lfinal if p not in ocupyCells]

# Inputs: This function accepts a coordenate from a knight piece located at coord and a game node
#         As second arg. accets a knight piece type

# Return: A list of all possible adversary captures for an input bishop i.e pairs [x,y] 
def listTargetsKnight(gameNode,piece):        

    maxsize=5 # max size gameboard
    
    l=[]
    x=piece.coordenates[0]
    y=piece.coordenates[1]
    l=[[x+1,y+2],[x+2,y+1],[x+1,y-2],[x+2,y-1],[x-1,y-2],[x-2,y-1],[x-1,y+2],[x-2,y+1]]
    
    lfinal=[]
    for p in l:
        if p[0]>0 and p[0]<maxsize and p[1]>0 and p[1]<maxsize:
            lfinal.append(p)

    #print "lfinal:",lfinal
    targetsCoordenates=[]
    targetsCoordenates=[p for p in gameNode.allPieces if piece.colour()!=p.colour() and p.coordenates in lfinal]    
    #for p in targetsCoordenates:
    #    print p
    
    return targetsCoordenates
