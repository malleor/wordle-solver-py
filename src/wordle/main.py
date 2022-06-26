MAX_RUNS = 6

def run_challenge(challenge, solver):
    result = []
    for i in range(MAX_RUNS):
        guess = solver.guess(result)
        hit = challenge.check_guess(guess)
        print(guess, '➡️', hit)
        result.append(hit)
        if result[-1].count('🟩') == 5:
            return 1 + i
    return 0
