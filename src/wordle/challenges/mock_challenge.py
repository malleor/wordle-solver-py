from .challenge import Challenge

class MockChallenge(Challenge):
    def __init__(self, word):
        super().__init__(word)

    def check_guess(self, guess):
        return super()._check_guess(self.word, guess)
