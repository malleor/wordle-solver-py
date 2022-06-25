class MockChallenge():
    GOOD       = '🟩'
    WRONG      = '⬜️'
    DISLOCATED = '🟨'

    def __init__(self, word):
        self.word = word

    def check_word(self, guess):
        def check_letter(w, g):
            if g is w:
                return MockChallenge.GOOD
            if g in self.word:
                return MockChallenge.DISLOCATED
            return MockChallenge.WRONG

        return ''.join([check_letter(w, g) for w, g in zip(self.word, guess)])
