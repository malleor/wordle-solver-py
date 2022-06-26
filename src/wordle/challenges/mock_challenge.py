from .challenge import Challenge

class MockChallenge(Challenge):
    def __init__(self, word):
        super().__init__(word)
