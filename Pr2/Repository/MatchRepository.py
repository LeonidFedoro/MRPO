from Class.Match import Match

class MatchRepository:
    def __init__(self):
        self.matches = []

    def add_match(self, match: Match):
        self.matches.append(match)

    def get_match(self, match_id: int):
        for match in self.matches:
            if match.match_id == match_id:
                return match
        return None
