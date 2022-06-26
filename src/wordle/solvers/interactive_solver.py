from .solver import Solver

class InteractiveSolver(Solver):
    def __init__(self):
        super().__init__()

    def guess(self, results):
        return input('guess the word: ')
