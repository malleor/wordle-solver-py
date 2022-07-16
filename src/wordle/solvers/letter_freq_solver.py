from .solver import Solver
from ..challenges.challenge import Challenge
import random
import string


class DictionarySolver(Solver):
    def __init__(self):
        super().__init__()

        # load the dictionary
        with open('../res/valid_guesses.csv', 'rt') as f:
            self.dictionary = [str.upper(w[:-1]) for w in f.readlines()]

    def _pick_word(self, selection):
        pass

    def guess(self, results, verbose=True):
        # pick an initial guess
        if len(results) == 0:
            return self._pick_word(self.dictionary)

        # understand the current situation
        good_letters = set()
        dislocated_letters = []
        wrong_letters = set()
        for g, h in results:
            for i in range(5):
                if h[i] == Challenge.GOOD:
                    good_letters.add((i,g[i]))
                elif h[i] == Challenge.DISLOCATED:
                    dislocated_letters.append((i,g[i]))
                elif h[i] == Challenge.WRONG:
                    wrong_letters.add(g[i])
        if verbose:
            print('good_letters', good_letters)
            print('dislocated_letters', dislocated_letters)
            print('wrong_letters', wrong_letters)
        all_good_letters_used = lambda w: all([(w[i] == c) for i, c in good_letters])
        contains_no_wrong_letters = lambda w: all([(c not in w) for c in wrong_letters])
        uses_and_moves_all_dislocated = lambda w: all([(c in w and w[i] != c) for i, c in dislocated_letters])

        # select candidate words
        candidates = [w for w in self.dictionary if all_good_letters_used(w) and contains_no_wrong_letters(w) and uses_and_moves_all_dislocated(w)]

        # pick a candidate
        return self._pick_word(candidates)


class DictionarySolver_Random(DictionarySolver):
    def __init__(self):
        super().__init__()

    def _pick_word(self, selection):
        return random.sample(selection, 1)[0]


class DictionarySolver_LetterFreq(DictionarySolver):
    def __init__(self):
        super().__init__()

    def _pick_word(self, selection):
        # calculate word scores based on letter frequency
        stats = {l: [0]*5 for l in string.ascii_uppercase}
        for w in selection:
            for i, c in enumerate(w):
                stats[c][i] += 1
        word_scores = {w: sum([stats[c][i] for i, c in enumerate(w)]) for w in selection}
        return sorted([(w, word_scores[w]) for w in selection], key=lambda x: -x[1])[0][0]
