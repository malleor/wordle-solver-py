### How to play the game in a terminal?

Run `python3` and run the challenge like so:

```
from wordle.solvers.interactive_solver import InteractiveSolver
from wordle.challenges.mock_challenge import MockChallenge
from wordle.main import *
from getpass import getpass
run_challenge(MockChallenge(getpass('set the challenge word: ')), InteractiveSolver())
```

After the prompt, ask someone to type in the challenge word and start solving the puzzle.
It may look like this:

```
>>> run_challenge(MockChallenge(getpass('set the challenge word: ')), InteractiveSolver())
set the challenge word:
guess the word: FINER
FINER ➡️ ⬜️⬜️⬜️⬜️🟨
guess the word: TRUTH
TRUTH ➡️ ⬜️🟨⬜️⬜️⬜️
guess the word: WORRY
WORRY ➡️ ⬜️⬜️🟩🟨⬜️
guess the word: CARDS
CARDS ➡️ 🟨🟨🟩⬜️🟨
guess the word: SCRAP
SCRAP ➡️ 🟩🟩🟩🟩🟩
5
```
