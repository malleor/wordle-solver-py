class Challenge():
    GOOD       = '🟩'
    WRONG      = '⬜️'
    DISLOCATED = '🟨'

    def __init__(self, word):
        self.word = word.upper()

    def _check_guess(self, word, guess):
        def _check_letter(w, g):
            if g is w:
                return Challenge.GOOD
            if g in self.word:
                return Challenge.DISLOCATED
            return Challenge.WRONG

        return ''.join([_check_letter(w, g) for w, g in zip(word, guess)])
