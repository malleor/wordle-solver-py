from .solver import Solver
from ..challenges.challenge import Challenge
import random


class LetterFreqSolver(Solver):
    def __init__(self):
        super().__init__()

        # load the dictionary
        with open('../res/valid_guesses.csv', 'rt') as f:
            self.dictionary = [str.upper(w[:-1]) for w in f.readlines()]

    def guess(self, results):
        # start with a random guess
        if len(results) == 0:
            return random.sample(self.dictionary, 1)[0]

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
        print('good_letters', good_letters)
        print('dislocated_letters', dislocated_letters)
        print('wrong_letters', wrong_letters)
        all_good_letters_used = lambda w: all([(w[i] == c) for i, c in good_letters])
        contains_no_wrong_letters = lambda w: all([(c not in w) for c in wrong_letters])
        uses_and_moves_all_dislocated = lambda w: all([(c in w and w[i] != c) for i, c in dislocated_letters])

        # select candidate words
        candidates = [w for w in self.dictionary if all_good_letters_used(w) and contains_no_wrong_letters(w) and uses_and_moves_all_dislocated(w)]

        # pick a random candidate
        return random.sample(candidates, 1)[0]
