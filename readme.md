### How to play the game in a terminal?

Run `python3` and run the game like so:

```
from wordle import *
from getpass import getpass

challenge = MockChallenge(getpass('set the challenge word: '))
solver = InteractiveSolver()
game = Game(challenge, solver, max_trials=6)

game.run()
```

After the prompt, ask someone to type in the challenge word and start solving the puzzle.
It may look like this:

```
>>> game.run()
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

If you'd rather play alone, you can use a randomly selected challenge word.
For this end, use

```
challenge = RandomChallenge()
```

To test the letter frequency solver against a random challenge, use:

```
challenge = RandomChallenge()
solver = DictionarySolver_Random()
```

...which may end up like this:

```
BASTA ➡️ ⬜⬜🟨🟩⬜
good_letters {(3, 'T')}
dislocated_letters [(2, 'S')]
wrong_letters {'A', 'B'}
LIFTS ➡️ ⬜⬜⬜🟩🟨
good_letters {(3, 'T')}
dislocated_letters [(2, 'S'), (4, 'S')]
wrong_letters {'A', 'I', 'F', 'L', 'B'}
SOWTH ➡️ 🟩🟨⬜🟩🟨
good_letters {(3, 'T'), (0, 'S')}
dislocated_letters [(2, 'S'), (4, 'S'), (1, 'O'), (4, 'H')]
wrong_letters {'A', 'I', 'W', 'F', 'L', 'B'}
SHOTT ➡️ 🟩🟩🟩🟩🟨
good_letters {(3, 'T'), (1, 'H'), (0, 'S'), (2, 'O')}
dislocated_letters [(2, 'S'), (4, 'S'), (1, 'O'), (4, 'H'), (4, 'T')]
wrong_letters {'A', 'I', 'W', 'F', 'L', 'B'}
SHOTE ➡️ 🟩🟩🟩🟩🟩
5
```

### Running a benchmark

```
$ python3 -c "from wordle import *; _ = run_games(RandomChallenge, [DictionarySolver_Random])"
```

### Dictionary

The package uses a 5-letter words dictionary from Bill Cruise, available on
[Kaggle](https://www.kaggle.com/datasets/bcruise/wordle-valid-words).
