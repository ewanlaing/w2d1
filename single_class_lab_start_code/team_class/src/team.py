class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, missing_player):
        for player in self.players:
            if player == missing_player:
                return True
        return False
    
    points = 0

    def play_game(self, win_state):
        if win_state == True:
            self.points += 3