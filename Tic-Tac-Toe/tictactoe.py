"""
This is a classic Tic-Tac-Toe game where any two people can play with it.
Each of them should put their name and the symbol they want to use.
But if any one of them use any empty character or null then the program will
raise exception error. So never use empty character.
"""

class Player:
    def __init__(self,name: str,symbol: str):
        if self.__check_name(name):
            self.__name = name 
        else:
            raise InvalidNameException("Empty Space can't be a name!!")     # Raise exception if invalid name is used

        if self.__check_symbol(symbol):
            self.__symbol = symbol
        else:
            raise InvalidSymbolException("Empty Space can't be a symbol!!") # Raise exception if invalid symbol is used 
    
    def __check_name(self,name: str):
        if name == ' ' or len(name)==0:
            return False 
        return True

    def __check_symbol(self,symbol: str):
        if symbol == ' ' or len(symbol)==0:
            return False
        return True

    @property
    def symbol(self):
        return self.__symbol
    
    @symbol.setter
    def symbol(self,symbol: str):
        if self.__check_symbol(symbol):
            self.__symbol = symbol

    @property
    def name(self):
        return self.__name 
    
    @name.setter
    def name(self,name: str):
        if self.__check_name(name):
            self.__name = name 

class Board:
    def __init__(self,p1Symbol: str,p2Symbol: str):
        self.__p1Symbol = p1Symbol
        self.__p2Symbol = p2Symbol
        self.boardSize = 3
        self.count = 0
        self.EMPTY = ' '
        self.PLAYER1WINS = 1   # Take 5 different conditions that might occur
        self.PLAYER2WINS = 2   # when any one of them make a move
        self.DRAW = 3
        self.INCOMPLETE = 4
        self.INVALIDMOVE = 5
        self.board = [[self.EMPTY for j in range(self.boardSize)] for i in range(self.boardSize)] # Intialize our board with empty characters

    def move(self,symbol: str,x: int,y: int):
        if x<0 or x>=self.boardSize or y<0 or y>= self.boardSize or self.board[x][y] != self.EMPTY:
            return self.INVALIDMOVE
        self.board[x][y] = symbol
        self.count += 1
        
        # Check Row-wise match
        if self.board[x][0]==self.board[x][1] and self.board[x][0]==self.board[x][2]:
            return self.PLAYER1WINS if symbol==self.__p1Symbol else self.PLAYER2WINS

        # Check Column-wise match
        if self.board[0][y]==self.board[1][y] and self.board[0][y]==self.board[2][y]:
            return self.PLAYER1WINS if symbol==self.__p1Symbol else self.PLAYER2WINS
        
        # Check Diagonally match
        if self.board[0][0]!=self.EMPTY and self.board[x][0]==self.board[x][1] and self.board[x][0]==self.board[x][2]:
            return self.PLAYER1WINS if symbol==self.__p1Symbol else self.PLAYER2WINS

        if self.board[0][2]!=self.EMPTY and self.board[0][2]==self.board[1][1] and self.board[0][2]==self.board[2][0]:
            return self.PLAYER1WINS if symbol==self.__p1Symbol else self.PLAYER2WINS
        
        # If the entire board is filled but nobody wins
        if self.count==self.boardSize*self.boardSize:
            return self.DRAW

        return self.INCOMPLETE

    def print(self):
        print("---------------")
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                print("| "+self.board[i][j]+" |",end="")
            print()
        print()
        print("---------------")


class TicTacToe:
    def __init__(self):
        self.__numPlayers = 0   # Initalize number of players with 0
    
    def startGame(self):
        self.__numPlayers += 1  # Incrementing by 1
        player1 = self.takePlayerInput(self.__numPlayers)

        self.__numPlayers += 1  # Incrementing by 1 again
        player2 = self.takePlayerInput(self.__numPlayers)
        
        while player1.symbol == player2.symbol:          # If two symbols are same then player2 has to make a change
            print("Symbol is already taken\nPlease enter the symbol again")
            player2.symbol = input()

        board = Board(player1.symbol,player2.symbol)     # Here we create our board object 
        player1Turn = True 
        status = board.INCOMPLETE
        while status==board.INCOMPLETE or status==board.INVALIDMOVE: 
            if player1Turn:
                print("Player 1 - "+player1.name+"'s turn")
                print("Enter x: ")
                x = int(input())
                print("Enter y: ")
                y = int(input())
                status = board.move(player1.symbol,x,y)
                if status==board.INVALIDMOVE:            # If player1 make an invalid move
                    print("Invalid move!! Please try again!")
                    continue
            else:
                print("Player 2 - "+player2.name+"'s turn")
                print("Enter x: ")
                x = int(input())
                print("Enter y: ")
                y = int(input())
                status = board.move(player2.symbol,x,y)
                if status==board.INVALIDMOVE:           # If player2 make an invalid move
                    print("Invalid move!! Please try again!")
                    continue
            player1Turn = not (player1Turn)
            board.print()
        
        if status==board.PLAYER1WINS:
            print("Player 1 - "+player1.name+" wins!!")
        elif status==board.PLAYER2WINS:
            print("Player 2 - "+player2.name+" wins!!")
        else:
            print("DRAW!!")

    def takePlayerInput(self,num: int):
        print("Enter Player "+str(num)+" name: ")
        name = input()
        print("Enter Player "+str(num)+" symbol: ")
        symbol = input()[0]
        p = Player(name,symbol)   # Creating Player object
        return p 

class InvalidNameException(Exception):
    def __init__(self,message=None):
        self.message = message
    
    def __str__(self):
        if self.message==None:
            return None
        else:
            return self.message

class InvalidSymbolException(Exception):
    def __init__(self,message=None):
        self.message = message
    
    def __str__(self):
        if self.message==None:
            return None
        else:
            return self.message

if __name__=="__main__":
    t = TicTacToe()
    t.startGame()