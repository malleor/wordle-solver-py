class Challenge():
    GOOD       = '🟩'
    WRONG      = '⬜'
    DISLOCATED = '🟨'

    def __init__(self, word):
        self.word = word.upper()

    def _check_letter(self, w, g):
        if g is w:
            return Challenge.GOOD
        if g in self.word:
            return Challenge.DISLOCATED
        return Challenge.WRONG

    def reveal(self):
        return self.word

    def check_guess(self, guess):
        result = [self._check_letter(w, g) for w, g in zip(self.word, guess.upper())]
        return result
