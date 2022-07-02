from .challenges.challenge import Challenge

MAX_RUNS = 6

def run_challenge(challenge, solver):
    result = []
    for i in range(MAX_RUNS):
        guess = solver.guess(result).upper()
        hit = challenge.check_guess(guess)
        print(guess, '➡️', hit)
        result.append((guess, hit))
        if hit.count(Challenge.GOOD) == 5:
            return 1 + i
    return 0
