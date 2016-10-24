
class Piece:
    def __init__(self, type, coordenates):
        self.type = type
        self.coordenates = coordenates
        
    def isWhite(self):
        return piece.type.isupper()
    
    def isBlack(self):
        return not piece.type.isupper()
        
    def colour(self):
        if self.type.isupper():
            return "white"
        else:
            return "black"

    def draw(self):
        print "(",self.type,",",self.coordenates,")"
 
