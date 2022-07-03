from .game import Game


def run_games(cls_challenge, cls_solver_list, max_trials=6, n_challenges=100):
    # present the same challenge to each solver
    def _run_game():
        c = cls_challenge()
        sl = [cs() for cs in cls_solver_list]
        rl = [Game(c, s, max_trials=max_trials, verbose=False).run() for s in sl]
        return rl

    # run n challenges
    results = [_run_game() for i in range(n_challenges)]
    results_per_solver = list(zip([s.__name__ for s in cls_solver_list], zip(*results)))

    for solver_name, solver_results in results_per_solver:
        stats = {i: len([0 for r in solver_results if r == i]) for i in range(1, 1+max_trials)}
        stats['X'] = len([0 for r in solver_results if r is None])
        print(solver_name, ':', stats)

    return results_per_solver
