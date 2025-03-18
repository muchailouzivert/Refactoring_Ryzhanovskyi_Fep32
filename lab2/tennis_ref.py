"""
This module contains the TennisGameRefactored class which implements the logic for a tennis game scoring system.
"""

class TennisGameRefactored:
    """
    A class to represent a tennis game and its scoring system.
    """
    
    score_names = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def __init__(self, player1_name, player2_name):
        """
        Initialize the tennis game with player names and initial scores.
        
        :param player1_name: Name of the first player
        :param player2_name: Name of the second player
        """
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        """
        Award a point to the specified player.
        
        :param player_name: Name of the player who won the point
        """
        if player_name == self.player1_name:
            self.p1points += 1
        else:
            self.p2points += 1

    def print_score(self):
        """
        Return the current score of the game in a readable format.
        
        :return: The current score as a string
        """
        score_is_tied = self.check_for_tie()
        someone_won = self.check_for_winner()
        someone_has_advantage = self.check_for_advantage()
        
        if score_is_tied:
            result = self.is_equal()
        else:
            if someone_won:
                result = self.winner()
            elif someone_has_advantage:
                result = self.advantage()
            else:
                result = self.different_scores()   
        return result
    
    def convert_score_to_english(self):
        """
        Convert the numerical scores to their English equivalents.
        
        :return: A tuple containing the English scores of both players
        """
        return self.score_names[self.p1points], self.score_names[self.p2points]
      
    def is_equal(self):
        """
        Check if the scores are equal and return the appropriate score description.
        
        :return: The score description for equal scores
        """
        if 0 <= self.p1points and self.p2points < 4:
            return f"{self.score_names[self.p1points]}-All"
        return "Deuce"
    def different_scores(self):
        """
        Return the score description when the scores are different.
        
        :return: The score description for different scores
        """
        p1_score, p2_score = self.convert_score_to_english()
        return f"{p1_score}-{p2_score}"   
    def check_for_advantage(self):
        """
        Check if either player has an advantage.
        
        :return: True if there is an advantage, False otherwise
        """
        min_score = min(self.p1points, self.p2points)
        abs_diff_score = abs(self.p1points - self.p2points)
        if min_score >= 3 and abs_diff_score == 1:
            return True
        return False
        
    def advantage(self):
        """
        Return the score description when a player has an advantage.
        
        :return: The score description for an advantage
        """
        if self.p1points > self.p2points:
            return f"Advantage {self.player1_name}"
        return f"Advantage {self.player2_name}"
            
    def check_for_winner(self):
        """
        Check if there is a winner.
        
        :return: True if there is a winner, False otherwise
        """
        max_score = max(self.p1points, self.p2points)
        abs_diff_score = abs(self.p1points - self.p2points)
        if max_score > 3 and abs_diff_score != 1:
            return True
        return False
        
    def winner(self):
        """
        Return the score description when a player has won.
        
        :return: The score description for a win
        """
        if self.p1points > self.p2points:
            champ = self.player1_name                    
        else:
            champ = self.player2_name
        return f"Win for {champ}"
            
    def check_for_tie(self):
        """
        Check if the scores are tied.
        
        :return: True if the scores are tied, False otherwise
        """
        if self.p1points == self.p2points:
            return True
        return False