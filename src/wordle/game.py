from .challenges.challenge import Challenge

class Game():
    CONTINUE = 'continue'
    FAILED = 'failed'
    WIN = 'win'

    def __init__(self, challenge, solver, max_trials=6, verbose=True):
        self.max_trials = max_trials
        self.num_trials = 0
        self.results = []
        self.challenge = challenge
        self.solver = solver
        self.verbose = verbose

    def get_max_trials(self):
        return self.max_trials

    def get_num_trials(self):
        return self.num_trials

    def update_num_trials(self):
        self.num_trials += 1

    def reveal(self):
        return self.challenge.reveal()

    def check_game_status(self,hit):
        if all(h==Challenge.GOOD for h in hit):
            return self.WIN
        elif self.num_trials==self.max_trials:
            return self.FAILED
        else:
            return self.CONTINUE

    def progress(self):
        self.update_num_trials()
        guess = self.solver.guess(
            self.results, self.max_trials, verbose=self.verbose)
        hit = self.challenge.check_guess(guess)
        status = self.check_game_status(hit)
        self.results.append((guess,hit))
        return status, guess, hit

    def run(self):
        while True:
            status, guess, hit = self.progress()

            if self.verbose:
                print(guess, '➡️', ''.join(hit))
            if status==self.WIN:
                num_trials = self.get_num_trials()
                if self.verbose:
                    print(f'{self.get_num_trials()}/{self.get_max_trials()}')
                return self.get_num_trials()
            elif status==self.FAILED:
                if self.verbose:
                    print(self.reveal())
                    print(f'X/{self.get_max_trials()}')
                return
