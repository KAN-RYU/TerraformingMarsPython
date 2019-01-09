import player
import board

class Game:
    def __init__(self, num_of_player):
        #Add players
        self.players = []
        for i in range(num_of_player):
            self.players.append(player())

        #Expansion check
        self.useHE = False
        self.useVN = False
        self.usePR = False

        if(self.useHE):
            self.board = board('random', self.useVN)
        else:
            self.board = board('base', self.useVN)

