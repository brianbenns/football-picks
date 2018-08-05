import nflgame
from datetime import datetime, timedelta

class NFLPick:
    #spread is always in perspective of the home team
    def __init__(self, home='', away='', pickType='Spread', spread=None, home_pick=None, total=None, over_pick=None, best_bet=False):
        self.home = home
        self.away = away  
        self.best_bet = best_bet
        self.pickType = pickType
        self.completed = False
        self.inProgress = False
        self.home_score = 0
        self.away_score = 0
        self.updatedAt = datetime.min
        if pickType == 'Spread':
            self.spread = spread
            self.home_pick = home_pick
            plus = '+' if spread > 0  else ''
            if home_pick:
                plus = '+' if spread > 0  else ''
                self.pick_string = '{} {}{}'.format(home, plus, spread)
            else:
                awaySpread = -1*self.spread
                plus = '+' if awaySpread > 0  else ''
                self.pick_string = '{} {}{}'.format(away, plus, awaySpread)
        elif pickType == 'Total':
            self.total = total
            self.over_pick = over_pick
            if over_pick:
                self.pick_string = 'OVER {}'.format(total)
            else:
                self.pick_string = 'UNDER {}'.format(total)
        else:
            raise BaseException()
    def isTied(self):
        if datetime.now() - self.updatedAt > timedelta(seconds=30):
            self.update()
        if not self.inProgress and not self.completed:
            return False
        if self.pickType == 'Spread':
            return self.home_score + self.spread == self.away_score
        else:
            return self.home_score + self.away_score == self.total
    def isWinning(self):
        if datetime.now() - self.updatedAt > timedelta(seconds=30):
            self.update()
        if not self.inProgress and not self.completed:
            return False
        if self.pickType == 'Spread':
            return (self.home_score + self.spread > self.away_score) == self.home_pick
        else:
            return (self.home_score + self.away_score > self.total) == self.over_pick
    def update(self):
        game = nflgame.one(2017, week=17, home=self.home, away=self.away)
        if game is None:
            home_score = 0
            away_score = 0
        else:
            if game.game_over():
                self.completed = True
            if game.playing():
                self.inProgress = True
            else:
                self.inProgress = False
            self.home_score = game.score_home
            self.away_score = game.score_away
        self.updatedAt = datetime.now()
    def status(self):
        if datetime.now() - self.updatedAt > timedelta(seconds=30):
            self.update()
        if self.inProgress:
            return 'IN PROGRESS'
        elif self.completed:
            return 'COMPLETED'
        else:
            return 'NOT STARTED'
    def css_class(self):
        if self.status()== 'IN PROGRESS':
            if self.isTied():
                return 'bg-warning'
            elif self.isWinning():
                return 'bg-success'
            else:
                return 'bg-danger'
        elif self.status() == 'COMPLETED':
            if self.isTied():
                return 'table-warning'
            elif self.isWinning():
                return 'table-success'
            else:
                return 'table-danger'
        else:
            return 'table-active'