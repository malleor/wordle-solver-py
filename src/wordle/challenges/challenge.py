class Challenge():
    GOOD       = '🟩'
    WRONG      = '⬜'
    DISLOCATED = '🟨'

    def __init__(self, word):
        self.word = word.upper()

    def reveal(self):
        return self.word

    def check_guess(self, guess):
        def _check_letter(w, g):
            if g is w:
                return self.GOOD
            if g in self.word:
                return self.DISLOCATED
            return self.WRONG

        result = [_check_letter(w, g) for w, g in zip(self.word, guess.upper())]
        return result
