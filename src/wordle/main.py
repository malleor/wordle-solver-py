from .challenges.challenge import Challenge
class Game():
    CONTINUE = 'continue'
    FAILED = 'failed'
    WIN = 'win'

    def __init__(self, max_trials):
        self.max_trials = max_trials
        self.num_trials = 0
        self.results = []

    def get_max_trials(self):
        return self.max_trials

    def get_num_trials(self):
        return self.num_trials

    def update_num_trials(self):
        self.num_trials += 1

    def check_game_status(self,hit):

        if all(h==Challenge.GOOD for h in hit):
            return self.WIN
        elif self.num_trials==self.max_trials:
            return self.FAILED
        else:
            return self.CONTINUE

    def progress(self, challenge, solver):
        self.update_num_trials()
        guess = solver.guess(self.results)
        hit = challenge.check_guess(guess)
        status = self.check_game_status(hit)
        self.results.append((guess,hit))
        return status, guess, hit

def run_challenge(challenge, solver):
    max_trials = 6
    game = Game(max_trials)
    while True:
        status, guess, hit = game.progress(challenge,solver)

        print(guess, '➡️', ''.join(hit))
        if status==game.WIN:
            num_trials = game.get_num_trials()
            print(f'{num_trials}/{max_trials}')
            return
        elif status==game.FAILED:
            print(challenge.reveal())
            print(f'X/{max_trials}')
            return
