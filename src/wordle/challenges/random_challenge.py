from .challenge import Challenge
import random

class RandomChallenge(Challenge):
    def __init__(self):
        super().__init__()

        with open('../res/valid_guesses.csv', 'rt') as f:
            w = [str.upper(w[:-1]) for w in f.readlines()[1:]]

        self.word = random.sample(w, 1)[0]

    def check_guess(self, guess):
        return super()._check_guess(self.word, guess)
