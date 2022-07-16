from .solver import Solver

class InteractiveSolver(Solver):

    # TODO: It's used in Solver only but it is a proprepry of a Challenge
    CHALLENGE_LENGTH = 5

    def __init__(self):
        super().__init__()

    def guess(self, results, max_trials, verbose=True):
        while len(g:=input('guess the word: '))!=self.CHALLENGE_LENGTH:
            print(f'Type {self.CHALLENGE_LENGTH}-letter word, please!')
        return g
