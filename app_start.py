import nflgame, time
from class_Pick import NFLPick
from class_Player import Player
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def template_home():
    players = app.config['PLAYERS']
    return render_template('home.html', players=players)
    
@app.route("/standings")
def template_standings():
    return render_template('standings.html')
    
@app.route("/makepicks")
def template_makepicks():
    games = app.config["GAMES"]
    return render_template('selectpicks.html', games=games)

def configure_app(players, games):
    app.config['PLAYERS'] = players
    app.config['GAMES'] = games
    return app

def get_pick(game_num, home_pick):
    game_dict = {
        1: NFLPick('BAL', 'CIN', spread=-9.5, home_pick=home_pick),
        2: NFLPick('DET', 'GB', spread=-6.5, home_pick=home_pick),
        3: NFLPick('MIA', 'BUF', spread=2.5, home_pick=home_pick),
        4: NFLPick('ATL', 'CAR', spread=-3.5, home_pick=home_pick),
        5: NFLPick('TB', 'NO', spread=7, home_pick=home_pick),
        6: NFLPick('TEN', 'JAX', spread=-3, home_pick=home_pick),
        7: NFLPick('NE', 'NYJ', spread=-15.5, home_pick=home_pick),
        8: NFLPick('IND', 'HOU', spread=-5, home_pick=home_pick),
        9: NFLPick('PIT', 'CLE', spread=-7, home_pick=home_pick),
        10: NFLPick('NYG', 'WAS', spread=3, home_pick=home_pick),
        11: NFLPick('MIN', 'CHI', spread=-12, home_pick=home_pick),
        12: NFLPick('LAC', 'OAK', spread=-8, home_pick=home_pick),
        13: NFLPick('SEA', 'ARI', spread=-9.5, home_pick=home_pick),
        14: NFLPick('DEN', 'KC', spread=-3.5, home_pick=home_pick),
        15: NFLPick('LA', 'SF', spread=3.5, home_pick=home_pick),
        16: NFLPick('PHI', 'DAL', spread=3, home_pick=home_pick)
    }
    return game_dict[game_num]
if __name__ == '__main__':
    
    David = Player('David')
    David.addPick(get_pick(3, False))
    David.addPick(get_pick(5, False))
    David.addPick(get_pick(15, False))
    David.addPick(get_pick(6, True))
    David.addPick(get_pick(2, True))
    David.addPick(get_pick(9, False))
    David.addPick(get_pick(14, True))
    David.addPick(get_pick(10, False))
    David.setBestBet(NFLPick('PHI', 'DAL', spread=3, home_pick=False, best_bet=True))
    David.setOU(NFLPick('MIA', 'BUF', pickType='Total', total=42.5, over_pick=False))
    
    Gary = Player('Gary')
    Gary.addPick(get_pick(6, False))
    Gary.addPick(get_pick(2, True))
    Gary.addPick(get_pick(8, True))
    Gary.addPick(get_pick(3, False))
    Gary.addPick(get_pick(4, False))
    Gary.addPick(get_pick(10, False))
    Gary.addPick(get_pick(14, True))
    Gary.addPick(get_pick(15, False))
    Gary.setOU(NFLPick('TB', 'NO', pickType='Total', total=50.5, over_pick=False))
    Gary.setBestBet(NFLPick('PHI', 'DAL', spread=3, home_pick=False, best_bet=True)) 
    
    Brian = Player('Brian')
    Brian.addPick(get_pick(6, False))
    Brian.addPick(get_pick(13, False))
    Brian.addPick(get_pick(15, False))
    Brian.addPick(get_pick(3, True))
    Brian.addPick(get_pick(16, False))
    Brian.addPick(get_pick(11, False))
    Brian.addPick(get_pick(7, False))
    Brian.addPick(get_pick(10, True))
    Brian.setOU(NFLPick('SEA', 'ARI', pickType='Total', total=38.5, over_pick=True))
    Brian.setBestBet(NFLPick('ATL', 'CAR', spread=-3.5, home_pick=False, best_bet=True)) 
 
    Naylor = Player('Naylor')
    Naylor.addPick(get_pick(12, True))
    Naylor.addPick(get_pick(16, False))
    Naylor.addPick(get_pick(3, False))
    Naylor.addPick(get_pick(6, False))
    Naylor.addPick(get_pick(14, True))
    Naylor.addPick(get_pick(1, False))
    Naylor.addPick(get_pick(8, True))
    Naylor.addPick(get_pick(13, True))
    Naylor.setOU(NFLPick('PHI', 'DAL', pickType='Total', total=39.5, over_pick=True))
    Naylor.setBestBet(NFLPick('LA', 'SF', spread=3.5, home_pick=False, best_bet=True)) 
    
    Pete = Player('Pete')
    Pete.addPick(get_pick(14, False))
    Pete.addPick(get_pick(7, False))
    Pete.addPick(get_pick(9, True))
    Pete.addPick(get_pick(3, False))
    Pete.addPick(get_pick(4, True))
    Pete.addPick(get_pick(8, False))
    Pete.addPick(get_pick(16, False))
    Pete.addPick(get_pick(6, True))
    Pete.setBestBet(NFLPick('TB', 'NO', spread=7, home_pick=False, best_bet=True))
    Pete.setOU(NFLPick('NE', 'NYJ', pickType='Total', total=43, over_pick=True))

    
    players = [Brian, Naylor, Pete, Gary, David]
    games = [{'id': 1, 'text': 'DEN -2 @IND'},
             {'id': 1, 'text': '@DET -6.5 CHI'}]
    configure_app(players, games)
    app.run(host='0.0.0.0', port=8080)

