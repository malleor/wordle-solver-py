from .challenge import Challenge
import random

class RandomChallenge(Challenge):
    def __init__(self):

        with open('../res/valid_guesses.csv', 'rt') as f:
            w = [str.upper(w[:-1]) for w in f.readlines()]

        word = random.sample(w, 1)[0]
        super().__init__(word)
