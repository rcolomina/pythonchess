from piece import Piece

class GameNode:
    def __init__(self, listPiecesWhite,listPiecesBlack,colourPlayer):
        self.listPiecesWhite = listPiecesWhite
        self.listPiecesBlack = listPiecesBlack
        self.allPieces=[]
        self.allPieces.extend(listPiecesWhite)
        self.allPieces.extend(listPiecesBlack)
        self.listCoordsWhite=[]
        self.listCoordsBlack=[]
        self.addCoord()
        self.colourPlayer=colourPlayer        
        self.lastPieceMoved=Piece("Root",[0,0])
        self.lastMov=[]
        self.turnNumber=0

    def buildWithPairs(self,pairs,colourPlayer):
        piecesWhite=[]
        piecesBlack=[]
        for pair in pairs:
            if pair.type.isupper():
                piecesWhite.append(Piece(pair.type,pair.coordenates))
            else: 
                piecesBlack.append(Piece(pair.type,pair.coordenates))
        return GameNode(piecesWhite,piecesBlack,colourPlayer)
   
        
    def addCoord(self):    
        for piece in self.listPiecesBlack:
           self.listCoordsBlack.append(piece.coordenates)
        #print self.listCoordsBlack

        for piece in self.listPiecesWhite:
           self.listCoordsWhite.append(piece.coordenates)
        #print self.listCoordsWhite

    def numBlackPieces(self):
        return len(self.listPiecesBlack)

    def numWhitePieces(self):
        return len(self.listPiecesWhite)
        
    def draw(self):
        print "** TURN GAME ** :", self.turnNumber
        for piece in self.listPiecesWhite:
            print piece.type," -> (","ABCD"[piece.coordenates[0]-1],",",piece.coordenates[1],")"
        for piece in self.listPiecesBlack:
            print piece.type," -> (","ABCD"[piece.coordenates[0]-1],",",piece.coordenates[1],")"
        print "White has ",self.numWhitePieces()," pieces","  | Black has ",self.numBlackPieces()," pieces"
        print "White Win: ",['NO','YES'][self.checkWhiteWin()]
        if self.lastPieceMoved.type!='Root':
            print "Last Piece Moved:",self.lastPieceMoved.type," From:",self.lastPieceMoved.coordenates," To:",self.lastMov
        else:
            print "Starting Position"
        if not self.checkWhiteWin():
            print "Next player:",self.colourPlayer
        else:
            print "TERMINAL NODE"
                    
    # Check if Black has still its queen
    def checkWhiteWin(self):
        for piece in self.listPiecesBlack:
            if piece.type=="q":
                return False
        return True
    
    # Check if White has still its queen
    def checkBlackWin(self):
        for piece in self.listPiecesWhite:
            if piece.type=="Q":
                return False
        return True    
                
    def genListPiecesWhite(self,piece,mov):
        newListPiecesWhite=[]
        for p in self.listPiecesWhite:
            if p!=piece:
                newListPiecesWhite.append(p)

        for p in newListPiecesWhite:
            if p.coordenates==mov or p.coordenates==piece.coordenates:
                newListPiecesWhite.remove(p)

        if piece.type.isupper():
            newPiece=Piece(piece.type,mov)
            newListPiecesWhite.append(newPiece)
            
        return newListPiecesWhite
                
    def genListPiecesBlack(self,piece,mov):
        newListPiecesBlack=[]
        for p in self.listPiecesBlack:
            if p!=piece:
                newListPiecesBlack.append(p)

        for p in newListPiecesBlack:
            if p.coordenates==mov or p.coordenates==piece.coordenates:
                newListPiecesBlack.remove(p)
                
        if not piece.type.isupper():
            newPiece=Piece(piece.type,mov)
            newListPiecesBlack.append(newPiece)
        
        return newListPiecesBlack
                                
    # This guess that movement is legal (a color not eat itself)
    # piece and mov must be validated previously to call this function
    def succesGameActionMove(self,piece,mov):
            
        # Change Player Turn for the game succesor
        if self.colourPlayer=="black":
            colorNextPlayer="white"
        else:
            colorNextPlayer="black"

        # Generate new list due to move piece into coordenates mov
        newListPiecesWhite=self.genListPiecesWhite(piece,mov)
        newListPiecesBlack=self.genListPiecesBlack(piece,mov)
                
        # Create new game succesor
        gameSuccesor=GameNode(newListPiecesWhite,newListPiecesBlack,colorNextPlayer)
        gameSuccesor.lastPieceMoved=piece
        gameSuccesor.lastMov=mov
        gameSuccesor.turnNumber=self.turnNumber+1
        return gameSuccesor

    # Gete List of Pieces that can be moved for the current player
    def listPiecesToMove(self):
        if self.colourPlayer=="black":
            return self.listPiecesBlack
        else:
            return self.listPiecesWhite


    def utility(self):
        if self.checkWhiteWin():
            return 1
        else:
            if self.checkBlackWin():
                return -1
            else:
                return 0        
