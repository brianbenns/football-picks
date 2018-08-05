from class_Pick import NFLPick

class Player:
    def __init__(self, name='', picks=None, best_bet=None, ou=None):
        self.name = name
        if picks:
            self.picks=picks
        else:
            self.picks = [] 
    def addPick(self, pick):
        self.picks.append(pick)
    def setBestBet(self, best_bet):
        self.best_bet = best_bet
    def setOU(self, ou):
        self.ou = ou
    def calc_score(self, completedOnly = False):
        score = 0
        if not completedOnly:
            for pick in self.picks:
                if pick.isTied():
                    score = score + 0.5
                elif pick.isWinning():
                    score = score + 1
            if self.ou.isTied():
                score = score + 0.5
            elif self.ou.isWinning():
                score = score + 1
            if self.best_bet.isTied():
                score = score + 1
            elif self.best_bet.isWinning():
                score = score + 2
        else:
            for pick in self.picks:
                if pick.isTied() and pick.completed:
                    score = score + 0.5
                elif pick.isWinning() and pick.completed:
                    score = score + 1
            if self.ou.isTied() and self.ou.completed:
                score = score + 0.5
            elif self.ou.isWinning() and self.ou.completed:
                score = score + 1
            if self.best_bet.isTied() and self.best_bet.completed:
                score = score + 1
            elif self.best_bet.isWinning() and self.best_bet.completed:
                score = score + 2
        return score
                